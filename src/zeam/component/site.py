
from zope.interface import Interface, providedBy, implementedBy
from zope.interface.adapter import AdapterRegistry
from zope.interface.interfaces import ISpecification
from zope.testing.cleanup import addCleanUp

from zeam.component.components import ComponentLookupError


def specificationOfInstance(obj):
    if ISpecification.providedBy(obj):
        return obj
    return providedBy(obj)

def specificationOfClass(obj):
    if ISpecification.providedBy(obj):
        return obj
    return implementedBy(obj)

def readSpecification(specs, transformer):
    if isinstance(specs, (list, tuple)):
        return tuple(transformer(spec) for spec in specs)
    return (transformer(specs),)


class Site(object):

    def __init__(self):
        self.clear()

    def lookup(self, specs=(), provided=Interface, name=u'', default=None):
        specs = readSpecification(specs, specificationOfInstance)
        return self.components.lookup(specs, provided, name, default)

    def lookupAll(self, specs=(), provided=Interface):
        specs = readSpecification(specs, specificationOfInstance)
        return self.components.lookupAll(specs, provided)

    def register(self, component, for_=None, provided=Interface, name=u''):
        if for_ is None:
            for_ = tuple()
        else:
            assert isinstance(for_, tuple) or ISpecification.providedBy(for_)
        specs = readSpecification(for_, specificationOfClass)
        self.components.register(specs, provided, name, component)

    def unregister(self, for_=None, provided=Interface, name=u''):
        if for_ is None:
            for_ = tuple()
        else:
            assert isinstance(for_, tuple) or ISpecification.providedBy(for_)
        specs = readSpecification(for_, specificationOfClass)
        self.components.unregister(specs, provided, name)

    def clear(self):
        self.components = AdapterRegistry()


global_site = Site()
_marker = object()

addCleanUp(global_site.clear)

def getSite():
    return global_site

def getComponent(specs=(), provided=Interface, name=u'', default=_marker):
    component = getSite().lookup(specs, provided, name, default)
    if component is _marker:
        raise ComponentLookupError(specs, provided, name)
    return component

def getAllComponents(specs=(), provided=Interface):
    return getSite().lookupAll(specs, provided)

def getWrapper(specs=(), provided=Interface, name=u'', default=_marker):
    if not isinstance(specs, tuple):
        specs = (specs,)
    component = getSite().lookup(specs, provided, name, default)
    if component is _marker:
        raise ComponentLookupError(specs, provided, name)
    return component(*specs)
