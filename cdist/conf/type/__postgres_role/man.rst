cdist-type__postgres_role(7)
============================
Manage postgres roles

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
This cdist type allows you to create or drop postgres roles.


OPTIONAL PARAMETERS
-------------------
state
    Either "present" or "absent", defaults to "present"

All other parameters map directly to the corresponding postgres createrole
parameters.

password

BOOLEAN PARAMETERS
------------------
All parameter map directly to the corresponding postgres createrole
parameters.

login
createdb
createrole
superuser
inherit

EXAMPLES
--------

.. code-block:: sh

    __postgres_role myrole

    __postgres_role myrole --password 'secret'

    __postgres_role admin --password 'very-secret' --superuser

    __postgres_role dbcustomer --password 'bla' --createdb


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__postgres_database(7) <cdist-type__postgres_database.html>`_
- http://www.postgresql.org/docs/current/static/sql-createrole.html


COPYING
-------
Copyright \(C) 2011 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
