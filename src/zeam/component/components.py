
import sys


class ComponentLookupError(Exception):
    pass


class Component(object):
    pass


def component(*interfaces, **options):

    def decorator(function):
        f_locals = sys._getframe(1).f_locals
        components = f_locals.get('__zeam_components__', None)
        if components is None:
            components = f_locals['__zeam_components__'] = []
        components.append((function, interfaces, options))
        return function

    return decorator
