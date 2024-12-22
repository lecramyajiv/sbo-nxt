# import the pytqtconfig.py for the normal or the debug build

import os
import sys
import sysconfig

sys.path.insert(0, os.path.join(sysconfig.get_path('platstdlib'), 'dist-packages', 'PyTQt'))

if 'd' in sys.abiflags:
    try:
        from pytqtconfig_d import *
        from pytqtconfig_d import _pkg_config, _default_macros
    except ImportError as msg:
        raise ImportError('No module named pytqtconfig; package python3-pytqt-dbg not installed')
else:
    from pytqtconfig_nd import *
    from pytqtconfig_nd import _pkg_config, _default_macros
