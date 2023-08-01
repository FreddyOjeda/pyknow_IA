from pyknow import *



class ProductRecommender(KnowledgeEngine):

    brand=""
    os=""
    price=0
    capacity=0

    def input_data(self):
        print("=====================================================================================================")
        print("SISTEMA EXPERTO PARA LA RECOMENDACIÓN DE TELÉFONOS MÓVILES\n")
        print("\nIngrese sus respuestas en minúscula por favor...\n")
        brand = input("¿Qué marca prefiere? (Samsung, Apple, Xiaomi, etc.): ")
        os = input("¿Prefiere un teléfono con sistema operativo Android o iOS?: ")
        price_range_cop = float(input("Ingrese su rango de precio máximo (en pesos colombianos): "))
        storage_capacity = int(input("¿Qué capacidad de almacenamiento desea? (en GB): "))

        self.brand=brand
        self.os=os
        self.price=price_range_cop
        self.capacity=storage_capacity

        self.declare(Fact(brand=brand))
        self.declare(Fact(os=os))
        self.declare(Fact(price_range_cop=price_range_cop))
        self.declare(Fact(storage_capacity=storage_capacity))

    @Rule(Fact(brand="samsung") & Fact(os="android"))
    def recommend_high_end_samsung(self):
        print("Le recomendamos el Samsung Galaxy S21 Ultra, un teléfono de alta gama con excelentes características.")

    @Rule(Fact(brand="samsung") & Fact(os="android"))
    def recommend_mid_range_samsung(self):
        print("Le recomendamos el Samsung Galaxy A52, un teléfono de gama media con buen rendimiento.")

    @Rule(Fact(brand="apple") & Fact(os="ios"))
    def recommend_high_end_iphone(self):
        print("Le recomendamos el iPhone 13 Pro, un teléfono de alta gama con el mejor rendimiento de iOS.")

    @Rule(Fact(brand="apple") & Fact(os="ios"))
    def recommend_mid_range_iphone(self):
        print("Le recomendamos el iPhone SE (2020), un teléfono de gama media con el respaldo de iOS.")

    @Rule(Fact(brand="xiaomi") & Fact(os="android"))
    def recommend_high_end_xiaomi(self):
        print("Le recomendamos el Xiaomi Mi 11, un teléfono de alta gama con una excelente relación calidad-precio.")

    @Rule(Fact(brand="xiaomi") & Fact(os="android"))
    def recommend_mid_range_xiaomi(self):
        print("Le recomendamos el Xiaomi Redmi Note 10, un teléfono de gama media con buenas características.")

    @Rule(Fact(brand=MATCH.brand) & Fact(os=MATCH.os))
    def recommend_generic(self):
        print(f"No hay una recomendación específica para la combinación de marca '{MATCH.brand}', sistema operativo '{MATCH.os}', "
              f"rango de precio máximo de '{MATCH.price}' pesos colombianos y capacidad de almacenamiento de '{MATCH.capacity}' GB.")
        print("Le sugerimos visitar nuestra tienda para explorar otras opciones disponibles.")

if __name__ == "__main__":
    engine = ProductRecommender()
    engine.reset()
    engine.input_data()
    print("\nResultados(s) o recomendaciones: ")
    engine.run()
    print("=====================================================================================================\n")
