cdist-type__package(7)
======================
Manage packages

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
This cdist type allows you to install or uninstall packages on the target.
It dispatches the actual work to the package system dependent types.


REQUIRED PARAMETERS
-------------------
None


OPTIONAL PARAMETERS
-------------------
name
    The name of the package to install. Default is to use the object_id as the
    package name.
version
    The version of the package to install. Default is to install the version
    chosen by the local package manager.
type
    The package type to use. Default is determined based on the $os explorer
    variable.
    e.g.
    * __package_apt for Debian
    * __package_emerge for Gentoo

state
    Either "present" or "absent", defaults to "present"


EXAMPLES
--------

.. code-block:: sh

    # Install the package vim on the target
    __package vim --state present

    # Same but install specific version
    __package vim --state present --version 7.3.50

    # Force use of a specific package type
    __package vim --state present --type __package_apt


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_


COPYING
-------
Copyright \(C) 2011 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
