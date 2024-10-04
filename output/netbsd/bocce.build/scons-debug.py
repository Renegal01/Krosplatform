# -*- coding: utf-8 -*-

import sys
import os
import subprocess

exit_code = subprocess.call(
    ['/usr/pkg/bin/python3.12', '-W', 'ignore', '/usr/pkg/lib/python3.12/site-packages/nuitka/build/inline_copy/bin/scons.py', '--quiet', '-f', '/usr/pkg/lib/python3.12/site-packages/nuitka/build/Backend.scons', '--jobs', '3', '--warn=no-deprecated', '--no-site-dir', 'source_dir=.', 'nuitka_python=false', 'debug_mode=false', 'debugger_mode=false', 'python_debug=false', 'module_mode=false', 'full_compat=false', 'experimental=', 'trace_mode=false', 'file_reference_mode=runtime', 'module_count=354', 'result_exe=/root/src/basic/output/netbsd/bocce.dist/bocce.bin', 'standalone_mode=true', 'frozen_modules=153', 'python_sysflag_no_site=true', 'python_sysflag_utf8=true', 'nuitka_src=/usr/pkg/lib/python3.12/site-packages/nuitka/build', 'python_version=3.12', 'python_prefix=/usr/pkg', 'debug_modes=', 'no_deployment=', 'target_arch=amd64'],
    env={'ENV': '/root/.shrc', 'MAKEFLAGS': ' ', 'BLOCKSIZE': '1k', 'PWD': '/root/src/basic', 'MAIL': '/var/mail/root', 'HOME': '/root', 'PATH': '/sbin:/usr/sbin:/bin:/usr/bin:/usr/pkg/sbin:/usr/pkg/bin:/usr/games:/usr/X11R7/bin:/usr/local/sbin:/usr/local/bin', 'HOST': 'MiWiFi-R4AC-srv', 'SSH_CONNECTION': '192.168.31.26 60910 192.168.31.11 22', 'SSH_TTY': '/dev/pts/0', 'MAKELEVEL': '1', 'TERM': 'xterm-256color', 'OLDPWD': '/usr/bin', 'USER': 'root', 'CFLAGS': '-I/usr/pkg/include/python3.12', 'SSH_CLIENT': '192.168.31.26 60910 22', 'LOGNAME': 'root', 'SHELL': '/bin/sh', 'LDFLAGS': '-L/usr/pkg/lib', 'LC_CTYPE': 'C.UTF-8', 'NUITKA_SITE_FILENAME': '5416:/usr/pkg/lib/python3.12/site.py', 'PYTHONHASHSEED': '0', 'NUITKA_PYTHON_EXE_PATH': '/usr/pkg/bin/python3.12', 'NUITKA_PACKAGE_DIR': '/usr/pkg/lib/python3.12/site-packages/nuitka', '_NUITKA_BUILD_DEFINITIONS_CATALOG': '_NUITKA_BUILD_DEFINITIONS_CATALOG', 'NUITKA_QUIET': '0'},
    shell=False
)