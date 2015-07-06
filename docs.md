# Using Cirdan

Cirdan is tested against Python 2.7 and 3.4 via [TravisCI](https://travis-ci.org/forana/python-cirdan). It _probably_ works on some older 2.6 and 3.2/3.3 versions, but I make no guarantees.

Note that I have also done no testing as to the performance of Cirdan. It probably adds an insignificant amount of startup time. It also caches the HTML for the docs page in memory, which is especially worth noting if you're serving something huge using gunicorn.

I highly, highly recommand taking a look at [the demo file](./demo.py) for a working example of all of Cirdan.

## Installation

```
pip install cirdan
```

## Decorators

All decorator arguments are assumed to be strings unless otherwise specified.

### @title(_name_)
Sets the name of the a resource class or route method.

### @description(_text_)
Sets the descripion of a resource class or route method. This can include HTML to style as you see fit - `<code>` and `<pre>` are useful tags here.

### @param(_name_, _description_[, _required_ = False])
Notes that a route method takes in a parameter with `name` and `description`. The optional parameter `required` is a boolean that marked if this parameter must be sent.

## API Usage

I've only documented the functions that are intended to be publicly used - if you want to wade through the source, there are nasty but nifty things you could do, I'm sure.

### cirdan.inject()
Injects Cirdan into Falcon by way of a small amount of monkey-patching. This must be called before `falcon.API` is invoked!

### cirdan.route_path
Settable property that defines the route that Cirdan's docs-serving resource is bound to. Defaults to `/docs`.

### cirdan.template_path
Settable property that defines the path to the [Jinja2](http://jinja.pocoo.org/) template that Cirdan's docs-serving resource will use to turn your decorator data into HTML. Override this if you'd like to have something that looks better than my craptastic HTML. I recommend using the existing template as a reference point for what will be in the template payload.

### cirdan.cache_template
Settable boolean property (defaulting to `True`) that tells Cirdan if it should re-render the HTML template on every request or not (default behavior is only the first time). Set it to `False` for easy custom template debugging.

### cirdan.set_meta(_api_, _name_ = "", _intro_text_ = "", _**kwargs_)

Settable properties that are passed through to the rendered template. `name` and `intro_text` are given defaults - these are used as the page title, main header, and intro text paragraph in the default template.

### cirdan.registry.dump()

Dumps the bound resources and their routes to standard out. I like to do this before letting the server start (as seen in `demo.py`). Just sort of nifty.

## Bugs / Issues / etc

Open issues on github.
