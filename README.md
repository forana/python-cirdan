# Cirdan

[![Build Status](https://travis-ci.org/forana/python-cirdan.svg?branch=master)](https://travis-ci.org/forana/python-cirdan)

Decorator-based documentation generation for Falcon web applications. Named after [Círdan the Shipwright](http://lotr.wikia.com/wiki/C%C3%ADrdan). Supports Python 2.7 and 3.4.

This was built with the thought in mind that every step of documenting your API should be easy. There exist a number of solutions (such as [Sphinx](http://sphinx-doc.org/)) that can generate HTML docs from docstrings in your code, but that means you still have to host those somewhere. Cirdan serves your API's documentation from the API server itself, meaning that **your docs and code are always in sync.**

## Installation

```
pip install cirdan
```

[Docs for Cirdan can be found here.](./docs.md)

## Quick Example

```python
import cirdan
import falcon
from cirdan.decorators import title, description
from wsgiref import simple_server

@title("It's a resource")
@description("It does a thing.")
class SomeResource:
    @title("Get Greeted")
    @description("This route says hello.")
    def on_get(self, request, response):
        response.body = "Hello"

# Important that this comes before your app is initialized
cirdan.inject()

app = falcon.API()
app.add_route("/something", SomeResource())

simple_server.make_server("localhost", 8080, app).serve_forever()
```

Run that, then navigate to [http://localhost:8080/docs](http://localhost:8080/docs) in your browser. It's that simple - Cirdan is automatically bound, and knows about all of your routes. See [demo.py](./demo.py) for a more extended example - a running version of the docs it generates is [available on Heroku](http://cirdan.herokuapp.com/docs).

## License

MIT
