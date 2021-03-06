cdist-type__rbenv(7)
====================
Manage rbenv installation

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
This cdist type allows you to manage rbenv installations.
It also installs ruby-build.


OPTIONAL PARAMETERS
-------------------
state
    Either "present" or "absent", defaults to "present"

owner
    Which user should own the rbenv installation, defaults to root


EXAMPLES
--------

.. code-block:: sh

    # Install rbenv including ruby-build for nico
    __rbenv /home/nico

    # Install rbenv including ruby-build for nico
    __rbenv /home/nico --owner nico

    # Bastian does not need rbenv anymore, he began to code C99
    __rbenv /home/bastian --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_


COPYING
-------
Copyright \(C) 2012-2014 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
