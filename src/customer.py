from car_rental import CarRental
class Customer:
    
    def __init__(self,name):
        print('Start of Customer:init')
        self.name = name
        print('End of Customer:init')
      
    def request_car(self,carRental, no_of_cars, rental_mode, duration):
        print('Start of Customer:request_car')
        carRental.rent_car(self.name, no_of_cars, rental_mode, duration)
        print('End of Customer:request_car')
        
    def return_car(self,carRental, no_of_cars, rental_mode, duration):
        print('Start of Customer:return_car')
        carRental.release_car(self.name, no_of_cars, rental_mode, duration)
        print('End of Customer:return_car')
    