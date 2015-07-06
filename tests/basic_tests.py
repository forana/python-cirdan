import cirdan.registry
import falcon

from cirdan.decorators import *

cirdan.inject()

"""
This really just makes sure it compiles. Doesn't do any meaningful checks.
"""
def test_all_the_things():
    api = falcon.API()

    @title("This is something")
    @description("Definitely something, I tell you what")
    class SomeResource:
        @title("Maybe this is a route")
        @param("hello", "what's up")
        @description("bananas")
        @param("hi", "what's up")
        @param("good morning", "what's up")
        @param("greetings", "what's up")
        @param("ayyyyyy", "what's up")
        def on_get(self, req, res):
            res.body = "{}"

        def on_post(self, req, res):
            res.body = "{}"

        @title("hi")
        def on_put(self, req, res):
            res.body = "{}"

        @description("hello")
        def on_patch(self, req, res):
            res.body = "{}"

        @param("what is this", "what are thooooose")
        def on_delete(self, req, res):
            res.body = "{}"

    class CompletelyUndocumentedResource:
        def on_get(self, req, res):
            res.body = "{}"

    api.add_route("/something", SomeResource())
    api.add_route("/undocumented", CompletelyUndocumentedResource())

    cirdan.set_meta(api, name = "This test", intro_text = "This is my intro")
    cirdan.registry.dump(api)
