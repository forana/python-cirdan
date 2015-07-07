from __future__ import absolute_import

"""
Resource and route decorators.
"""

from cirdan.registry import registry, Parameter, ReturnStatus

# Marks the title of a resource class or route method.
def title(value):
    def inner(wrapped):
        item = registry.get(wrapped)
        item.title = value
        return wrapped
    return inner

# Marks the description of a resource class or route method.
def description(value):
    def inner(wrapped):
        item = registry.get(wrapped)
        item.description = value
        return wrapped
    return inner

# Marks a parameter to a route.
def param(name, description, required = False):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.parameters.append(Parameter(name, description, required))
        return wrapped
    return inner

def returns_status(status_code, description):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.return_statuses.append(ReturnStatus(status_code, description))
        return wrapped
    return inner

def content_type(value):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.content_type = value
        return wrapped
    return inner

def requires_permission(value):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.requires_permission = value
        return wrapped
    return inner
