# coding: utf-8

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.review import Review


class MainHandler(webapp2.RequestHandler):
    def get(self):
        usuario = users.get_current_user()

        valores_plantilla = {}
        if usuario:
            reviews = Review.query().order(-Review.hora)

            valores_plantilla = {
                "usuario": usuario,
                "reviews": reviews,
                "url_usuario": users.create_logout_url("/")
            }

        else:
            valores_plantilla = {
                "url_usuario": users.create_login_url("/")
            }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("index.html", **valores_plantilla))




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
