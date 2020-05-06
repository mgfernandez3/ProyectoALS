# coding: utf-8
# Nueva review

import webapp2
from webapp2_extras import jinja2
import time

from model.review import Review


class EliminaReviewHandler(webapp2.RequestHandler):
    def get(self):
        review = Review.recupera(self.request)
        review.key.delete()
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/reviews/elimina', EliminaReviewHandler)
], debug=True)