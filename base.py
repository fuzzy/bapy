#!/usr/bin/env python2

from bottle import Bottle, run
from bottleCBV import BottleView, route


__NAME__ = "{{metadata.name}}"
__VERS__ = "{{metadata.vers}}"

app = Bottle()

{% for route in routes %}
class {{route.name[0].upper()}}{{route.name[1:]}}View(BottleView):

    def index(self):
        return "{{route.name[0].upper()}}{{route.name[1:]}}View.index()"
    {% if 'get' in route.methods %}
    def get(self, item_key):
        return "GET {{route.name[0].upper()}}{{route.name[1:]}}View.get({0})".format(item_key){% endif %}
    {% if 'post' in route.methods %}
    def post(self):
        return "POST {{route.name[0].upper()}}{{route.name[1:]}}View.post()"{% endif %}
    {% if 'put' in route.methods %}
    def put(self, item_key):
        return "PUT {{route.name[0].upper()}}{{route.name[1:]}}View.put({0})".format(item_key){% endif %}
    {% if 'custom' in route.keys() %}
    {% for croute in route.custom.routes %}
    @route("{{croute.path}}", method={{croute.methods}})
    def {{croute.name}}(self):
        return "Custom route"{% endfor %}{% endif %}
{% endfor %}
    
{% for route in routes %}
# Setup routes for {{route.name}}
{{route.name[0].upper()}}{{route.name[1:]}}View.register(app)
{% endfor %}
# Run the app
app.run(port=8080)

