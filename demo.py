import falcon
import cirdan, cirdan.registry
import os
from cirdan.decorators import *

from wsgiref import simple_server

@title("First Resource, nicely named")
class FirstResource():
    @title("Retrieve all things")
    def on_get(self, req, res):
        res.body = '{"hello": "world"}'

    @title("Create a thing")
    @description("I have a description")
    @content_type("application/json")
    @requires_permission("Admin")
    def on_post(self, req, res):
        res.body = '{"hello": "world"}'

    def not_a_route(self):
        pass

    # route with no decorators at all
    def on_put(self, req, res):
        res.body = "{}"

    @secret
    def on_delete(self, req, res):
        res.body = "{}"

class SecondResource():
    @title("Retrieve a thing")
    @description("I have parameters AND a description. I'm such a cool route.")
    @param("param1", "This is a query parameter")
    @param("param2", "This is also a query parameter, and it is required")
    def on_get(self, req, res, thing_id):
        res.body = '{"hello": "world"}'

    @title("Update a full thing")
    @description("""
I have quite a long description and it contains <b>HTML</b>. <i>Oh wow.</i> <code>Oh geez.</code>

Words.

Words.

Words.

<pre>Code block. Indentation can get a
    little
        goofy
            here.
</pre>

Words.
    """)
    @example(request = {
                "name": "Bojangles"
            }, response = {
                "hello": "world"
            })
    def on_put(self, req, res, thing_id):
        res.body = '{"hello": "world"}'
    
    @title("Patch a thing")
    @description("I also have a description")
    def on_patch(self, req, res, thing_id):
        res.body = '{"hello": "world"}'

    @title("Delete a thing")
    @returns_status(200, "If all goes well")
    @returns_status(404, "If the thing didn't exist")
    @returns_status(418, "If I'm a teapot")
    @example(request = "requests can be strings, yo")
    def on_delete(self, req, res, thing_id):
        res.body = '{"hello": "world"}'

@secret
class ThirdResource:
    def on_get(self, req, res):
        res.body = "{}"

cirdan.inject()

app = falcon.API()
app.add_route("/hello", FirstResource())
app.add_route("/things/{thing_id}", SecondResource())
app.add_route("/hidden", ThirdResource())

cirdan.set_meta(app, name = "Cirdan Demo", intro_text = "This is intro text that could be longer if you wanted.")

cirdan.registry.dump(app)

simple_server.make_server("0.0.0.0", int(os.getenv("PORT", "8080")), app).serve_forever()
