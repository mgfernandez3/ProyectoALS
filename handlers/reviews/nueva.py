# Nueva review

import webapp2
from webapp2_extras import jinja2

from model.review import Review


class NuevaReviewHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_review.html", **valores_plantilla))

    def post(self):
        pass


app = webapp2.WSGIApplication([
    ('/reviews/nueva', NuevaReviewHandler)
], debug=True)