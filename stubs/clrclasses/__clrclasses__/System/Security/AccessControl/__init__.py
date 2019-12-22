from __clrclasses__.System import Enum as _n_0_t_0
from __clrclasses__.System import IComparable as _n_0_t_1
from __clrclasses__.System import IFormattable as _n_0_t_2
from __clrclasses__.System import IConvertible as _n_0_t_3
from __clrclasses__.System import Byte as _n_0_t_4
from __clrclasses__.System import Array as _n_0_t_5
from __clrclasses__.System import Type as _n_0_t_6
from __clrclasses__.System import Guid as _n_0_t_7
from __clrclasses__.System import UnauthorizedAccessException as _n_0_t_8
from __clrclasses__.System import Exception as _n_0_t_9
from __clrclasses__.System.Collections import IEnumerator as _n_1_t_0
from __clrclasses__.System.Collections import ReadOnlyCollectionBase as _n_1_t_1
from __clrclasses__.System.Collections import ICollection as _n_1_t_2
from __clrclasses__.System.Runtime.InteropServices import _Exception as _n_2_t_0
from __clrclasses__.System.Runtime.Serialization import ISerializable as _n_3_t_0
from __clrclasses__.System.Security.Principal import IdentityReference as _n_4_t_0
from __clrclasses__.System.Security.Principal import SecurityIdentifier as _n_4_t_1
import typing
T = typing.TypeVar('T')
class AccessControlActions(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Change: int
    _None: int
    value__: int
    View: int
class AccessControlModification(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Add: int
    Remove: int
    RemoveAll: int
    RemoveSpecific: int
    Reset: int
    Set: int
    value__: int
class AccessControlSections(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Access: int
    All: int
    Audit: int
    Group: int
    _None: int
    Owner: int
    value__: int
class AccessControlType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Allow: int
    Deny: int
    value__: int
class AccessRule(AccessRule, typing.Generic[T]):
    @property
    def Rights(self) -> T:"""Rights { get; } -> T"""
    def __init__(self, identity: _n_4_t_0, rights: T, type: AccessControlType) -> AccessRule:...
    def __init__(self, identity: str, rights: T, type: AccessControlType) -> AccessRule:...
    def __init__(self, identity: _n_4_t_0, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule:...
    def __init__(self, identity: str, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> AccessRule:...
class AceEnumerator(_n_1_t_0):
    pass
class AceFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AuditFlags: int
    ContainerInherit: int
    FailedAccess: int
    InheritanceFlags: int
    Inherited: int
    InheritOnly: int
    _None: int
    NoPropagateInherit: int
    ObjectInherit: int
    SuccessfulAccess: int
    value__: int
class AceQualifier(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AccessAllowed: int
    AccessDenied: int
    SystemAlarm: int
    SystemAudit: int
    value__: int
class AceType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AccessAllowed: int
    AccessAllowedCallback: int
    AccessAllowedCallbackObject: int
    AccessAllowedCompound: int
    AccessAllowedObject: int
    AccessDenied: int
    AccessDeniedCallback: int
    AccessDeniedCallbackObject: int
    AccessDeniedObject: int
    MaxDefinedAceType: int
    SystemAlarm: int
    SystemAlarmCallback: int
    SystemAlarmCallbackObject: int
    SystemAlarmObject: int
    SystemAudit: int
    SystemAuditCallback: int
    SystemAuditCallbackObject: int
    SystemAuditObject: int
    value__: int
class AuditFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Failure: int
    _None: int
    Success: int
    value__: int
class AuditRule(AuditRule, typing.Generic[T]):
    @property
    def Rights(self) -> T:"""Rights { get; } -> T"""
    def __init__(self, identity: _n_4_t_0, rights: T, flags: AuditFlags) -> AuditRule:...
    def __init__(self, identity: _n_4_t_0, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule:...
    def __init__(self, identity: str, rights: T, flags: AuditFlags) -> AuditRule:...
    def __init__(self, identity: str, rights: T, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> AuditRule:...
class AuthorizationRule(object):
    @property
    def IdentityReference(self) -> _n_4_t_0:"""IdentityReference { get; } -> IdentityReference"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:"""InheritanceFlags { get; } -> InheritanceFlags"""
    @property
    def IsInherited(self) -> bool:"""IsInherited { get; } -> bool"""
    @property
    def PropagationFlags(self) -> PropagationFlags:"""PropagationFlags { get; } -> PropagationFlags"""
class AuthorizationRuleCollection(_n_1_t_1, _n_1_t_2, typing.Iterable[typing.Any]):
    @property
    def Item(self) -> AuthorizationRule:"""Item { get; } -> AuthorizationRule"""
    def __init__(self) -> AuthorizationRuleCollection:...
    def AddRule(self, rule: AuthorizationRule):...
class CommonAce(QualifiedAce):
    def __init__(self, flags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: _n_4_t_1, isCallback: bool, opaque: _n_0_t_5[_n_0_t_4]) -> CommonAce:...
    @staticmethod
    def MaxOpaqueLength(isCallback: bool) -> int:...
class CommonAcl(GenericAcl, _n_1_t_2, typing.Iterable[typing.Any]):
    @property
    def IsCanonical(self) -> bool:"""IsCanonical { get; } -> bool"""
    @property
    def IsContainer(self) -> bool:"""IsContainer { get; } -> bool"""
    @property
    def IsDS(self) -> bool:"""IsDS { get; } -> bool"""
    def Purge(self, sid: _n_4_t_1):...
    def RemoveInheritedAces(self):...
class CommonObjectSecurity(ObjectSecurity):
    def GetAccessRules(self, includeExplicit: bool, includeInherited: bool, targetType: _n_0_t_6) -> AuthorizationRuleCollection:...
    def GetAuditRules(self, includeExplicit: bool, includeInherited: bool, targetType: _n_0_t_6) -> AuthorizationRuleCollection:...
class CommonSecurityDescriptor(GenericSecurityDescriptor):
    @property
    def DiscretionaryAcl(self) -> DiscretionaryAcl:"""DiscretionaryAcl { get; set; } -> DiscretionaryAcl"""
    @property
    def IsContainer(self) -> bool:"""IsContainer { get; } -> bool"""
    @property
    def IsDiscretionaryAclCanonical(self) -> bool:"""IsDiscretionaryAclCanonical { get; } -> bool"""
    @property
    def IsDS(self) -> bool:"""IsDS { get; } -> bool"""
    @property
    def IsSystemAclCanonical(self) -> bool:"""IsSystemAclCanonical { get; } -> bool"""
    @property
    def SystemAcl(self) -> SystemAcl:"""SystemAcl { get; set; } -> SystemAcl"""
    def __init__(self, isContainer: bool, isDS: bool, flags: ControlFlags, owner: _n_4_t_1, group: _n_4_t_1, systemAcl: SystemAcl, discretionaryAcl: DiscretionaryAcl) -> CommonSecurityDescriptor:...
    def __init__(self, isContainer: bool, isDS: bool, rawSecurityDescriptor: RawSecurityDescriptor) -> CommonSecurityDescriptor:...
    def __init__(self, isContainer: bool, isDS: bool, sddlForm: str) -> CommonSecurityDescriptor:...
    def __init__(self, isContainer: bool, isDS: bool, binaryForm: _n_0_t_5[_n_0_t_4], offset: int) -> CommonSecurityDescriptor:...
    def AddDiscretionaryAcl(self, revision: _n_0_t_4, trusted: int):...
    def AddSystemAcl(self, revision: _n_0_t_4, trusted: int):...
    def PurgeAccessControl(self, sid: _n_4_t_1):...
    def PurgeAudit(self, sid: _n_4_t_1):...
    def SetDiscretionaryAclProtection(self, isProtected: bool, preserveInheritance: bool):...
    def SetSystemAclProtection(self, isProtected: bool, preserveInheritance: bool):...
class CompoundAce(KnownAce):
    @property
    def CompoundAceType(self) -> CompoundAceType:"""CompoundAceType { get; set; } -> CompoundAceType"""
    def __init__(self, flags: AceFlags, accessMask: int, compoundAceType: CompoundAceType, sid: _n_4_t_1) -> CompoundAce:...
class CompoundAceType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    Impersonation: int
    value__: int
class ControlFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DiscretionaryAclAutoInherited: int
    DiscretionaryAclAutoInheritRequired: int
    DiscretionaryAclDefaulted: int
    DiscretionaryAclPresent: int
    DiscretionaryAclProtected: int
    DiscretionaryAclUntrusted: int
    GroupDefaulted: int
    _None: int
    OwnerDefaulted: int
    RMControlValid: int
    SelfRelative: int
    ServerSecurity: int
    SystemAclAutoInherited: int
    SystemAclAutoInheritRequired: int
    SystemAclDefaulted: int
    SystemAclPresent: int
    SystemAclProtected: int
    value__: int
class CryptoKeyAccessRule(AccessRule):
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:"""CryptoKeyRights { get; } -> CryptoKeyRights"""
    def __init__(self, identity: _n_4_t_0, cryptoKeyRights: CryptoKeyRights, type: AccessControlType) -> CryptoKeyAccessRule:...
    def __init__(self, identity: str, cryptoKeyRights: CryptoKeyRights, type: AccessControlType) -> CryptoKeyAccessRule:...
class CryptoKeyAuditRule(AuditRule):
    @property
    def CryptoKeyRights(self) -> CryptoKeyRights:"""CryptoKeyRights { get; } -> CryptoKeyRights"""
    def __init__(self, identity: _n_4_t_0, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags) -> CryptoKeyAuditRule:...
    def __init__(self, identity: str, cryptoKeyRights: CryptoKeyRights, flags: AuditFlags) -> CryptoKeyAuditRule:...
class CryptoKeyRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ChangePermissions: int
    Delete: int
    FullControl: int
    GenericAll: int
    GenericExecute: int
    GenericRead: int
    GenericWrite: int
    ReadAttributes: int
    ReadData: int
    ReadExtendedAttributes: int
    ReadPermissions: int
    Synchronize: int
    TakeOwnership: int
    value__: int
    WriteAttributes: int
    WriteData: int
    WriteExtendedAttributes: int
class CryptoKeySecurity(NativeObjectSecurity):
    def __init__(self) -> CryptoKeySecurity:...
    def __init__(self, securityDescriptor: CommonSecurityDescriptor) -> CryptoKeySecurity:...
    def AddAccessRule(self, rule: CryptoKeyAccessRule):...
    def AddAuditRule(self, rule: CryptoKeyAuditRule):...
    def RemoveAccessRule(self, rule: CryptoKeyAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: CryptoKeyAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: CryptoKeyAccessRule):...
    def RemoveAuditRule(self, rule: CryptoKeyAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: CryptoKeyAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: CryptoKeyAuditRule):...
    def ResetAccessRule(self, rule: CryptoKeyAccessRule):...
    def SetAccessRule(self, rule: CryptoKeyAccessRule):...
    def SetAuditRule(self, rule: CryptoKeyAuditRule):...
class CustomAce(GenericAce):
    MaxOpaqueLength: int
    @property
    def OpaqueLength(self) -> int:"""OpaqueLength { get; } -> int"""
    def __init__(self, type: AceType, flags: AceFlags, opaque: _n_0_t_5[_n_0_t_4]) -> CustomAce:...
    def GetOpaque(self) -> _n_0_t_5[_n_0_t_4]:...
    def SetOpaque(self, opaque: _n_0_t_5[_n_0_t_4]):...
class DirectoryObjectSecurity(ObjectSecurity):
    def GetAccessRules(self, includeExplicit: bool, includeInherited: bool, targetType: _n_0_t_6) -> AuthorizationRuleCollection:...
    def GetAuditRules(self, includeExplicit: bool, includeInherited: bool, targetType: _n_0_t_6) -> AuthorizationRuleCollection:...
class DirectorySecurity(FileSystemSecurity):
    def __init__(self) -> DirectorySecurity:...
    def __init__(self, name: str, includeSections: AccessControlSections) -> DirectorySecurity:...
class DiscretionaryAcl(CommonAcl, _n_1_t_2, typing.Iterable[typing.Any]):
    def __init__(self, isContainer: bool, isDS: bool, capacity: int) -> DiscretionaryAcl:...
    def __init__(self, isContainer: bool, isDS: bool, revision: _n_0_t_4, capacity: int) -> DiscretionaryAcl:...
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl) -> DiscretionaryAcl:...
    def AddAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def AddAccess(self, accessType: AccessControlType, sid: _n_4_t_1, rule: ObjectAccessRule):...
    def AddAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
    def RemoveAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool:...
    def RemoveAccess(self, accessType: AccessControlType, sid: _n_4_t_1, rule: ObjectAccessRule) -> bool:...
    def RemoveAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7) -> bool:...
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: _n_4_t_1, rule: ObjectAccessRule):...
    def RemoveAccessSpecific(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
    def SetAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def SetAccess(self, accessType: AccessControlType, sid: _n_4_t_1, rule: ObjectAccessRule):...
    def SetAccess(self, accessType: AccessControlType, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
class EventWaitHandleAccessRule(AccessRule):
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:"""EventWaitHandleRights { get; } -> EventWaitHandleRights"""
    def __init__(self, identity: _n_4_t_0, eventRights: EventWaitHandleRights, type: AccessControlType) -> EventWaitHandleAccessRule:...
    def __init__(self, identity: str, eventRights: EventWaitHandleRights, type: AccessControlType) -> EventWaitHandleAccessRule:...
class EventWaitHandleAuditRule(AuditRule):
    @property
    def EventWaitHandleRights(self) -> EventWaitHandleRights:"""EventWaitHandleRights { get; } -> EventWaitHandleRights"""
    def __init__(self, identity: _n_4_t_0, eventRights: EventWaitHandleRights, flags: AuditFlags) -> EventWaitHandleAuditRule:...
class EventWaitHandleRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ChangePermissions: int
    Delete: int
    FullControl: int
    Modify: int
    ReadPermissions: int
    Synchronize: int
    TakeOwnership: int
    value__: int
class EventWaitHandleSecurity(NativeObjectSecurity):
    def __init__(self) -> EventWaitHandleSecurity:...
    def AddAccessRule(self, rule: EventWaitHandleAccessRule):...
    def AddAuditRule(self, rule: EventWaitHandleAuditRule):...
    def RemoveAccessRule(self, rule: EventWaitHandleAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: EventWaitHandleAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: EventWaitHandleAccessRule):...
    def RemoveAuditRule(self, rule: EventWaitHandleAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: EventWaitHandleAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: EventWaitHandleAuditRule):...
    def ResetAccessRule(self, rule: EventWaitHandleAccessRule):...
    def SetAccessRule(self, rule: EventWaitHandleAccessRule):...
    def SetAuditRule(self, rule: EventWaitHandleAuditRule):...
class FileSecurity(FileSystemSecurity):
    def __init__(self) -> FileSecurity:...
    def __init__(self, fileName: str, includeSections: AccessControlSections) -> FileSecurity:...
class FileSystemAccessRule(AccessRule):
    @property
    def FileSystemRights(self) -> FileSystemRights:"""FileSystemRights { get; } -> FileSystemRights"""
    def __init__(self, identity: _n_4_t_0, fileSystemRights: FileSystemRights, type: AccessControlType) -> FileSystemAccessRule:...
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, type: AccessControlType) -> FileSystemAccessRule:...
    def __init__(self, identity: _n_4_t_0, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> FileSystemAccessRule:...
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> FileSystemAccessRule:...
class FileSystemAuditRule(AuditRule):
    @property
    def FileSystemRights(self) -> FileSystemRights:"""FileSystemRights { get; } -> FileSystemRights"""
    def __init__(self, identity: _n_4_t_0, fileSystemRights: FileSystemRights, flags: AuditFlags) -> FileSystemAuditRule:...
    def __init__(self, identity: _n_4_t_0, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> FileSystemAuditRule:...
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, flags: AuditFlags) -> FileSystemAuditRule:...
    def __init__(self, identity: str, fileSystemRights: FileSystemRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> FileSystemAuditRule:...
class FileSystemRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    AppendData: int
    ChangePermissions: int
    CreateDirectories: int
    CreateFiles: int
    Delete: int
    DeleteSubdirectoriesAndFiles: int
    ExecuteFile: int
    FullControl: int
    ListDirectory: int
    Modify: int
    Read: int
    ReadAndExecute: int
    ReadAttributes: int
    ReadData: int
    ReadExtendedAttributes: int
    ReadPermissions: int
    Synchronize: int
    TakeOwnership: int
    Traverse: int
    value__: int
    Write: int
    WriteAttributes: int
    WriteData: int
    WriteExtendedAttributes: int
class FileSystemSecurity(NativeObjectSecurity):
    def AddAccessRule(self, rule: FileSystemAccessRule):...
    def AddAuditRule(self, rule: FileSystemAuditRule):...
    def RemoveAccessRule(self, rule: FileSystemAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: FileSystemAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: FileSystemAccessRule):...
    def RemoveAuditRule(self, rule: FileSystemAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: FileSystemAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: FileSystemAuditRule):...
    def ResetAccessRule(self, rule: FileSystemAccessRule):...
    def SetAccessRule(self, rule: FileSystemAccessRule):...
    def SetAuditRule(self, rule: FileSystemAuditRule):...
class GenericAce(object):
    @property
    def AceFlags(self) -> AceFlags:"""AceFlags { get; set; } -> AceFlags"""
    @property
    def AceType(self) -> AceType:"""AceType { get; } -> AceType"""
    @property
    def AuditFlags(self) -> AuditFlags:"""AuditFlags { get; } -> AuditFlags"""
    @property
    def BinaryLength(self) -> int:"""BinaryLength { get; } -> int"""
    @property
    def InheritanceFlags(self) -> InheritanceFlags:"""InheritanceFlags { get; } -> InheritanceFlags"""
    @property
    def IsInherited(self) -> bool:"""IsInherited { get; } -> bool"""
    @property
    def PropagationFlags(self) -> PropagationFlags:"""PropagationFlags { get; } -> PropagationFlags"""
    def Copy(self) -> GenericAce:...
    @staticmethod
    def CreateFromBinaryForm(binaryForm: _n_0_t_5[_n_0_t_4], offset: int) -> GenericAce:...
    def GetBinaryForm(self, binaryForm: _n_0_t_5[_n_0_t_4], offset: int):...
class GenericAcl(_n_1_t_2, typing.Iterable[typing.Any]):
    AclRevision: int
    AclRevisionDS: int
    MaxBinaryLength: int
    @property
    def BinaryLength(self) -> int:"""BinaryLength { get; } -> int"""
    @property
    def Item(self) -> GenericAce:"""Item { get; set; } -> GenericAce"""
    @property
    def Revision(self) -> _n_0_t_4:"""Revision { get; } -> Byte"""
    def GetBinaryForm(self, binaryForm: _n_0_t_5[_n_0_t_4], offset: int):...
class GenericSecurityDescriptor(object):
    @property
    def BinaryLength(self) -> int:"""BinaryLength { get; } -> int"""
    @property
    def ControlFlags(self) -> ControlFlags:"""ControlFlags { get; } -> ControlFlags"""
    @property
    def Group(self) -> _n_4_t_1:"""Group { get; set; } -> SecurityIdentifier"""
    @property
    def Owner(self) -> _n_4_t_1:"""Owner { get; set; } -> SecurityIdentifier"""
    @property
    def Revision(self) -> _n_0_t_4:"""Revision { get; } -> Byte"""
    def GetBinaryForm(self, binaryForm: _n_0_t_5[_n_0_t_4], offset: int):...
    def GetSddlForm(self, includeSections: AccessControlSections) -> str:...
    @staticmethod
    def IsSddlConversionSupported() -> bool:...
class InheritanceFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ContainerInherit: int
    _None: int
    ObjectInherit: int
    value__: int
class KnownAce(GenericAce):
    @property
    def AccessMask(self) -> int:"""AccessMask { get; set; } -> int"""
    @property
    def SecurityIdentifier(self) -> _n_4_t_1:"""SecurityIdentifier { get; set; } -> SecurityIdentifier"""
class MutexAccessRule(AccessRule):
    @property
    def MutexRights(self) -> MutexRights:"""MutexRights { get; } -> MutexRights"""
    def __init__(self, identity: _n_4_t_0, eventRights: MutexRights, type: AccessControlType) -> MutexAccessRule:...
    def __init__(self, identity: str, eventRights: MutexRights, type: AccessControlType) -> MutexAccessRule:...
class MutexAuditRule(AuditRule):
    @property
    def MutexRights(self) -> MutexRights:"""MutexRights { get; } -> MutexRights"""
    def __init__(self, identity: _n_4_t_0, eventRights: MutexRights, flags: AuditFlags) -> MutexAuditRule:...
class MutexRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ChangePermissions: int
    Delete: int
    FullControl: int
    Modify: int
    ReadPermissions: int
    Synchronize: int
    TakeOwnership: int
    value__: int
class MutexSecurity(NativeObjectSecurity):
    def __init__(self) -> MutexSecurity:...
    def __init__(self, name: str, includeSections: AccessControlSections) -> MutexSecurity:...
    def AddAccessRule(self, rule: MutexAccessRule):...
    def AddAuditRule(self, rule: MutexAuditRule):...
    def RemoveAccessRule(self, rule: MutexAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: MutexAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: MutexAccessRule):...
    def RemoveAuditRule(self, rule: MutexAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: MutexAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: MutexAuditRule):...
    def ResetAccessRule(self, rule: MutexAccessRule):...
    def SetAccessRule(self, rule: MutexAccessRule):...
    def SetAuditRule(self, rule: MutexAuditRule):...
class NativeObjectSecurity(CommonObjectSecurity):
    pass
class ObjectAccessRule(AccessRule):
    @property
    def InheritedObjectType(self) -> _n_0_t_7:"""InheritedObjectType { get; } -> Guid"""
    @property
    def ObjectFlags(self) -> ObjectAceFlags:"""ObjectFlags { get; } -> ObjectAceFlags"""
    @property
    def ObjectType(self) -> _n_0_t_7:"""ObjectType { get; } -> Guid"""
class ObjectAce(QualifiedAce):
    @property
    def InheritedObjectAceType(self) -> _n_0_t_7:"""InheritedObjectAceType { get; set; } -> Guid"""
    @property
    def ObjectAceFlags(self) -> ObjectAceFlags:"""ObjectAceFlags { get; set; } -> ObjectAceFlags"""
    @property
    def ObjectAceType(self) -> _n_0_t_7:"""ObjectAceType { get; set; } -> Guid"""
    def __init__(self, aceFlags: AceFlags, qualifier: AceQualifier, accessMask: int, sid: _n_4_t_1, flags: ObjectAceFlags, type: _n_0_t_7, inheritedType: _n_0_t_7, isCallback: bool, opaque: _n_0_t_5[_n_0_t_4]) -> ObjectAce:...
    @staticmethod
    def MaxOpaqueLength(isCallback: bool) -> int:...
class ObjectAceFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    InheritedObjectAceTypePresent: int
    _None: int
    ObjectAceTypePresent: int
    value__: int
class ObjectAuditRule(AuditRule):
    @property
    def InheritedObjectType(self) -> _n_0_t_7:"""InheritedObjectType { get; } -> Guid"""
    @property
    def ObjectFlags(self) -> ObjectAceFlags:"""ObjectFlags { get; } -> ObjectAceFlags"""
    @property
    def ObjectType(self) -> _n_0_t_7:"""ObjectType { get; } -> Guid"""
class ObjectSecurity(NativeObjectSecurity, typing.Generic[T]):
    def AddAccessRule(self, rule: AccessRule[T]):...
    def AddAuditRule(self, rule: AuditRule[T]):...
    def RemoveAccessRule(self, rule: AccessRule[T]) -> bool:...
    def RemoveAccessRuleAll(self, rule: AccessRule[T]):...
    def RemoveAccessRuleSpecific(self, rule: AccessRule[T]):...
    def RemoveAuditRule(self, rule: AuditRule[T]) -> bool:...
    def RemoveAuditRuleAll(self, rule: AuditRule[T]):...
    def RemoveAuditRuleSpecific(self, rule: AuditRule[T]):...
    def ResetAccessRule(self, rule: AccessRule[T]):...
    def SetAccessRule(self, rule: AccessRule[T]):...
    def SetAuditRule(self, rule: AuditRule[T]):...
class PrivilegeNotHeldException(_n_0_t_8, _n_3_t_0, _n_2_t_0):
    @property
    def PrivilegeName(self) -> str:"""PrivilegeName { get; } -> str"""
    def __init__(self) -> PrivilegeNotHeldException:...
    def __init__(self, privilege: str) -> PrivilegeNotHeldException:...
    def __init__(self, privilege: str, inner: _n_0_t_9) -> PrivilegeNotHeldException:...
class PropagationFlags(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    InheritOnly: int
    _None: int
    NoPropagateInherit: int
    value__: int
class QualifiedAce(KnownAce):
    @property
    def AceQualifier(self) -> AceQualifier:"""AceQualifier { get; } -> AceQualifier"""
    @property
    def IsCallback(self) -> bool:"""IsCallback { get; } -> bool"""
    @property
    def OpaqueLength(self) -> int:"""OpaqueLength { get; } -> int"""
    def GetOpaque(self) -> _n_0_t_5[_n_0_t_4]:...
    def SetOpaque(self, opaque: _n_0_t_5[_n_0_t_4]):...
class RawAcl(GenericAcl, _n_1_t_2, typing.Iterable[typing.Any]):
    def __init__(self, revision: _n_0_t_4, capacity: int) -> RawAcl:...
    def __init__(self, binaryForm: _n_0_t_5[_n_0_t_4], offset: int) -> RawAcl:...
    def InsertAce(self, index: int, ace: GenericAce):...
    def RemoveAce(self, index: int):...
class RawSecurityDescriptor(GenericSecurityDescriptor):
    @property
    def DiscretionaryAcl(self) -> RawAcl:"""DiscretionaryAcl { get; set; } -> RawAcl"""
    @property
    def ResourceManagerControl(self) -> _n_0_t_4:"""ResourceManagerControl { get; set; } -> Byte"""
    @property
    def SystemAcl(self) -> RawAcl:"""SystemAcl { get; set; } -> RawAcl"""
    def __init__(self, flags: ControlFlags, owner: _n_4_t_1, group: _n_4_t_1, systemAcl: RawAcl, discretionaryAcl: RawAcl) -> RawSecurityDescriptor:...
    def __init__(self, sddlForm: str) -> RawSecurityDescriptor:...
    def __init__(self, binaryForm: _n_0_t_5[_n_0_t_4], offset: int) -> RawSecurityDescriptor:...
    def SetFlags(self, flags: ControlFlags):...
class RegistryAccessRule(AccessRule):
    @property
    def RegistryRights(self) -> RegistryRights:"""RegistryRights { get; } -> RegistryRights"""
    def __init__(self, identity: _n_4_t_0, registryRights: RegistryRights, type: AccessControlType) -> RegistryAccessRule:...
    def __init__(self, identity: str, registryRights: RegistryRights, type: AccessControlType) -> RegistryAccessRule:...
    def __init__(self, identity: _n_4_t_0, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> RegistryAccessRule:...
    def __init__(self, identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, type: AccessControlType) -> RegistryAccessRule:...
class RegistryAuditRule(AuditRule):
    @property
    def RegistryRights(self) -> RegistryRights:"""RegistryRights { get; } -> RegistryRights"""
    def __init__(self, identity: _n_4_t_0, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> RegistryAuditRule:...
    def __init__(self, identity: str, registryRights: RegistryRights, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, flags: AuditFlags) -> RegistryAuditRule:...
class RegistryRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ChangePermissions: int
    CreateLink: int
    CreateSubKey: int
    Delete: int
    EnumerateSubKeys: int
    ExecuteKey: int
    FullControl: int
    Notify: int
    QueryValues: int
    ReadKey: int
    ReadPermissions: int
    SetValue: int
    TakeOwnership: int
    value__: int
    WriteKey: int
class RegistrySecurity(NativeObjectSecurity):
    def __init__(self) -> RegistrySecurity:...
    def AddAccessRule(self, rule: RegistryAccessRule):...
    def AddAuditRule(self, rule: RegistryAuditRule):...
    def RemoveAccessRule(self, rule: RegistryAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: RegistryAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: RegistryAccessRule):...
    def RemoveAuditRule(self, rule: RegistryAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: RegistryAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: RegistryAuditRule):...
    def ResetAccessRule(self, rule: RegistryAccessRule):...
    def SetAccessRule(self, rule: RegistryAccessRule):...
    def SetAuditRule(self, rule: RegistryAuditRule):...
class ResourceType(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DSObject: int
    DSObjectAll: int
    FileObject: int
    KernelObject: int
    LMShare: int
    Printer: int
    ProviderDefined: int
    RegistryKey: int
    RegistryWow6432Key: int
    Service: int
    Unknown: int
    value__: int
    WindowObject: int
    WmiGuidObject: int
class SecurityInfos(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    DiscretionaryAcl: int
    Group: int
    Owner: int
    SystemAcl: int
    value__: int
class SemaphoreAccessRule(AccessRule):
    @property
    def SemaphoreRights(self) -> SemaphoreRights:"""SemaphoreRights { get; } -> SemaphoreRights"""
    def __init__(self, identity: str, eventRights: SemaphoreRights, type: AccessControlType) -> SemaphoreAccessRule:...
    def __init__(self, identity: _n_4_t_0, eventRights: SemaphoreRights, type: AccessControlType) -> SemaphoreAccessRule:...
class SemaphoreAuditRule(AuditRule):
    @property
    def SemaphoreRights(self) -> SemaphoreRights:"""SemaphoreRights { get; } -> SemaphoreRights"""
    def __init__(self, identity: _n_4_t_0, eventRights: SemaphoreRights, flags: AuditFlags) -> SemaphoreAuditRule:...
class SemaphoreRights(_n_0_t_0, _n_0_t_1, _n_0_t_2, _n_0_t_3):
    ChangePermissions: int
    Delete: int
    FullControl: int
    Modify: int
    ReadPermissions: int
    Synchronize: int
    TakeOwnership: int
    value__: int
class SemaphoreSecurity(NativeObjectSecurity):
    def __init__(self, name: str, includeSections: AccessControlSections) -> SemaphoreSecurity:...
    def __init__(self) -> SemaphoreSecurity:...
    def AddAccessRule(self, rule: SemaphoreAccessRule):...
    def AddAuditRule(self, rule: SemaphoreAuditRule):...
    def RemoveAccessRule(self, rule: SemaphoreAccessRule) -> bool:...
    def RemoveAccessRuleAll(self, rule: SemaphoreAccessRule):...
    def RemoveAccessRuleSpecific(self, rule: SemaphoreAccessRule):...
    def RemoveAuditRule(self, rule: SemaphoreAuditRule) -> bool:...
    def RemoveAuditRuleAll(self, rule: SemaphoreAuditRule):...
    def RemoveAuditRuleSpecific(self, rule: SemaphoreAuditRule):...
    def ResetAccessRule(self, rule: SemaphoreAccessRule):...
    def SetAccessRule(self, rule: SemaphoreAccessRule):...
    def SetAuditRule(self, rule: SemaphoreAuditRule):...
class SystemAcl(CommonAcl, _n_1_t_2, typing.Iterable[typing.Any]):
    def __init__(self, isContainer: bool, isDS: bool, capacity: int) -> SystemAcl:...
    def __init__(self, isContainer: bool, isDS: bool, revision: _n_0_t_4, capacity: int) -> SystemAcl:...
    def __init__(self, isContainer: bool, isDS: bool, rawAcl: RawAcl) -> SystemAcl:...
    def AddAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def AddAudit(self, sid: _n_4_t_1, rule: ObjectAuditRule):...
    def AddAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
    def RemoveAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags) -> bool:...
    def RemoveAudit(self, sid: _n_4_t_1, rule: ObjectAuditRule) -> bool:...
    def RemoveAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7) -> bool:...
    def RemoveAuditSpecific(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def RemoveAuditSpecific(self, sid: _n_4_t_1, rule: ObjectAuditRule):...
    def RemoveAuditSpecific(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
    def SetAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags):...
    def SetAudit(self, sid: _n_4_t_1, rule: ObjectAuditRule):...
    def SetAudit(self, auditFlags: AuditFlags, sid: _n_4_t_1, accessMask: int, inheritanceFlags: InheritanceFlags, propagationFlags: PropagationFlags, objectFlags: ObjectAceFlags, objectType: _n_0_t_7, inheritedObjectType: _n_0_t_7):...
