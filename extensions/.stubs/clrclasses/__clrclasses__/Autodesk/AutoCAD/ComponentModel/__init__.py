from __clrclasses__.System import Attribute as _n_0_t_0
from __clrclasses__.System import Array as _n_0_t_1
from __clrclasses__.System import Type as _n_0_t_2
from __clrclasses__.System.Collections.ObjectModel import ReadOnlyCollection as _n_1_t_0
from __clrclasses__.System.ComponentModel import PropertyDescriptorCollection as _n_2_t_0
from __clrclasses__.System.ComponentModel import PropertyDescriptor as _n_2_t_1
from __clrclasses__.System.ComponentModel import TypeDescriptionProvider as _n_2_t_2
from __clrclasses__.System.Runtime.InteropServices import _Attribute as _n_3_t_0
import typing
TComponent = typing.TypeVar('TComponent')
TPropertyValue = typing.TypeVar('TPropertyValue')
T = typing.TypeVar('T')
class IPropertyProvider():
    def GetProperties(self, instance: object) -> _n_2_t_0:...
class ITypeDescriptor():
    @property
    def HasPerInstancePropertyProviders(self) -> bool:"""HasPerInstancePropertyProviders { get; } -> bool"""
    def AddPerInstancePropertyProvider(self, pp: IPropertyProvider):...
    def AddProperty(self, prop: _n_2_t_1):...
    def GetPerInstancePropertyProviders(self) -> _n_1_t_0[IPropertyProvider]:...
    def ModifyPropertyCollection(self, defaultProps: _n_2_t_0, instance: object) -> _n_2_t_0:...
    def RemovePerInstancePropertyProvider(self, pp: IPropertyProvider):...
    def RemoveProperty(self, prop: _n_2_t_1):...
class PropertyDescriptorBase(_n_2_t_1, typing.Generic[TComponent, TPropertyValue]):
    def __init__(self, name: str, att: _n_0_t_1[_n_0_t_0]) -> PropertyDescriptorBase:...
    def __init__(self, name: str) -> PropertyDescriptorBase:...
class PropertyProviderAttribute(_n_0_t_0, _n_3_t_0):
    @property
    def PropertyProviderType(self) -> _n_0_t_2:"""PropertyProviderType { get; } -> Type"""
    def __init__(self, type: _n_0_t_2) -> PropertyProviderAttribute:...
class TypeDescriptionProvider(_n_2_t_2, typing.Generic[T]):
    def __init__(self) -> TypeDescriptionProvider:...
class TypeDescriptor(ITypeDescriptor):
    def __init__(self, type: _n_0_t_2) -> TypeDescriptor:...
class TypeManager(typing.Iterable[ITypeDescriptor]):
    @property
    def Instance(self) -> TypeManager:"""Instance { get; } -> TypeManager"""
    @property
    def Item(self) -> ITypeDescriptor:"""Item { get; } -> ITypeDescriptor"""