from __clrclasses__.System import ApplicationId as _n_0_t_0
from __clrclasses__.System import ActivationContext as _n_0_t_1
from __clrclasses__.System import ApplicationIdentity as _n_0_t_2
from __clrclasses__.System import Array as _n_0_t_3
from __clrclasses__.System import Enum as _n_0_t_4
from __clrclasses__.System import IComparable as _n_0_t_5
from __clrclasses__.System import IFormattable as _n_0_t_6
from __clrclasses__.System import IConvertible as _n_0_t_7
from __clrclasses__.System import Type as _n_0_t_8
from __clrclasses__.System import Byte as _n_0_t_9
from __clrclasses__.System import SystemException as _n_0_t_10
from __clrclasses__.System import Exception as _n_0_t_11
from __clrclasses__.System import Version as _n_0_t_12
from __clrclasses__.System.Collections import ICollection as _n_1_t_0
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_1
from __clrclasses__.System.Collections import IList as _n_1_t_2
from __clrclasses__.System.Collections import DictionaryEntry as _n_1_t_3
from __clrclasses__.System.Collections.Generic import IList as _n_2_t_0
from __clrclasses__.System.Collections.Generic import IEnumerable as _n_2_t_1
from __clrclasses__.System.Reflection import Assembly as _n_3_t_0
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_4_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_5_t_0
from __clrclasses__.System.Runtime.Serialization import IDeserializationCallback as _n_5_t_1
from __clrclasses__.System.Security import PermissionSet as _n_6_t_0
from __clrclasses__.System.Security import ISecurityEncodable as _n_6_t_1
from __clrclasses__.System.Security import SecurityElement as _n_6_t_2
from __clrclasses__.System.Security import IPermission as _n_6_t_3
from __clrclasses__.System.Security import ISecurityPolicyEncodable as _n_6_t_4
from __clrclasses__.System.Security import PolicyLevelType as _n_6_t_5
from __clrclasses__.System.Security import NamedPermissionSet as _n_6_t_6
from __clrclasses__.System.Security import SecurityZone as _n_6_t_7
from __clrclasses__.System.Security.Cryptography import HashAlgorithm as _n_7_t_0
from __clrclasses__.System.Security.Cryptography.X509Certificates import X509Certificate as _n_8_t_0
from __clrclasses__.System.Security.Permissions import FileIOPermissionAccess as _n_9_t_0
from __clrclasses__.System.Security.Permissions import StrongNamePublicKeyBlob as _n_9_t_1
import typing
class AllMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    def __init__(self) -> AllMembershipCondition:...
class ApplicationDirectory(EvidenceBase):
    @property
    def Directory(self) -> str:"""Directory { get; } -> str"""
    def __init__(self, name: str) -> ApplicationDirectory:...
    def Copy(self) -> object:...
class ApplicationDirectoryMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    def __init__(self) -> ApplicationDirectoryMembershipCondition:...
class ApplicationSecurityInfo(object):
    @property
    def ApplicationEvidence(self) -> Evidence:"""ApplicationEvidence { get; set; } -> Evidence"""
    @property
    def ApplicationId(self) -> _n_0_t_0:"""ApplicationId { get; set; } -> ApplicationId"""
    @property
    def DefaultRequestSet(self) -> _n_6_t_0:"""DefaultRequestSet { get; set; } -> PermissionSet"""
    @property
    def DeploymentId(self) -> _n_0_t_0:"""DeploymentId { get; set; } -> ApplicationId"""
    def __init__(self, activationContext: _n_0_t_1) -> ApplicationSecurityInfo:...
class ApplicationSecurityManager(object):
    @property
    def ApplicationTrustManager(self) -> IApplicationTrustManager:"""ApplicationTrustManager { get; } -> IApplicationTrustManager"""
    @property
    def UserApplicationTrusts(self) -> ApplicationTrustCollection:"""UserApplicationTrusts { get; } -> ApplicationTrustCollection"""
    @staticmethod
    def DetermineApplicationTrust(activationContext: _n_0_t_1, context: TrustManagerContext) -> bool:...
class ApplicationTrust(EvidenceBase, _n_6_t_1):
    @property
    def ApplicationIdentity(self) -> _n_0_t_2:"""ApplicationIdentity { get; set; } -> ApplicationIdentity"""
    @property
    def DefaultGrantSet(self) -> PolicyStatement:"""DefaultGrantSet { get; set; } -> PolicyStatement"""
    @property
    def ExtraInfo(self) -> object:"""ExtraInfo { get; set; } -> object"""
    @property
    def FullTrustAssemblies(self) -> _n_2_t_0[StrongName]:"""FullTrustAssemblies { get; } -> IList"""
    @property
    def IsApplicationTrustedToRun(self) -> bool:"""IsApplicationTrustedToRun { get; set; } -> bool"""
    @property
    def Persist(self) -> bool:"""Persist { get; set; } -> bool"""
    def __init__(self, defaultGrantSet: _n_6_t_0, fullTrustAssemblies: _n_2_t_1[StrongName]) -> ApplicationTrust:...
    def __init__(self) -> ApplicationTrust:...
    def __init__(self, applicationIdentity: _n_0_t_2) -> ApplicationTrust:...
class ApplicationTrustCollection(_n_1_t_0, typing.Iterable[ApplicationTrust]):
    @property
    def Item(self) -> ApplicationTrust:"""Item { get; } -> ApplicationTrust"""
    def Add(self, trust: ApplicationTrust) -> int:...
    def AddRange(self, trusts: ApplicationTrustCollection):...
    def AddRange(self, trusts: _n_0_t_3[ApplicationTrust]):...
    def Clear(self):...
    def Find(self, applicationIdentity: _n_0_t_2, versionMatch: ApplicationVersionMatch) -> ApplicationTrustCollection:...
    def Remove(self, trust: ApplicationTrust):...
    def Remove(self, applicationIdentity: _n_0_t_2, versionMatch: ApplicationVersionMatch):...
    def RemoveRange(self, trusts: ApplicationTrustCollection):...
    def RemoveRange(self, trusts: _n_0_t_3[ApplicationTrust]):...
class ApplicationTrustEnumerator(_n_1_t_1):
    pass
class ApplicationVersionMatch(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    MatchAllVersions: int
    MatchExactVersion: int
    value__: int
class CodeConnectAccess(object):
    AnyScheme: int
    DefaultPort: int
    OriginPort: int
    OriginScheme: int
    @property
    def Port(self) -> int:"""Port { get; } -> int"""
    @property
    def Scheme(self) -> str:"""Scheme { get; } -> str"""
    def __init__(self, allowScheme: str, allowPort: int) -> CodeConnectAccess:...
    @staticmethod
    def CreateAnySchemeAccess(allowPort: int) -> CodeConnectAccess:...
    @staticmethod
    def CreateOriginSchemeAccess(allowPort: int) -> CodeConnectAccess:...
class CodeGroup(object):
    @property
    def AttributeString(self) -> str:"""AttributeString { get; } -> str"""
    @property
    def Children(self) -> _n_1_t_2:"""Children { get; set; } -> IList"""
    @property
    def Description(self) -> str:"""Description { get; set; } -> str"""
    @property
    def MembershipCondition(self) -> IMembershipCondition:"""MembershipCondition { get; set; } -> IMembershipCondition"""
    @property
    def MergeLogic(self) -> str:"""MergeLogic { get; } -> str"""
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PermissionSetName(self) -> str:"""PermissionSetName { get; } -> str"""
    @property
    def PolicyStatement(self) -> PolicyStatement:"""PolicyStatement { get; set; } -> PolicyStatement"""
    def AddChild(self, group: CodeGroup):...
    def Copy(self) -> CodeGroup:...
    def FromXml(self, e: _n_6_t_2):...
    def FromXml(self, e: _n_6_t_2, level: PolicyLevel):...
    def RemoveChild(self, group: CodeGroup):...
    def Resolve(self, evidence: Evidence) -> PolicyStatement:...
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:...
    def ToXml(self, level: PolicyLevel) -> _n_6_t_2:...
    def ToXml(self) -> _n_6_t_2:...
class Evidence(_n_1_t_0):
    @property
    def IsReadOnly(self) -> bool:"""IsReadOnly { get; } -> bool"""
    @property
    def Locked(self) -> bool:"""Locked { get; set; } -> bool"""
    def __init__(self, hostEvidence: _n_0_t_3[object], assemblyEvidence: _n_0_t_3[object]) -> Evidence:...
    def __init__(self, evidence: Evidence) -> Evidence:...
    def __init__(self) -> Evidence:...
    def AddAssembly(self, id: object):...
    def AddAssemblyEvidence(self, evidence: typing.Any):...
    def AddHost(self, id: object):...
    def AddHostEvidence(self, evidence: typing.Any):...
    def Clear(self):...
    def Clone(self) -> Evidence:...
    def GetAssemblyEnumerator(self) -> _n_1_t_1:...
    def GetAssemblyEvidence(self) -> typing.Any:...
    def GetHostEnumerator(self) -> _n_1_t_1:...
    def GetHostEvidence(self) -> typing.Any:...
    def Merge(self, evidence: Evidence):...
    def RemoveType(self, t: _n_0_t_8):...
class EvidenceBase(object):
    def Clone(self) -> EvidenceBase:...
class FileCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    def __init__(self, membershipCondition: IMembershipCondition, access: _n_9_t_0) -> FileCodeGroup:...
class FirstMatchCodeGroup(CodeGroup):
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement) -> FirstMatchCodeGroup:...
class GacInstalled(EvidenceBase, IIdentityPermissionFactory):
    def __init__(self) -> GacInstalled:...
    def Copy(self) -> object:...
class GacMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    def __init__(self) -> GacMembershipCondition:...
class Hash(EvidenceBase, _n_5_t_0):
    @property
    def MD5(self) -> _n_0_t_3[_n_0_t_9]:"""MD5 { get; } -> Array"""
    @property
    def SHA1(self) -> _n_0_t_3[_n_0_t_9]:"""SHA1 { get; } -> Array"""
    @property
    def SHA256(self) -> _n_0_t_3[_n_0_t_9]:"""SHA256 { get; } -> Array"""
    def __init__(self, assembly: _n_3_t_0) -> Hash:...
    @staticmethod
    def CreateMD5(md5: _n_0_t_3[_n_0_t_9]) -> Hash:...
    @staticmethod
    def CreateSHA1(sha1: _n_0_t_3[_n_0_t_9]) -> Hash:...
    @staticmethod
    def CreateSHA256(sha256: _n_0_t_3[_n_0_t_9]) -> Hash:...
    def GenerateHash(self, hashAlg: _n_7_t_0) -> _n_0_t_3[_n_0_t_9]:...
class HashMembershipCondition(_n_5_t_0, _n_5_t_1, IMembershipCondition, IReportMatchMembershipCondition):
    @property
    def HashAlgorithm(self) -> _n_7_t_0:"""HashAlgorithm { get; set; } -> HashAlgorithm"""
    @property
    def HashValue(self) -> _n_0_t_3[_n_0_t_9]:"""HashValue { get; set; } -> Array"""
    def __init__(self, hashAlg: _n_7_t_0, value: _n_0_t_3[_n_0_t_9]) -> HashMembershipCondition:...
class IApplicationTrustManager(_n_6_t_1):
    def DetermineApplicationTrust(self, activationContext: _n_0_t_1, context: TrustManagerContext) -> ApplicationTrust:...
class IIdentityPermissionFactory():
    def CreateIdentityPermission(self, evidence: Evidence) -> _n_6_t_3:...
class IMembershipCondition(_n_6_t_1, _n_6_t_4):
    def Check(self, evidence: Evidence) -> bool:...
    def Copy(self) -> IMembershipCondition:...
    def Equals(self, obj: object) -> bool:...
    def ToString(self) -> str:...
class NetCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    AbsentOriginScheme: int
    AnyOtherOriginScheme: int
    def __init__(self, membershipCondition: IMembershipCondition) -> NetCodeGroup:...
    def AddConnectAccess(self, originScheme: str, connectAccess: CodeConnectAccess):...
    def GetConnectAccessRules(self) -> _n_0_t_3[_n_1_t_3]:...
    def ResetConnectAccess(self):...
class PermissionRequestEvidence(EvidenceBase):
    @property
    def DeniedPermissions(self) -> _n_6_t_0:"""DeniedPermissions { get; } -> PermissionSet"""
    @property
    def OptionalPermissions(self) -> _n_6_t_0:"""OptionalPermissions { get; } -> PermissionSet"""
    @property
    def RequestedPermissions(self) -> _n_6_t_0:"""RequestedPermissions { get; } -> PermissionSet"""
    def __init__(self, request: _n_6_t_0, optional: _n_6_t_0, denied: _n_6_t_0) -> PermissionRequestEvidence:...
    def Copy(self) -> PermissionRequestEvidence:...
class PolicyException(_n_0_t_10, _n_5_t_0, _n_4_t_0):
    def __init__(self, message: str, exception: _n_0_t_11) -> PolicyException:...
    def __init__(self, message: str) -> PolicyException:...
    def __init__(self) -> PolicyException:...
class PolicyLevel(object):
    @property
    def FullTrustAssemblies(self) -> _n_1_t_2:"""FullTrustAssemblies { get; } -> IList"""
    @property
    def Label(self) -> str:"""Label { get; } -> str"""
    @property
    def NamedPermissionSets(self) -> _n_1_t_2:"""NamedPermissionSets { get; } -> IList"""
    @property
    def RootCodeGroup(self) -> CodeGroup:"""RootCodeGroup { get; set; } -> CodeGroup"""
    @property
    def StoreLocation(self) -> str:"""StoreLocation { get; } -> str"""
    @property
    def Type(self) -> _n_6_t_5:"""Type { get; } -> PolicyLevelType"""
    def AddFullTrustAssembly(self, snMC: StrongNameMembershipCondition):...
    def AddFullTrustAssembly(self, sn: StrongName):...
    def AddNamedPermissionSet(self, permSet: _n_6_t_6):...
    def ChangeNamedPermissionSet(self, name: str, pSet: _n_6_t_0) -> _n_6_t_6:...
    @staticmethod
    def CreateAppDomainLevel() -> PolicyLevel:...
    def FromXml(self, e: _n_6_t_2):...
    def GetNamedPermissionSet(self, name: str) -> _n_6_t_6:...
    def Recover(self):...
    def RemoveFullTrustAssembly(self, snMC: StrongNameMembershipCondition):...
    def RemoveFullTrustAssembly(self, sn: StrongName):...
    def RemoveNamedPermissionSet(self, name: str) -> _n_6_t_6:...
    def RemoveNamedPermissionSet(self, permSet: _n_6_t_6) -> _n_6_t_6:...
    def Reset(self):...
    def Resolve(self, evidence: Evidence) -> PolicyStatement:...
    def ResolveMatchingCodeGroups(self, evidence: Evidence) -> CodeGroup:...
    def ToXml(self) -> _n_6_t_2:...
class PolicyStatement(_n_6_t_4, _n_6_t_1):
    @property
    def Attributes(self) -> PolicyStatementAttribute:"""Attributes { get; set; } -> PolicyStatementAttribute"""
    @property
    def AttributeString(self) -> str:"""AttributeString { get; } -> str"""
    @property
    def PermissionSet(self) -> _n_6_t_0:"""PermissionSet { get; set; } -> PermissionSet"""
    def __init__(self, permSet: _n_6_t_0, attributes: PolicyStatementAttribute) -> PolicyStatement:...
    def __init__(self, permSet: _n_6_t_0) -> PolicyStatement:...
    def Copy(self) -> PolicyStatement:...
class PolicyStatementAttribute(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    All: int
    Exclusive: int
    LevelFinal: int
    Nothing: int
    value__: int
class Publisher(EvidenceBase, IIdentityPermissionFactory):
    @property
    def Certificate(self) -> _n_8_t_0:"""Certificate { get; } -> X509Certificate"""
    def __init__(self, cert: _n_8_t_0) -> Publisher:...
    def Copy(self) -> object:...
class PublisherMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    @property
    def Certificate(self) -> _n_8_t_0:"""Certificate { get; set; } -> X509Certificate"""
    def __init__(self, certificate: _n_8_t_0) -> PublisherMembershipCondition:...
class Site(EvidenceBase, IIdentityPermissionFactory):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    def __init__(self, name: str) -> Site:...
    def Copy(self) -> object:...
    @staticmethod
    def CreateFromUrl(url: str) -> Site:...
class SiteMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    @property
    def Site(self) -> str:"""Site { get; set; } -> str"""
    def __init__(self, site: str) -> SiteMembershipCondition:...
class StrongName(EvidenceBase, IIdentityPermissionFactory, IDelayEvaluatedEvidence):
    @property
    def Name(self) -> str:"""Name { get; } -> str"""
    @property
    def PublicKey(self) -> _n_9_t_1:"""PublicKey { get; } -> StrongNamePublicKeyBlob"""
    @property
    def Version(self) -> _n_0_t_12:"""Version { get; } -> Version"""
    def __init__(self, blob: _n_9_t_1, name: str, version: _n_0_t_12) -> StrongName:...
    def Copy(self) -> object:...
class StrongNameMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    @property
    def Name(self) -> str:"""Name { get; set; } -> str"""
    @property
    def PublicKey(self) -> _n_9_t_1:"""PublicKey { get; set; } -> StrongNamePublicKeyBlob"""
    @property
    def Version(self) -> _n_0_t_12:"""Version { get; set; } -> Version"""
    def __init__(self, blob: _n_9_t_1, name: str, version: _n_0_t_12) -> StrongNameMembershipCondition:...
class TrustManagerContext(object):
    @property
    def IgnorePersistedDecision(self) -> bool:"""IgnorePersistedDecision { get; set; } -> bool"""
    @property
    def KeepAlive(self) -> bool:"""KeepAlive { get; set; } -> bool"""
    @property
    def NoPrompt(self) -> bool:"""NoPrompt { get; set; } -> bool"""
    @property
    def Persist(self) -> bool:"""Persist { get; set; } -> bool"""
    @property
    def PreviousApplicationIdentity(self) -> _n_0_t_2:"""PreviousApplicationIdentity { get; set; } -> ApplicationIdentity"""
    @property
    def UIContext(self) -> TrustManagerUIContext:"""UIContext { get; set; } -> TrustManagerUIContext"""
    def __init__(self, uiContext: TrustManagerUIContext) -> TrustManagerContext:...
    def __init__(self) -> TrustManagerContext:...
class TrustManagerUIContext(_n_0_t_4, _n_0_t_5, _n_0_t_6, _n_0_t_7):
    Install: int
    Run: int
    Upgrade: int
    value__: int
class UnionCodeGroup(CodeGroup, IUnionSemanticCodeGroup):
    def __init__(self, membershipCondition: IMembershipCondition, policy: PolicyStatement) -> UnionCodeGroup:...
class Url(EvidenceBase, IIdentityPermissionFactory):
    @property
    def Value(self) -> str:"""Value { get; } -> str"""
    def __init__(self, name: str) -> Url:...
    def Copy(self) -> object:...
class UrlMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    @property
    def Url(self) -> str:"""Url { get; set; } -> str"""
    def __init__(self, url: str) -> UrlMembershipCondition:...
class Zone(EvidenceBase, IIdentityPermissionFactory):
    @property
    def SecurityZone(self) -> _n_6_t_7:"""SecurityZone { get; } -> SecurityZone"""
    def __init__(self, zone: _n_6_t_7) -> Zone:...
    def Copy(self) -> object:...
    @staticmethod
    def CreateFromUrl(url: str) -> Zone:...
class ZoneMembershipCondition(IMembershipCondition, IConstantMembershipCondition, IReportMatchMembershipCondition):
    @property
    def SecurityZone(self) -> _n_6_t_7:"""SecurityZone { get; set; } -> SecurityZone"""
    def __init__(self, zone: _n_6_t_7) -> ZoneMembershipCondition:...
