cdist-type__user(7)
===================
Manage users

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
This cdist type allows you to create or modify users on the target.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
state
    absent or present, defaults to present

comment
    see usermod(8)

home
    see above

gid
    see above

password
    see above

shell
    see above

uid
    see above


BOOLEAN PARAMETERS
------------------
system
    see useradd(8), apply only on user create

create-home
    see useradd(8), apply only on user create

remove-home
    see userdel(8), apply only on user delete


MESSAGES
--------
mod
    User is modified

add
    New user added


EXAMPLES
--------

.. code-block:: sh

    # Create user account for foobar with operating system default settings
    __user foobar

    # Same but with a different shell
    __user foobar --shell /bin/zsh

    # Same but for a system account
    __user foobar --system

    # Set explicit uid and home
    __user foobar --uid 1001 --shell /bin/zsh --home /home/foobar

    # Drop user if exists
    __user foobar --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- usermod(8) or pw(8)


COPYING
-------
Copyright \(C) 2011 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
