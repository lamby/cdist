cdist-type__consul_service(7)
=============================
Manages consul services

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Generate and deploy service definitions for a consul agent.
See http://www.consul.io/docs/agent/services.html for parameter documentation.

Use either script together with interval, or use ttl.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
check-interval
   the interval in which the script given with --check-script should be run

check-script
   the shell command to run every --check-interval

check-ttl
   how long a service is considered healthy without being updated through the
   HTTP interfave

id
   Defaults to --name

name
   The name of this service. Defaults to __object_id

port
   the port at which this service can be reached

state
   if this service is 'present' or 'absent'. Defaults to 'present'.

tag
   a tag to add to this service. Can be specified multiple times.


EXAMPLES
--------

.. code-block:: sh

    __consul_service redis \
       --tag master \
       --tag production \
       --port 8000 \
       --check-script /usr/local/bin/check_redis.py \
       --check-interval 10s

    __consul_service webapp \
       --port 80 \
       --check-ttl 10s


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__consul_agent(7) <cdist-type__consul_agent.html>`_


COPYING
-------
Copyright \(C) 2015 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
