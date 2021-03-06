cdist-type__mount(7)
====================
Manage filesystem mounts

Steven Armstrong <steven-cdist--@--armstrong.cc>


DESCRIPTION
-----------
Manage filesystem mounts either via /etc/fstab or manually.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
device
   device to mount at path, defaults to 'none'. see mount(8)

dump
   value for the dump field in fstab. see fstab(5)
   defaults to 0.

   This parameter is ignored, if the nofstab parameter is given.

options
   comma separated string of options, see mount(8)

pass
   value for the pass field in fstab. see fstab(5)
   defaults to 0.

   This parameter is ignored, if the nofstab parameter is given.

path
   mount point where to mount the device, see mount(8).
   Defaults to __object_id

state
   either present or absent. Defaults to present.

type
   vfstype, see mount(8)


BOOLEAN PARAMETERS
------------------
nofstab
   do not manage an entry in /etc/fstab


EXAMPLES
--------

.. code-block:: sh

    __mount /some/dir \
       --device /dev/sdc3 \
       --type xfs \
       --options "defaults,ro"
       --dump 0 \
       --pass 1

    __mount /var/lib/one \
       --device mfsmount \
       --type fuse \
       --options "mfsmaster=mfsmaster.domain.tld,mfssubfolder=/one,nonempty,_netdev"


SEE ALSO
--------
- `cdist-type(7) <cdist-type.html>`_


COPYING
-------
Copyright \(C) 2014 Steven Armstrong. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
