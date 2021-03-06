cdist-type__package_pip(7)
==========================
Manage packages with pip

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
Pip is used in Python environments to install packages.
It is also included in the python virtualenv environment.


REQUIRED PARAMETERS
-------------------
None


OPTIONAL PARAMETERS
-------------------
name
    If supplied, use the name and not the object id as the package name.

pip
    Instead of using pip from PATH, use the specific pip path.

state
    Either "present" or "absent", defaults to "present" 

runas
    Run pip as specified user. By default it runs as root.


EXAMPLES
--------

.. code-block:: sh

    # Install a package
    __package_pip pyro --state present

    # Use pip in a virtualenv located at /root/shinken_virtualenv
    __package_pip pyro --state present --pip /root/shinken_virtualenv/bin/pip

    # Use pip in a virtualenv located at /foo/shinken_virtualenv as user foo
    __package_pip pyro --state present --pip /foo/shinken_virtualenv/bin/pip --runas foo


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__package(7) <cdist-type__package.html>`_


COPYING
-------
Copyright \(C) 2012 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
