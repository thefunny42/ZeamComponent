# This is a package.

from zeam.component.components import Component, component
from zeam.component.site import getSite, getWrapper, getComponent
from grokcore.component import provides, name, implements, adapts


__all__ = ['Component', 'component',
           'getSite', 'getWrapper', 'getComponent',
           'provides', 'name', 'implements', 'adapts']
