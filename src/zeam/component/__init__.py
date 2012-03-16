# This is a package.

from zeam.component.components import Component
from zeam.component.site import getSite, queryComponent, getComponent
from grokcore.component import provides, name, implements, adapts

__all__ = ['Component', 'provides', 'name', 'implements', 'adapts',
           'getSite', 'queryComponent', 'getComponent']
