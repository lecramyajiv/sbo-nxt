# import the sipconfig.py for the normal or the debug build

import os
import sys
import sysconfig

sys.path.insert(0, os.path.join(sysconfig.get_path('platstdlib'), 'dist-packages'))

if 'd' in sys.abiflags:
    try:
        from pytdeconfig_d import *
        from pytdeconfig_d import _pkg_config, _default_macros
    except ImportError as msg:
        raise ImportError('No module named pytdeconfig; package python3-pytde-dbg not installed')
else:
    from pytdeconfig_nd import *
    from pytdeconfig_nd import _pkg_config, _default_macros
