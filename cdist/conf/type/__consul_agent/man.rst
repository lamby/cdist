cdist-type__consul_agent(7)
===========================
Manage the consul agent

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Configure and manage the consul agent.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
acl-datacenter
   only used by servers. This designates the datacenter which is authoritative
   for ACL information.

acl-default-policy
   either "allow" or "deny"; defaults to "allow". The default policy controls the
   behavior of a token when there is no matching rule.

acl-down-policy
   either "allow", "deny" or "extend-cache"; "extend-cache" is the default.

acl-master-token
   only used for servers in the acl_datacenter. This token will be created with
   management-level permissions if it does not exist. It allows operators to
   bootstrap the ACL system with a token ID that is well-known.

acl-token
   when provided, the agent will use this token when making requests to the
   Consul servers.

acl-ttl
   used to control Time-To-Live caching of ACLs.

bind-addr
   sets the bind address for cluster communication

bootstrap-expect
   sets server to expect bootstrap mode

ca-file-source
   path to a PEM encoded certificate authority file which will be uploaded and
   configure using the ca_file config option.

cert-file-source
   path to a PEM encoded certificate file which will be uploaded and
   configure using the cert_file config option.

client-addr
   sets the address to bind for client access

datacenter
   datacenter of the agent

encrypt
   provides the gossip encryption key

group
   the primary group for the agent

json-config
   path to a partial json config file without leading { and trailing }.
   If json-config is '-' (dash), take what was written to stdin as the file content.

key-file-source
   path to a PEM encoded private key file which will be uploaded and
   configure using the key_file config option.

node-name
   name of this node. Must be unique in the cluster

retry-join
   address to attempt joining every retry_interval until at least one join works.
   Can be specified multiple times.

user
   the user to run the agent as

state
   if the agent is 'present' or 'absent'. Defaults to 'present'.
   Currently state=absent is not working due to some dependency issues.


BOOLEAN PARAMETERS
------------------
disable-remote-exec
   disables support for remote execution. When set to true, the agent will ignore any incoming remote exec requests.

disable-update-check
   disables automatic checking for security bulletins and new version releases

leave-on-terminate
   gracefully leave cluster on SIGTERM

rejoin-after-leave
   rejoin the cluster using the previous state after leaving

server
   used to control if an agent is in server or client mode

syslog
   enables logging to syslog

verify-incoming
   enforce the use of TLS and verify a client's authenticity on incomming connections

verify-outgoing
   enforce the use of TLS and verify the peers authenticity on outgoing connections


EXAMPLES
--------

.. code-block:: sh

    # configure as server, bootstrap and rejoin
    hostname="$(cat "$__global/explorer/hostname")"
    __consul_agent \
       --datacenter dc1 \
       --node-name "${hostname%%.*}" \
       --disable-update-check \
       --server \
       --rejoin-after-leave \
       --bootstrap-expect 3 \
       --retry-join consul-01 \
       --retry-join consul-02 \
       --retry-join consul-03

    # configure as server, bootstrap and rejoin with ssl support
    hostname="$(cat "$__global/explorer/hostname")"
    __consul_agent \
       --datacenter dc1 \
       --node-name "${hostname%%.*}" \
       --disable-update-check \
       --server \
       --rejoin-after-leave \
       --bootstrap-expect 3 \
       --retry-join consul-01 \
       --retry-join consul-02 \
       --retry-join consul-03 \
       --ca-file-source /path/to/ca.pem \
       --cert-file-source /path/to/cert.pem \
       --key-file-source /path/to/key.pem \
       --verify-incoming \
       --verify-outgoing

    # configure as client and try joining existing cluster
    __consul_agent \
       --datacenter dc1 \
       --node-name "${hostname%%.*}" \
       --disable-update-check \
       --retry-join consul-01 \
       --retry-join consul-02 \
       --retry-join consul-03


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_
- http://www.consul.io/docs/agent/options.html


COPYING
-------
Copyright \(C) 2015 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
