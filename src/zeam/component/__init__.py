# This is a package.

from zeam.component.components import Component, component
from zeam.component.site import getSite
from zeam.component.site import getWrapper, getComponent, getAllComponents
from grokcore.component import provides, name, implements, adapts


__all__ = ['Component', 'component',
           'getSite', 'getWrapper', 'getComponent', 'getAllComponents',
           'provides', 'name', 'implements', 'adapts']
