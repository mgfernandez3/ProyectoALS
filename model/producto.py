#Reseña sobre un libro, película, videojuego...
from google.appengine.ext import ndb

from webapp2_extras.users import users


class Review(ndb.Model):
    usuario = ndb.KeyProperty(kind=users.User) #Add kind usuario
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    tipo = ndb.StringProperty(required=True, choices=["Película", "Serie", "Libro", "Videojuego"])
    titulo = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)
    nota = ndb.NumberProperty(required=True)
    comentario = ndb.StringProperty()
