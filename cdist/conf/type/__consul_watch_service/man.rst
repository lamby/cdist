cdist-type__consul_watch_service(7)
===================================
Manages consul service watches

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Generate and deploy watch definitions of type 'service' for a consul agent.
See http://www.consul.io/docs/agent/watches.html for parameter documentation.


REQUIRED PARAMETERS
-------------------
handler
   the handler to invoke when the data view updates

service
   the service to watch for changes


OPTIONAL PARAMETERS
-------------------
datacenter
   can be provided to override the agent's default datacenter

state
   if this watch is 'present' or 'absent'. Defaults to 'present'.

token
   can be provided to override the agent's default ACL token

tag
   filter by tag


BOOLEAN PARAMETERS
------------------
passingonly
   specifies if only hosts passing all checks are displayed


EXAMPLES
--------

.. code-block:: sh

    __consul_watch_service some-id \
       --service consul \
       --handler /usr/bin/my-handler.sh

    __consul_watch_service some-id \
       --service redis \
       --tag production \
       --handler /usr/bin/my-handler.sh

    __consul_watch_service some-id \
       --service redis \
       --tag production \
       --passingonly \
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
