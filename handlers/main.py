# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from model.review import Review


class MainHandler(webapp2.RequestHandler):
    def get(self):
        reviews = Review.query().order(-Review.hora)

        valores_plantilla = {
            "reviews": reviews
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
