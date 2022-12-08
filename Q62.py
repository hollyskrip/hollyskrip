class Ambulance:

myAmbulance = Ambulance()
myAmbulance.priority=priority
myAmbulance.speed=speed
myAmbulance.capacity=capacity

controlled_velocity= -10(1-priority)+2.37((speed/10)^3.98)+30(capacity+1.2)

print(controlled_velocity)
