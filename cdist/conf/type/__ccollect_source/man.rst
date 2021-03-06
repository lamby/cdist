cdist-type__ccollect_source(7)
==============================
Manage ccollect sources

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
This cdist type allows you to create or delete ccollect sources.


REQUIRED PARAMETERS
-------------------
source
    The source from which to backup
destination
    The destination directory


OPTIONAL PARAMETERS
-------------------
state
    'present' or 'absent', defaults to 'present'
ccollectconf
    The CCOLLECT_CONF directory. Defaults to /etc/ccollect.


OPTIONAL MULTIPLE PARAMETERS
----------------------------
exclude
    Paths to exclude of backup


BOOLEAN PARAMETERS
------------------
verbose
    Whether to report backup verbosely


EXAMPLES
--------

.. code-block:: sh

    __ccollect_source doc.ungleich.ch \
        --source doc.ungleich.ch:/ \
        --destination /backup/doc.ungleich.ch \
        --exclude '/proc/*' --exclude '/sys/*' \
        --verbose


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- ccollect(1)
- http://www.nico.schottelius.org/software/ccollect/


COPYING
-------
Copyright \(C) 2014 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
