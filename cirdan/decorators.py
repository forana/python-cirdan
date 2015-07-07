from __future__ import absolute_import

"""
Resource and route decorators.
"""

import json

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

# Marks that a resource class or route method should not appear in docs
def secret(wrapped):
    item = registry.get(wrapped)
    item.secret = True
    return wrapped

# Marks a parameter to a route.
def param(name, description, required = False):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.parameters.append(Parameter(name, description, required))
        return wrapped
    return inner

# Marks that a route can return a certain status under a certain condition
def returns_status(status_code, description):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.return_statuses.append(ReturnStatus(status_code, description))
        return wrapped
    return inner

# Marks that a route will return a certain content type under successful conditions.
def content_type(value):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.content_type = value
        return wrapped
    return inner

# Marks that a route requires a certain permission
def requires_permission(value):
    def inner(wrapped):
        route = registry.get(wrapped)
        route.requires_permission = value
        return wrapped
    return inner

# Provides an example request and/or response for a route
def example(request = None, response = None):
    def inner(wrapped):
        route = registry.get(wrapped)
        if request is not None:
            route.example_request = request if isinstance(request, str) else json.dumps(request, indent = 4)
        if response is not None:
            route.example_response = response if isinstance(response, str) else json.dumps(response, indent = 4)
        return wrapped
    return inner
