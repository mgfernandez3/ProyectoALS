# coding: utf-8
# Nueva review
import time

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.review import Review


class NuevaReviewHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nueva_review.html", **valores_plantilla))

    def post(self):
        tipo = self.request.get("edTipo", "")
        titulo = self.request.get("edTitulo", "")
        autor = self.request.get("edAutor", "")
        str_nota = self.request.get("edNota", "")
        comentario = self.request.get("edComentario", "")

        try:
            nota = int(str_nota)
        except ValueError:
            nota = -1

        if not tipo or not titulo or not autor or nota < 0:
            return self.redirect("/")
        else:
            usuario = users.get_current_user()
            review = Review(
                usuario_email=usuario.email(),
                usuario_nombre=usuario.nickname(),
                tipo=tipo,
                titulo=titulo,
                autor=autor,
                nota=nota,
                comentario=comentario)
            review.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/reviews/nueva', NuevaReviewHandler)
], debug=True)