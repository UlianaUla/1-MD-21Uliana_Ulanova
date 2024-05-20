class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Название ресторана - ",self.restaurant_name, end='\n', "Тип кухни - ",self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")
newRestaurant=Restaurant("Wowowo", "Английская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
class Icecreamcafe(Restaurant):
    def __init__(self,restaurant_name,flavors,time,location):
        self.restaurant_name=restaurant_name
        self.flavors=flavors
        self.time=time
        self.location=location
    def __add__(self, flavors_new):
        #self.flavors=flavors_new
        self.flavors.append(flavors_new)
    def __del__(self,flavors,flavors_new):
        #self.flavors=flavors or flavors_new
    def proverka(self,flavors,flavors_new):
        if flavors_new in flavors:
            print("Мороженное данного сорта есть ")
        else:
            print("Мороженное отсутствует")
    def spisok_icecream(self):
        print("Список сортов мороженного - ", self.flavors)
newIcecreamcafe=("Мороженка",[Шоколад-Маракуйя,Ваниль-Кола,Абрикос-Ежевика])
newIcecreamcafe.spisok_icecream
