# initializing variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# getting vacant cars by substracting the drivers to the number of cars
cars_not_driven = cars - drivers
# getting the cars driven, assuming all drivers are driving the cars
cars_driven = drivers
# total capacity of all the cars being driven
carpool_capacity = cars_driven * space_in_a_car

average_passengers_per_car = passengers / cars_driven

# display the results
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

