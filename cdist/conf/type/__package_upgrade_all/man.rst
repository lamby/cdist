cdist-type__package_upgrade_all(7)
==================================
Upgrade all the installed packages

Ricardo Catalinas Jiménez <jimenezrick--@--gmail.com>


DESCRIPTION
-----------
This cdist type allows you to upgrade all the installed packages on the
target. It will automatically use the appropriate package manager.


REQUIRED PARAMETERS
-------------------
None


OPTIONAL PARAMETERS
-------------------
type
    The package manager to use. Default is determined based on the $os
    explorer variable.
    e.g.
    * apt for Debian
    * yum for Red Hat
    * pacman for Arch Linux


EXAMPLES
--------

.. code-block:: sh

    # Upgrade all the installed packages on the target
    __package_upgrade_all

    # Force use of a specific package manager
    __package_upgrade_all --type apt


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_


COPYING
-------
Copyright \(C) 2014 Ricardo Catalinas Jiménez. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
