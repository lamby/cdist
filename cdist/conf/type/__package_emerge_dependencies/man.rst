cdist-type__package_emerge_dependencies(7)
==========================================
Install dependencies for __package_emerge

Thomas Oettli <otho--@--sfs.biz>


DESCRIPTION
-----------
Portage is usually used on the gentoo distribution to manage packages.
This type installs the following tools which are required by __package_emerge to work:

* app-portage/flaggie
* app-portage/gentoolkit


REQUIRED PARAMETERS
-------------------
None


OPTIONAL PARAMETERS
-------------------
None


EXAMPLES
--------

.. code-block:: sh

    # Ensure app-portage/flaggie and app-portage/gentoolkit are installed
    __package_emerge_dependencies


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__package(7) <cdist-type__package.html>`_
- `cdist-type__package_emerge(7) <cdist-type__package_emerge.html>`_


COPYING
-------
Copyright \(C) 2013 Thomas Oettli. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
