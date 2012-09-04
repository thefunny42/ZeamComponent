==============
zeam.component
==============

``zeam.component`` is inspired by ``zope.component`` and
``grokcore.component``, but stays much simpler, and have less
base concepts. Hopefully this improve flexibility.

Registration
------------

A base class can be used to register a component,
``zeam.component.Component``. It supports all the directives
``grok.context``, ``grok.adapts``, ``grok.provides`` and ``grok.name``
like they are defined in Grok. You can use those to register your
component as either an Utility, an (named) Adapter or a (named)
MultiAdapter.

An another possibility to register a component is to use the
``component`` decorator, ``zeam.component.component``. It takes as
arguments the interfaces that the component adapts, and as keyword
arguments, ``provides`` the `Interface` that the component provides,
and as ``name`` the name under which it will be registered.

Lookup
------

You can lookup a specific registered component with
``zeam.component.getComponent``. You can optionally provide:

- ``specs``: a tuple of objects or specifications that the component
  must adapt in order to be returned.

- ``provided``: an `Interface` that the component must provides in
  order to be returned.

- ``name``: a name under which the component must be registered in
  order to be returned.

- ``default``: a default value that will be returned if no component
  match the requirements. If you no default value is provided, and no
  component is found, an exception will be triggered.


You can lookup a list of possible registered component with
``zeam.component.getAllComponents``. You can optionally provide:

- ``specs``: tuple of objects or specification stat the component must
  adapt in order to be returned.

- ``provided``: an `Interface` that the component must provides in
  order to be returned.


Please note that in both cases the component is directly returned. In
any case, no construction is done with the result of the lookup.

An helper ``zeam.component.getWrapper`` that support the same options
than the ``zeam.component.getComponent`` function will call the result
of the lookup passing as argument the values given as ``specs`` to
it. This is used in order to have a `getAdapter` or `queryAdapter`
like behavior. Please note that if an error happens during the
initialization of the component, the error won't be catched for you.
