from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Raider, Driver
from vehicle import Car, Bike

niy_jao = RideSharing("Nia Jao")
rahim = Raider("Rahim", "rahim@gmail.com", "123456789", "Mohakhali", "1200")
niy_jao.add_rider(rahim)
karim = Driver("Karim", "karim@gmail.com", "987654321", "Gulsan")
niy_jao.add_driver(karim)
rahim.request_ride(niy_jao, "uttara", "car")
rahim.show_current_ride()
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
print(niy_jao)
