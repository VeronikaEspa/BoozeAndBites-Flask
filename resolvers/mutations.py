import graphene
from db.data import products_db
from models.product import Producto

class ModificarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(lambda: Producto)

    def mutate(self, info, id, cantidad):
        for producto in products_db:
            if producto["id"] == id:
                producto["stock"] += cantidad

                # Lógica para disponibilidad
                if producto["stock"] <= 0:
                    producto["stock"] = 0
                    producto["disponible"] = False
                else:
                    producto["disponible"] = True

                return ModificarStock(producto=producto)

        raise Exception("Producto no encontrado")

class ProductoCompraInput(graphene.InputObjectType):
    id = graphene.Int(required=True)
    cantidad = graphene.Int(required=True)

class ComprarProductos(graphene.Mutation):
    class Arguments:
        productos = graphene.List(ProductoCompraInput, required=True)

    productos_actualizados = graphene.List(Producto)

    def mutate(self, info, productos):
        actualizados = []
        for compra in productos:
            for producto in products_db:
                if producto["id"] == compra.id:
                    producto["stock"] -= compra.cantidad
                    if producto["stock"] <= 0:
                        producto["stock"] = 0
                        producto["disponible"] = False
                    actualizados.append(producto)
                    break
        return ComprarProductos(productos_actualizados=actualizados)

class Mutation(graphene.ObjectType):
    modificar_stock = ModificarStock.Field()
    comprar_productos = ComprarProductos.Field()