cdist(1)
========
Usable Configuration Management

Nico Schottelius <nico-cdist--@--schottelius.org>


SYNOPSIS
--------

::

    cdist [-h] [-d] [-v] [-V] {banner,config,shell} ...

    cdist banner [-h] [-d] [-v]

    cdist config [-h] [-d] [-V] [-c CONF_DIR] [-f HOSTFILE] [-i MANIFEST] [-p] [-s] [host [host ...]]

    cdist shell [-h] [-d] [-v] [-s SHELL]


DESCRIPTION
-----------
cdist is the frontend executable to the cdist configuration management.
cdist supports different subcommands as explained below.

GENERAL
-------
All commands accept the following options:

.. option:: -d, --debug

    Set log level to debug

.. option:: -h, --help

   Show the help screen

.. option:: -v, --verbose

    Set log level to info, be more verbose

.. option:: -V, --version

   Show version and exit


BANNER
------
Displays the cdist banner. Useful for printing
cdist posters - a must have for every office.


CONFIG
------
Configure one or more hosts

.. option:: -h, --help

    Show the help screen

.. option:: -c CONF_DIR, --conf-dir CONF_DIR

    Add a configuration directory. Can be specified multiple times.
    If configuration directories contain conflicting types, explorers or
    manifests, then the last one found is used. Additionally this can also
    be configured by setting the CDIST_PATH environment variable to a colon
    delimited list of config directories. Directories given with the
    --conf-dir argument have higher precedence over those set through the
    environment variable.

.. option:: -f HOSTFILE, --file HOSTFILE

    Read additional hosts to operate on from specified file
    or from stdin if '-' (each host on separate line).
    If no host or host file is specified then, by default,
    read hosts from stdin.

.. option:: -i MANIFEST, --initial-manifest MANIFEST

    Path to a cdist manifest or - to read from stdin

.. option:: -p, --parallel

    Operate on multiple hosts in parallel

.. option:: -s, --sequential

    Operate on multiple hosts sequentially

.. option:: --remote-copy REMOTE_COPY

    Command to use for remote copy (should behave like scp)

.. option:: --remote-exec REMOTE_EXEC

    Command to use for remote execution (should behave like ssh)

SHELL
-----
This command allows you to spawn a shell that enables access
to the types as commands. It can be thought as an
"interactive manifest" environment. See below for example
usage. Its primary use is for debugging type parameters.

.. option:: -s/--shell

    Select shell to use, defaults to current shell


EXAMPLES
--------

.. code-block:: sh

    # Configure ikq05.ethz.ch with debug enabled
    % cdist config -d ikq05.ethz.ch

    # Configure hosts in parallel and use a different configuration directory
    % cdist config -c ~/p/cdist-nutzung \
        -p ikq02.ethz.ch ikq03.ethz.ch ikq04.ethz.ch

    # Use custom remote exec / copy commands
    % cdist config --remote-exec /path/to/my/remote/exec \
        --remote-copy /path/to/my/remote/copy \
        -p ikq02.ethz.ch ikq03.ethz.ch ikq04.ethz.ch

    # Configure hosts read from file loadbalancers
    % cdist config -f loadbalancers

    # Display banner
    cdist banner

    # Show help
    % cdist --help

    # Show Version
    % cdist --version

    # Enter a shell that has access to emulated types
    % cdist shell
    % __git
    usage: __git --source SOURCE [--state STATE] [--branch BRANCH]
                 [--group GROUP] [--owner OWNER] [--mode MODE] object_id


ENVIRONMENT
-----------
TMPDIR, TEMP, TMP
    Setup the base directory for the temporary directory.
    See http://docs.python.org/py3k/library/tempfile.html for
    more information. This is rather useful, if the standard
    directory used does not allow executables.

CDIST_LOCAL_SHELL
    Selects shell for local script execution, defaults to /bin/sh

CDIST_REMOTE_SHELL
    Selects shell for remote scirpt execution, defaults to /bin/sh

CDIST_REMOTE_EXEC
    Use this command for remote execution (should behave like ssh)

CDIST_REMOTE_COPY
    Use this command for remote copy (should behave like scp)

EXIT STATUS
-----------
The following exit values shall be returned:

0
    Successful completion
1
    One or more host configurations failed


SEE ALSO
--------
- `cdist-type(7) <../man7/cdist-type.html>`_
- `cdist-reference(7) <../man7/cdist-reference.html>`_


COPYING
-------
Copyright \(C) 2011-2013 Nico Schottelius. Free use of this software is
granted under the terms of the GNU General Public License version 3 (GPLv3).
