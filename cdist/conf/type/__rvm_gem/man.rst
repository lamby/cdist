cdist-type__rvm_gemset(7)
==========================
Manage Ruby gems through rvm

Evax Software <contact@evax.fr>


DESCRIPTION
-----------
RVM is the Ruby enVironment Manager for the Ruby programming language.


REQUIRED PARAMETERS
-------------------
user
    The remote user account to use
gemset
    The gemset to use
state
    Either "present" or "absent", defaults to "present".

OPTIONAL PARAMETERS
-------------------
default
    Make the selected gemset the default

EXAMPLES
--------

.. code-block:: sh

    # Install the rails gem in gemset ruby-1.9.3-p0@myset for user bill
    __rvm_gemset rails --gemset ruby-1.9.3-p0@myset --user bill --state present

    # Do the same and also make ruby-1.9.3-p0@myset the default gemset
    __rvm_gemset rails --gemset ruby-1.9.3-p0@myset --user bill \
                       --state present --default

    # Remove it
    __rvm_ruby rails --gemset ruby-1.9.3-p0@myset --user bill --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__rvm(7) <cdist-type__rvm.html>`_
- `cdist-type__rvm_ruby(7) <cdist-type__rvm_ruby.html>`_
- `cdist-type__rvm_gemset(7) <cdist-type__rvm_gemset.html>`_


COPYING
-------
Copyright \(C) 2012 Evax Software. Free use of this software is granted under
the terms of the GNU General Public License version 3 (GPLv3).
