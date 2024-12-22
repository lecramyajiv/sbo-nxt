# import the sip_tqt_config.py for the normal or the debug build

import os
import sys
import sysconfig

sys.path.insert(0, os.path.join(sysconfig.get_path('platstdlib'), 'dist-packages'))

if 'd' in sys.abiflags:
    try:
        from sip_tqt_config_d import *
        from sip_tqt_config_d import _pkg_config, _default_macros
    except ImportError as msg:
        raise ImportError('No module named sip_tqt_config; package python-sip-tqt-dbg not installed')
else:
    from sip_tqt_config_nd import *
    from sip_tqt_config_nd import _pkg_config, _default_macros
