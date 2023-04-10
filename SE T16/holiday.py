# Inputs as requested
city_flight = input('Which city you flying to? (Options; London, Manchester and York): ')
num_nights = input('How many nights will you be staying: ')
rental_days = input('How many days will you be needing a hired car: ')

# Hotel cost function
def hotel_cost(input):
    if(int(input)):
        return int(input)*1
    else:
        return ''

# Plane cost function
def plane_cost(input):
    if input.lower() == 'london':
        return 100
    elif input.lower() == 'manchester':
        return 101
    elif input.lower() == 'york':
        return 102
    else:
        return 0

# Car rental cost function
def car_rental(input):
    if(int(input)):
        return int(input)*2
    else:
        return ''

# Total holiday cost function
def holiday_cost():
    # If check in case an incorrect inputs were used
    if(plane_cost(city_flight) != 0 and type(hotel_cost(num_nights)) is int and type(car_rental(rental_days)) is int):
        total = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
        print('Your total holiday cost is: £' + str(total))
        print('Your cost break down:')
        print('     ' + city_flight.capitalize() + ': £' + str(plane_cost(city_flight)))
        print('     ' + 'Hotel cost: £' + str(hotel_cost(num_nights)))
        print('     ' + 'Rental cost: £' + str(car_rental(rental_days)))

    else:
        print('Sorry you one of the inputs was incorrect, please try again')

holiday_cost()