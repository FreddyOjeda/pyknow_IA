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
            producto=PRODUCTO_A,
            cantidad_recomendada=10
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_B,
            cantidad_recomendada=20
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_C,
            cantidad_recomendada=5
        ))

    @Rule(AND(
        Producto(stock=P(lambda stock: stock >= 5)),
        Producto(stock=P(lambda stock: stock < 15))
    ))
    def regla_comprar_moderados(self):
        self.declare(Recomendacion(
            producto=PRODUCTO_A,
            cantidad_recomendada=20
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_B,
            cantidad_recomendada=30
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_C,
            cantidad_recomendada=15
        ))

    @Rule(Producto(stock=P(lambda stock: stock >= 15)))
    def regla_comprar_suficientes(self):
        self.declare(Recomendacion(
            producto=PRODUCTO_A,
            cantidad_recomendada=50
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_B,
            cantidad_recomendada=100
        ))
        self.declare(Recomendacion(
            producto=PRODUCTO_C,
            cantidad_recomendada=30
        ))

    @Rule(AS.recomendacion << Recomendacion())
    def mostrar_recomendacion(self, recomendacion):
        print(f"Se recomienda comprar {recomendacion['cantidad_recomendada']} unidades de {recomendacion['producto']}.")

# Función principal para ejecutar el sistema experto
def ejecutar_sistema_experto_inventario():
    engine = SistemaExpertoInventario()

    # Agregar información sobre el inventario de productos
    PRODUCTO_A = input("Ingrese el nombre del Producto A: ")
    PRODUCTO_B = input("Ingrese el nombre del Producto B: ")
    PRODUCTO_C = input("Ingrese el nombre del Producto C: ")
    stock_A = int(input(f"Ingrese el stock actual de {PRODUCTO_A}: "))
    stock_B = int(input(f"Ingrese el stock actual de {PRODUCTO_B}: "))
    stock_C = int(input(f"Ingrese el stock actual de {PRODUCTO_C}: "))
    
    engine.reset()
    engine.declare(Producto(producto=PRODUCTO_A, stock=stock_A))
    engine.declare(Producto(producto=PRODUCTO_B, stock=stock_B))
    engine.declare(Producto(producto=PRODUCTO_C, stock=stock_C))

    # Ejecutar el sistema experto y obtener recomendaciones de compra
    engine.run()

if __name__ == "__main__":
    ejecutar_sistema_experto_inventario()
