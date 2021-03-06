cdist-type__link(7)
===================
Manage links (hard and symbolic)

Nico Schottelius <nico-cdist--@--schottelius.org>


DESCRIPTION
-----------
This cdist type allows you to manage hard and symbolic links.
The given object id is the destination for the link.


REQUIRED PARAMETERS
-------------------
source
   Specifies the link source.

type
   Specifies the link type: Either hard or symoblic.


OPTIONAL PARAMETERS
-------------------
state
   'present' or 'absent', defaults to 'present'


EXAMPLES
--------

.. code-block:: sh

    # Create hard link of /etc/shadow
    __link /root/shadow --source /etc/shadow --type hard

    # Relative symbolic link
    __link /etc/apache2/sites-enabled/www.test.ch   \
       --source ../sites-available/www.test.ch      \
       --type symbolic

    # Absolute symbolic link
    __link /opt/plone --source /home/services/plone --type symbolic

    # Remove link
    __link /opt/plone --state absent


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_


COPYING
-------
Copyright \(C) 2011-2012 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
