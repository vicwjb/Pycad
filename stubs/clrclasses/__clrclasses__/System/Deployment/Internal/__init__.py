from __clrclasses__.System import ActivationContext as _n_0_t_0
from __clrclasses__.System import Byte as _n_0_t_1
from __clrclasses__.System import Array as _n_0_t_2
from __clrclasses__.System import ApplicationIdentity as _n_0_t_3
import typing
class InternalActivationContextHelper(object):
    @staticmethod
    def GetActivationContextData(appInfo: _n_0_t_0) -> object:...
    @staticmethod
    def GetApplicationComponentManifest(appInfo: _n_0_t_0) -> object:...
    @staticmethod
    def GetApplicationManifestBytes(appInfo: _n_0_t_0) -> _n_0_t_2[_n_0_t_1]:...
    @staticmethod
    def GetDeploymentComponentManifest(appInfo: _n_0_t_0) -> object:...
    @staticmethod
    def GetDeploymentManifestBytes(appInfo: _n_0_t_0) -> _n_0_t_2[_n_0_t_1]:...
    @staticmethod
    def IsFirstRun(appInfo: _n_0_t_0) -> bool:...
    @staticmethod
    def PrepareForExecution(appInfo: _n_0_t_0):...
class InternalApplicationIdentityHelper(object):
    @staticmethod
    def GetInternalAppId(id: _n_0_t_3) -> object:...
