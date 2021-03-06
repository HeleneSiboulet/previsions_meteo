import json
import numpy as np
from matplotlib import pyplot as plt

with open('../json/temperatureTest.json') as jsonfile :
	temperature = json.load(jsonfile)

with open('../json/humiditeTest.json') as jsonfile :
	humidite = json.load(jsonfile)


somme = 0
compt = 0

j = []
t = []
h = []

for ip in range (1,10) :
	i = 1*ip
	j.append(ip)
	somme = 0
	compt = 0
	for annee in temperature[0].keys () :
		for date in temperature[0][annee] :
			if (date - i) in temperature [0][annee] :
				temperature_aujourdhui = temperature[1][annee][temperature[0][annee].index (date) ]
				temperature_hier = temperature[1][annee][temperature[0][annee].index (date - i ) ]  
				somme += (temperature_aujourdhui - temperature_hier) ** 2
				compt += 1
	t.append ((somme/compt)**(1/2))

	somme = 0
	compt = 0
	for annee in humidite[0].keys () :
		for date in humidite[0][annee] :
			if (date - i) in humidite [0][annee] :
				humidite_aujourdhui = humidite[1][annee][humidite[0][annee].index (date) ]
				humidite_hier = humidite[1][annee][humidite[0][annee].index (date - i ) ]
				somme += (humidite_aujourdhui - humidite_hier) ** 2
				compt += 1
	h.append ((somme/compt)**(1/2))

print ("j = " + str (j))
print ("t = " + str (t))
print ("h = " + str (h))

plt.plot(j,t)
plt.savefig("Tpersistance_EC.png")

plt.clf()
plt.plot(j,h)
plt.savefig("Hpersisance_EC.png")
