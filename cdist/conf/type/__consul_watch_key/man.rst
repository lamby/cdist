cdist-type__consul_watch_key(7)
===============================
Manages consul key watches

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Generate and deploy watch definitions of type 'key' for a consul agent.
See http://www.consul.io/docs/agent/watches.html for parameter documentation.


REQUIRED PARAMETERS
-------------------
handler
   the handler to invoke when the data view updates

key
   the key to watch for changes


OPTIONAL PARAMETERS
-------------------
datacenter
   can be provided to override the agent's default datacenter

state
   if this watch is 'present' or 'absent'. Defaults to 'present'.

token
   can be provided to override the agent's default ACL token


EXAMPLES
--------

.. code-block:: sh

    __consul_watch_key some-id \
       --key foo/bar/baz \
       --handler /usr/bin/my-key-handler.sh


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__consul_agent(7) <cdist-type__consul_agent.html>`_
- http://www.consul.io/docs/agent/watches.html


COPYING
-------
Copyright \(C) 2015 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
