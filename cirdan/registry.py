from __future__ import absolute_import

import inspect
import itertools
import re

from collections import OrderedDict

class Resource:
    def __init__(self, cls):
        self.title = cls.__name__
        self.path = "???"
        self.description = None
        self.methods = []

    def safe_title(self):
        assert(hasattr(self, "title"))
        return re.sub("[^A-Za-z0-9_\-]", "", self.title.strip().replace(" ", "_"));

    def __str__(self):
        return "%s - %s" % (self.title, self.path)

class RouteMethod:
    def __init__(self, func):
        self.verb = METHODS_TO_VERBS[func.__name__]
        self.title = self.verb
        self.description = None
        self.parameters = []

    def __str__(self):
        return "%s: %s" % (self.verb, str(self.title))

class Parameter:
    def __init__(self, name, description, required):
        self.name = name
        self.description = description
        self.required = required

    def __star__(self):
        return "%s: %s (required = %s" % (self.name, self.description, repr(self.required))

METHODS_TO_VERBS = OrderedDict([
    ("on_post", "POST"),
    ("on_get", "GET"),
    ("on_put", "PUT"),
    ("on_delete", "DELETE"),
    ("on_patch", "PATCH")
])

class Registry:
    def __init__(self):
        self.api_to_resources = {}
        self.api_meta = {}
        self.resources = {}
        self.route_methods = {}

    def get(self, item):
        if inspect.isclass(item):
            if id(item) not in self.resources:
                self.resources[id(item)] = Resource(item)
            return self.resources[id(item)]
        else:
            if id(item) not in self.route_methods:
                self.route_methods[id(item)] = RouteMethod(item)
            return self.route_methods[id(item)]

    def knows_about(self, api):
        return api in self.api_to_resources

    def bind_api(self, api, resource):
        if api not in self.api_to_resources:
            self.api_to_resources[api] = []
        self.api_to_resources[api].append(resource)

    def set_api_meta(self, api, **kwargs):
        self.api_meta[api] = kwargs

    def dump(self, api):
        for resource in self.api_to_resources[api]:
            print(resource)
            for method in resource.methods:
                print("\t" + str(method))

registry = Registry()
