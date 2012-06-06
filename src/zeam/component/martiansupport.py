
import martian
import zeam.component
import grokcore.component
from martian.error import GrokError
from martian.util import isclass
from zope.interface import Interface
from zope.interface.interfaces import ISpecification
from zeam.component.site import getSite
from zope.component import adaptedBy


OPTIONS = set(['name', 'provides'])


class DecoratedComponentGrokker(martian.GlobalGrokker):

    def grok(self, name, module, module_info, config, **kw):
        components = module_info.getAnnotation('zeam.components', [])

        for factory, specs, options in components:
            if set(options.keys()).difference(OPTIONS):
                raise GrokError(u'There are unknown options for %s' % factory)
            name = options.get('name', u'')
            provides = options.get('provides', Interface)
            validated_specs = []
            for value in specs:
                if value is None:
                    validated_specs.append(Interface)
                elif ISpecification.providedBy(value) or isclass(value):
                    validated_specs.append(value)
                else:
                    raise GrokError(
                        u"Invalid adaption argument %r for %r" % (
                            value, factory))
            validated_specs = tuple(validated_specs)
            config.action(
                discriminator=('component', validated_specs, provides, name),
                callable=getSite().register,
                args=(factory, validated_specs, provides, name))
        return len(components) != 0


class ComponentGrokker(martian.ClassGrokker):
    martian.component(zeam.component.Component)
    martian.directive(zeam.component.provides)
    martian.directive(zeam.component.name)

    def execute(self, factory, config, provides, name, **kw):
        specs = adaptedBy(factory)
        context = grokcore.component.context.bind(
            get_default=lambda *args, **kwargs: None).get(factory)
        validated_specs = []
        if specs is None:
            if context is not None:
                validated_specs = [context,]
        else:
            default = context is not None and context or Interface
            for value in specs:
                if value is None:
                    validated_specs.append(default)
                elif ISpecification.providedBy(value) or isclass(value):
                    validated_specs.append(value)
                else:
                    raise GrokError(
                        u"Invalid adaption argument %r for %r" % (
                            value, factory))
        validated_specs = tuple(validated_specs)
        config.action(
            discriminator=('component', validated_specs, provides, name),
            callable=getSite().register,
            args=(factory, validated_specs, provides, name))
        return True
