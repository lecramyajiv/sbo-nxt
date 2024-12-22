#ifdef        __dilos__
#include <tdeglobal.h>

class TDEGlobalNetworkManager;
class TDEGlobalNetworkManager;
class TDEHardwareDevices;

TDEGlobalNetworkManager *
TDEInstance::networkManager()const
{

        return (NULL);
}

TDEHardwareDevices *
TDEInstance::hardwareDevices()const
{

        return (NULL);
}

TDEGlobalNetworkManager *
TDEGlobal::networkManager()
{

        return (NULL);
}

TDEHardwareDevices *
TDEGlobal::hardwareDevices()
{

        return (NULL);
}

#include <kuniqueapplication.h>
void
KUniqueApplication::virtual_hook(int, void*)
{
}
#endif        /* __dilos__ */
