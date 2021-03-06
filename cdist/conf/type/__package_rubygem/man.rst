cdist-type__package_rubygem(7)
==============================
Manage rubygem packages

Chase Allen James <nx-cdist@nu-ex.com>


DESCRIPTION
-----------
Rubygems is the default package management system for the Ruby programming language.


REQUIRED PARAMETERS
-------------------
None


OPTIONAL PARAMETERS
-------------------
name
    If supplied, use the name and not the object id as the package name.

state
    Either "present" or "absent", defaults to "present"


EXAMPLES
--------

.. code-block:: sh

    # Ensure sinatra is installed
    __package_rubygem sinatra --state present

    # Remove package
    __package_rubygem rails --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__package(7) <cdist-type__package.html>`_


COPYING
-------
Copyright \(C) 2011 Chase Allen James. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
