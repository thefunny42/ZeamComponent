
import martian
import zeam.component
import grokcore.component
from martian.error import GrokError
from martian.util import isclass
from zope.interface import Interface
from zope.interface.interfaces import ISpecification
from zeam.component.site import getSite
from zope.component import adaptedBy


class ComponentGrokker(martian.ClassGrokker):
    martian.component(zeam.component.Component)
    martian.directive(zeam.component.provides)
    martian.directive(zeam.component.name)

    def execute(self, factory, config, provides, name, **kw):
        specs = adaptedBy(factory)
        context = grokcore.component.context.bind(
            get_default=lambda *args, **kwargs: None).get(factory)
        if specs is None and context is not None:
            validated_specs = (context,)
        else:
            validated_specs = []
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
