# -*- coding: utf-8 -*-
#
# 2011 Steven Armstrong (steven-cdist at armstrong.cc)
#
# This file is part of cdist.
#
# cdist is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cdist is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cdist. If not, see <http://www.gnu.org/licenses/>.
#
#

import os
import tempfile
import unittest
import shutil
import getpass

import cdist
from cdist import core
from cdist import test
from cdist.exec import local
from cdist.exec import remote
from cdist.core import code

import os.path as op
my_dir = op.abspath(op.dirname(__file__))
fixtures = op.join(my_dir, 'fixtures')
local_base_path = fixtures

class ExplorerClassTestCase(unittest.TestCase):

    def mkdtemp(self, **kwargs):
        return tempfile.mkdtemp(prefix='tmp.cdist.test.', **kwargs)

    def mkstemp(self, **kwargs):
        return tempfile.mkstemp(prefix='tmp.cdist.test.', **kwargs)

    def setUp(self):
        target_host = 'localhost'

        self.local_base_path = local_base_path
        self.out_path = self.mkdtemp()
        self.local = local.Local(target_host, self.local_base_path, self.out_path)
        self.local.create_directories()

        self.remote_base_path = self.mkdtemp()
        self.user = getpass.getuser()
        remote_exec = "ssh -o User=%s -q" % self.user
        remote_copy = "scp -o User=%s -q" % self.user
        self.remote = remote.Remote(target_host, self.remote_base_path, remote_exec, remote_copy)

        self.code = code.Code(target_host, self.local, self.remote)

        self.cdist_type = core.Type(self.local.type_path, '__dump_environment')
        self.cdist_object = core.Object(self.cdist_type, self.local.object_path, 'whatever')
        self.cdist_object.create()

    def tearDown(self):
        shutil.rmtree(self.out_path)
        shutil.rmtree(self.remote_base_path)

    def test_run_gencode_local_environment(self):
        output_string = self.code.run_gencode_local(self.cdist_object)
        output_dict = {}
        for line in output_string.split('\n'):
            if line:
                junk,value = line.split(': ')
                key = junk.split(' ')[1]
                output_dict[key] = value
        self.assertEqual(output_dict['__target_host'], self.local.target_host)
        self.assertEqual(output_dict['__global'], self.local.out_path)
        self.assertEqual(output_dict['__type'], self.cdist_type.absolute_path)
        self.assertEqual(output_dict['__object'], self.cdist_object.absolute_path)
        self.assertEqual(output_dict['__object_id'], self.cdist_object.object_id)
        self.assertEqual(output_dict['__object_fq'], self.cdist_object.path)

    def test_run_gencode_remote_environment(self):
        output_string = self.code.run_gencode_remote(self.cdist_object)
        output_dict = {}
        for line in output_string.split('\n'):
            if line:
                junk,value = line.split(': ')
                key = junk.split(' ')[1]
                output_dict[key] = value
        self.assertEqual(output_dict['__target_host'], self.local.target_host)
        self.assertEqual(output_dict['__global'], self.local.out_path)
        self.assertEqual(output_dict['__type'], self.cdist_type.absolute_path)
        self.assertEqual(output_dict['__object'], self.cdist_object.absolute_path)
        self.assertEqual(output_dict['__object_id'], self.cdist_object.object_id)
        self.assertEqual(output_dict['__object_fq'], self.cdist_object.path)

    def test_transfer_code_remote(self):
        self.cdist_object.code_remote = self.code.run_gencode_remote(self.cdist_object)
        self.code.transfer_code_remote(self.cdist_object)
        destination = os.path.join(self.remote.object_path, self.cdist_object.code_remote_path)
        self.assertTrue(os.path.isfile(destination))

    def test_run_code_local_environment(self):
        self.cdist_object.code_local = self.code.run_gencode_local(self.cdist_object)
        output_string = self.code.run_code_local(self.cdist_object)
        output_dict = {}
        for line in output_string.split('\n'):
            if line:
                key,value = line.split(': ')
                output_dict[key] = value
        self.assertEqual(output_dict['__target_host'], self.local.target_host)
        self.assertEqual(output_dict['__global'], self.local.out_path)
        self.assertEqual(output_dict['__type'], self.cdist_type.absolute_path)
        self.assertEqual(output_dict['__object'], self.cdist_object.absolute_path)
        self.assertEqual(output_dict['__object_id'], self.cdist_object.object_id)
        self.assertEqual(output_dict['__object_fq'], self.cdist_object.path)
        
    def test_run_code_remote_environment(self):
        self.cdist_object.code_remote = self.code.run_gencode_remote(self.cdist_object)
        output_string = self.code.run_code_remote(self.cdist_object)
        output_dict = {}
        for line in output_string.split('\n'):
            if line:
                key,value = line.split(': ')
                output_dict[key] = value
        self.assertEqual(output_dict['__target_host'], self.local.target_host)
        self.assertEqual(output_dict['__global'], self.local.out_path)
        self.assertEqual(output_dict['__type'], self.cdist_type.absolute_path)
        self.assertEqual(output_dict['__object'], self.cdist_object.absolute_path)
        self.assertEqual(output_dict['__object_id'], self.cdist_object.object_id)
        self.assertEqual(output_dict['__object_fq'], self.cdist_object.path)

'''
    def test_list_type_explorer_names(self):
        cdist_type = core.Type(self.local.type_path, '__test_type')
        expected = cdist_type.explorers
        self.assertEqual(self.explorer.list_type_explorer_names(cdist_type), expected)

    def test_transfer_type_explorers(self):
        cdist_type = core.Type(self.local.type_path, '__test_type')
        self.explorer.transfer_type_explorers(cdist_type)
        source = os.path.join(self.local.type_path, cdist_type.explorer_path)
        destination = os.path.join(self.remote.type_path, cdist_type.explorer_path)
        self.assertEqual(os.listdir(source), os.listdir(destination))

    def test_transfer_object_parameters(self):
        cdist_type = core.Type(self.local.type_path, '__test_type')
        cdist_object = core.Object(cdist_type, self.local.object_path, 'whatever')
        cdist_object.parameters = {'first': 'first value', 'second': 'second value'}
        self.explorer.transfer_object_parameters(cdist_object)
        source = os.path.join(self.local.object_path, cdist_object.parameter_path)
        destination = os.path.join(self.remote.object_path, cdist_object.parameter_path)
        self.assertEqual(os.listdir(source), os.listdir(destination))

    def test_run_type_explorer(self):
        cdist_type = core.Type(self.local.type_path, '__test_type')
        cdist_object = core.Object(cdist_type, self.local.object_path, 'whatever')
        self.explorer.transfer_type_explorers(cdist_type)
        output = self.explorer.run_type_explorer('world', cdist_object)
        self.assertEqual(output, 'hello\n')
'''
