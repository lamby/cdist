cdist-type__start_on_boot(7)
============================
Manage stuff to be started at boot

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
This cdist type allows you to enable or disable stuff to be started
at boot of your operating system.

Warning: This type has not been tested intensively and is not fully
supported (i.e. \*BSD are not implemented).


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
state
    Either "present" or "absent", defaults to "present"
target_runlevel
    Runlevel which should be modified, defaults to "default" (only used on gentoo systems).


EXAMPLES
--------

.. code-block:: sh

    # Ensure snmpd is started at boot
    __start_on_boot snmpd

    # Same, but more explicit
    __start_on_boot snmpd --state present

    # Ensure legacy configuration management will not be started
    __start_on_boot puppet --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__process(7) <cdist-type__process.html>`_


COPYING
-------
Copyright \(C) 2012 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
