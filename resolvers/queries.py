import graphene
from db.data import products_db
from models.product import Producto

class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(self, info):
        return products_db