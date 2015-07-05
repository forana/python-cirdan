from __future__ import absolute_import

from cirdan.registry import registry, Parameter

def title(value):
    def inner(wrapped):
        item = registry.get(wrapped)
        item.title = value
        return wrapped
    return inner

def description(value):
    def inner(wrapped):
        item = registry.get(wrapped)
        item.description = value
        return wrapped
    return inner

def param(name, description, required = False):
    def inner(wrapped):
        item = registry.get(wrapped)
        item.parameters.append(Parameter(name, description, required))
        return wrapped
    return inner
