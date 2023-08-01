from pyknow import *

class Producto(Fact):
    """Información sobre un producto en el inventario."""
    pass

class Recomendacion(Fact):
    """Recomendación de compra para un producto específico."""
    pass

class SistemaExpertoInventario(KnowledgeEngine):
    @Rule(Producto(stock=P(lambda stock: stock < 5)))
    def regla_comprar_pocos(self):
        self.declare(Recomendacion(
            producto="smartphone",
            cantidad_recomendada=10
        ))

    @Rule(AND(
        Producto(stock=P(lambda stock: stock >= 5)),
        Producto(stock=P(lambda stock: stock < 15))
    ))
    def regla_comprar_moderados(self):
        self.declare(Recomendacion(
            producto="tablet",
            cantidad_recomendada=20
        ))

    @Rule(Producto(stock=P(lambda stock: stock >= 15)))
    def regla_comprar_suficientes(self):
        self.declare(Recomendacion(
            producto="laptop",
            cantidad_recomendada=5
        ))

    @Rule(AS.recomendacion << Recomendacion())
    def mostrar_recomendacion(self, recomendacion):
        print(f"Se recomienda comprar {recomendacion['cantidad_recomendada']} unidades de {recomendacion['producto']}.")

# Función principal para ejecutar el sistema experto
def ejecutar_sistema_experto_inventario():
    engine = SistemaExpertoInventario()

    # Agregar información sobre el inventario de productos
    A=int(input("Ingrese el stock actual de smartphones: "))
    B=int(input("Ingrese el stock actual de Tablets: "))
    C=int(input("Ingrese el stock actual de Laptops: "))
    engine.reset()
    engine.declare(Producto(producto="smartphone", stock=A))
    engine.declare(Producto(producto="tablet", stock=B))
    engine.declare(Producto(producto="laptop", stock=C))

    # Ejecutar el sistema experto y obtener recomendaciones de compra
    engine.run()

if __name__ == "__main__":
    ejecutar_sistema_experto_inventario()
