cdist-type__consul_watch_checks(7)
==================================
Manages consul checks watches

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Generate and deploy watch definitions of type 'checks' for a consul agent.
See http://www.consul.io/docs/agent/watches.html for parameter documentation.


REQUIRED PARAMETERS
-------------------
handler
   the handler to invoke when the data view updates


OPTIONAL PARAMETERS
-------------------
datacenter
   can be provided to override the agent's default datacenter

filter-service
   filter to a specific service. Conflicts with --filter-state.

filter-state
   filter to a specific state. Conflicts with --filter-service.

state
   if this watch is 'present' or 'absent'. Defaults to 'present'.

token
   can be provided to override the agent's default ACL token


EXAMPLES
--------

.. code-block:: sh

    __consul_watch_checks some-id \
       --handler /usr/bin/my-handler.sh

    __consul_watch_checks some-id \
       --filter-service consul \
       --handler /usr/bin/my-handler.sh

    __consul_watch_checks some-id \
       --filter-state passing \
       --handler /usr/bin/my-handler.sh


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__consul_agent(7) <cdist-type__consul_agent.html>`_
- http://www.consul.io/docs/agent/watches.html


COPYING
-------
Copyright \(C) 2015 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
