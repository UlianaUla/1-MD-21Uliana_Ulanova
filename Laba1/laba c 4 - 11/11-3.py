class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,rating_poll):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.rating_poll=rating_poll
    def describe_restaurant(self):
        print("Название ресторана - ",self.restaurant_name, "Тип кухни - ",self.cuisine_type, "Рейтинг заведения - ", self.rating_poll)
    def rating_new(self,new_rating):
        self.rating_poll=new_rating
    def open_restaurant(self):
        print("Ресторан открыт")
newRestaurant=Restaurant("Wowowo", "Английская",3,5)
newRestaurant.rating_new(4)
newRestaurant.describe_restaurant()
