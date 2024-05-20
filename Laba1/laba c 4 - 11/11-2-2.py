class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Название ресторана -", self.restaurant_name, "Тип кухни -", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")

class Restauranto:
    def __init__(self, restauranto_name, cuisine_type):
        self.restauranto_name=restauranto_name
        self.cuisine_type=cuisine_type
    def describe_restauranto(self):
        print("Название ресторана -", self.restauranto_name, "Тип кухни -", self.cuisine_type)
    def open_restauranto(self):
        print("Ресторан открыт")

class Restaro:
    def __init__(self, restaro_name, cuisine_type):
        self.restaro_name=restaro_name
        self.cuisine_type=cuisine_type
    def describe_restaro(self):
        print("Название ресторана -", self.restaro_name, "Тип кухни -", self.cuisine_type)
    def open_restaro(self):
        print("Ресторан открыт")


newRestaurant = Restaurant("Берёзка", "Русская")
newRestaurant1 = Restauranto("Mom", "Итальянская")
newRestaurant2 = Restaro("La la", "Французская")

newRestaurant.describe_restaurant()
newRestaurant1.describe_restauranto()
newRestaurant2.describe_restaro()
