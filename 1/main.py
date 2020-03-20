import random
def a(x,y):
    return str(random.random()*x-x*1.0/2+y)

#  wind	REAL
#  rain 	REAL
#  temp		REAL
#  air-pollution	REAL
#  cloud-coverage	REAL
#  humidity 	REAL
#  seismic-activity		REAL
#  cisnienie	REAL
print('@RELATION cities_weather')
print('@ATTRIBUTE wind	REAL')
print('@ATTRIBUTE rain 	REAL')
print('@ATTRIBUTE temp		REAL')
print('@ATTRIBUTE air-pollution	REAL')
print('@ATTRIBUTE cloud-coverage	REAL')
print('@ATTRIBUTE humidity 	REAL')
print('@ATTRIBUTE seismic-activity		REAL')
print('@ATTRIBUTE cisnienie	REAL')
print('@ATTRIBUTE class 	{Krakow,Warszawa,Katowice,Kielce,Elk}')
for i in range(6):
    print(','.join([a(1,1),a(2,2),a(6,30),a(50,300),a(50,50),a(50,10),a(0.01,0.005),a(20,1000),"Krakow"]))
for i in range(6):
    print(','.join([a(1,1), a(2,2),a(6,30), a(30,100), a(50,50), a(50,10), a(0.01,0.005), a(20,1000), "Warszawa"]))
for i in range(6):
    print(','.join([a(1,1),a(2,2),a(6,30),a(45, 150),a(50,50),a(50,10),a(0.5,1),a(20,1000),"Katowice"]))
for i in range(6):
    print(','.join([a(5,5),a(2,2),a(6,30),a(30,100),a(50,50),a(50,10),a(0.01,0.005),a(20,1000),"Kielce"]))
for i in range(6):
    print(','.join([a(2,2),a(2,2),a(6,25),a(20,50),a(50,50),a(60,10),a(0.01,0.005),a(20,1000),"Elk"]))