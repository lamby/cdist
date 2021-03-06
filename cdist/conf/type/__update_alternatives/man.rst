cdist-type__update_alternatives(7)
==================================
Configure alternatives

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
On Debian and alike systems update-alternatives(1) can be used
to setup alternatives for various programs.
One of the most common used targets is the "editor".


REQUIRED PARAMETERS
-------------------
path
   Use this path for the given alternative


EXAMPLES
--------

.. code-block:: sh

    # Setup vim as the default editor
    __update_alternatives editor --path /usr/bin/vim.basic


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__debconf_set_selections(7) <cdist-type__debconf_set_selections.html>`_
- update-alternatives(8)


COPYING
-------
Copyright \(C) 2013 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
