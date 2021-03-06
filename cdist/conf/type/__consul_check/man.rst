cdist-type__consul_check(7)
=============================
Manages consul checks

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Generate and deploy check definitions for a consul agent.
See http://www.consul.io/docs/agent/checks.html for parameter documentation.

Use either script toghether with interval, or use ttl.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
interval
   the interval in which the script given with --script should be run

script
   the shell command to run every --interval

ttl
   how long a check is considered healthy without being updated through the
   HTTP interfave

id
   Defaults to --name

name
   The name of this check. Defaults to __object_id

notes
   human readable description

state
   if this check is 'present' or 'absent'. Defaults to 'present'.


EXAMPLES
--------

.. code-block:: sh

    __consul_check redis \
       --script /usr/local/bin/check_redis.py \
       --interval 10s

    __consul_check some-object-id \
       --id web-app \
       --name "Web App Status" \
       --notes "Web app does a curl internally every 10 seconds" \
       --ttl 30s


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- `cdist-type__consul_agent(7) <cdist-type__consul_agent.html>`_


COPYING
-------
Copyright \(C) 2015 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
