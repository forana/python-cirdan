from __future__ import absolute_import

import falcon
import os.path

from cirdan.resource import DocsResource
from cirdan.registry import registry, METHODS_TO_VERBS

route_path = "/docs"
template_path = os.path.join(os.path.dirname(__file__), "default.jinja2")
cache_template = True

def inject():
    falcon.API._wrapped_add_route = falcon.API.add_route
    falcon.API.add_route = register

def set_meta(api, name = "Docs", intro_text = "", **kwargs):
    registry.set_api_meta(api, name = name, intro_text = intro_text, **kwargs)

def register(api, path, resource):
    api._wrapped_add_route(path, resource)
    add_docs_route(api)
    cls = resource.__class__
    wrapped_resource = registry.get(cls)
    wrapped_resource.path = path
    registry.bind_api(api, wrapped_resource)
    for method, verb in METHODS_TO_VERBS.items():
        if hasattr(cls, method):
            f = getattr(cls, method)
            if hasattr(f, "__func__"): # python 2.X
                f = f.__func__
            wrapped_resource.methods.append(registry.get(f))

def add_docs_route(api):
    if not registry.knows_about(api):
        api._wrapped_add_route(route_path, DocsResource(api))
