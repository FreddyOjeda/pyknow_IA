from pyknow import *

class ProductRecommender(KnowledgeEngine):

    brand=""
    os=""
    price=0
    capacity=0
    camera=""
    screen_size=""

    def input_data(self):
        print("=====================================================================================================")
        print("SISTEMA EXPERTO PARA LA RECOMENDACIÓN DE TELÉFONOS MÓVILES\n")
        print("\nIngrese sus respuestas en minúscula por favor...\n")
        brand = input("¿Qué marca prefiere? (Samsung, Apple, Xiaomi, etc.): ")
        os = input("¿Prefiere un teléfono con sistema operativo Android o iOS?: ")
        price_range_cop = float(input("Ingrese su rango de precio máximo (en pesos colombianos): "))
        storage_capacity = int(input("¿Qué capacidad de almacenamiento desea? (en GB): "))
        camera = input("¿Qué calidad de cámara prefiere? (alta, media, básica): ")
        screen_size = float(input("¿Qué tamaño de pantalla prefiere? (en pulgadas): "))

        self.brand=brand
        self.os=os
        self.price=price_range_cop
        self.capacity=storage_capacity
        self.camera=camera
        self.screen_size=screen_size

        self.declare(Fact(brand=brand))
        self.declare(Fact(os=os))
        self.declare(Fact(price_range_cop=price_range_cop))
        self.declare(Fact(storage_capacity=storage_capacity))
        self.declare(Fact(camera=camera))
        self.declare(Fact(screen_size=screen_size))

    @Rule(Fact(brand="samsung") & Fact(os="android") & Fact(camera="alta") & Fact(screen_size=MATCH.screen_size))
    def recommend_high_end_samsung(self, screen_size):
        print(f"Le recomendamos el Samsung Galaxy S21 Ultra, un teléfono de alta gama con una excelente cámara, "
              f"pantalla de {screen_size} pulgadas y características destacadas.")

    @Rule(Fact(brand="samsung") & Fact(os="android") & Fact(camera="media") & Fact(screen_size=MATCH.screen_size))
    def recommend_mid_range_samsung(self, screen_size):
        print(f"Le recomendamos el Samsung Galaxy A52, un teléfono de gama media con una cámara aceptable y "
              f"pantalla de {screen_size} pulgadas.")

    # Agregar más reglas para otros modelos y marcas según las preferencias del usuario.

    @Rule(Fact(brand=MATCH.brand) & Fact(os=MATCH.os) & Fact(camera=MATCH.camera) & Fact(screen_size=MATCH.screen_size))
    def recommend_generic(self, brand, os, camera, screen_size):
        print(f"No hay una recomendación específica para la combinación de marca '{brand}', sistema operativo '{os}', "
              f"cámara '{camera}', pantalla de '{screen_size}' pulgadas, rango de precio máximo de '{self.price}' pesos colombianos y capacidad de almacenamiento de '{self.capacity}' GB.")
        print("Le sugerimos visitar nuestra tienda para explorar otras opciones disponibles.")

if __name__ == "__main__":
    engine = ProductRecommender()
    engine.reset()
    engine.input_data()
    print("\nResultados(s) o recomendaciones: ")
    engine.run()
    print("=====================================================================================================\n")
