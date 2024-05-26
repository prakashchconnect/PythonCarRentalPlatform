class CarRental:
    def __init__(self,total_cars):
        print('Start of CarRental:init')
        self.total_cars = total_cars
        self.available_cars = total_cars
        self.rental_rates = {
            'hourly': 10,
            'daily': 50,
            'weekly': 200
        }
        self.rented_cars = {}
        print('End of CarRental:init')
        
    def display_available_cars(self):
        print('Start of CarRental:display_available_cars')
        print(f"Available cars: {self.total_cars}")
        print('End of CarRental:display_available_cars')
    
    def rent_hourly(self, no_of_cars, duration):
        print('Start of CarRental:rent_hourly')
        bill_amount = self.rental_rates['hourly'] * duration * no_of_cars
        return bill_amount
        print('End of CarRental:rent_hourly')
        
    def rent_daily(self, no_of_cars, duration):
        print('Start of CarRental:rent_daily')
        bill_amount = self.rental_rates['daily'] * duration * no_of_cars
        
        days_in_hours = 24 * duration;
        return bill_amount
        print('End of CarRental:rent_daily')
        
    def rent_weekly(self, no_of_cars, duration):
        print('Start of CarRental:rent_weekly')
        bill_amount = self.rental_rates['weekly'] * duration * no_of_cars
        weeks_in_hours = 7 * 24 * duration
        return bill_amount
        print('End of CarRental:rent_weekly')
    
    def rent_car(self, name, no_of_cars, rental_mode, duration):
        print('Start of CarRental:rent_car')
        bill_amount =0;
        if self.available_cars == 0 :
            print('Hello ', name,' No available cars as of now. Please try again after some time',)
            
        elif self.available_cars < no_of_cars :
            print('Hello ', name,' We dont have requested no of cars available with us')
            print('We have only ', self.available_cars,' with us. If you want you can book those')
        
        self.available_cars = self.available_cars - no_of_cars  
        print('End of CarRental:rent_car')
        
    def release_car(self,name, no_of_cars, rental_mode, duration):
        print('Start of CarRental: release_car')
        self.available_cars = self.available_cars + no_of_cars 
        
        if rental_mode == 'hourly':
            print('Rental mode selected is hourly')
            bill_amount = self.rent_hourly(no_of_cars, duration)
        elif rental_mode == 'daily':
            print('Rental mode selected is daily')
            bill_amount = self.rent_daily(no_of_cars, duration)
        elif rental_mode == 'weekly':
            print('Rental mode selected is weekly')
            bill_amount = self.rent_weekly(no_of_cars, duration)
        else:
            print('Wrong Rental Mode. Please select only hourly, daily or weekly')
        
        print('Hello ', name, ' , your bill amount = ', bill_amount)
        print('Start of CarRental: release_car')
        
    