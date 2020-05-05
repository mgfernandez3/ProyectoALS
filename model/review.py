# Review sobre un libro, pelicula, videojuego...
from google.appengine.ext import ndb

from webapp2_extras.users import users


class Review(ndb.Model):
    # usuario = ndb.KeyProperty(kind=users.User)
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    tipo = ndb.StringProperty(required=True, choices=["Pelicula", "Serie", "Libro", "Videojuego"])
    titulo = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)
    nota = ndb.FloatProperty(required=True)
    comentario = ndb.StringProperty()
