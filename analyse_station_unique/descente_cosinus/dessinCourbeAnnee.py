import numpy as np
import json
from matplotlib import pyplot as plt



import json
from matplotlib import pyplot as plt

with open('../json/temperature.json') as jsonfile :
	temperature = json.load(jsonfile)


Moyenne_temperature = []
dates = set()

for annee in temperature[0].keys() :
	for date in temperature[0][annee] :
		dates.add(int (date))
dates = list(dates)
dates.sort()

for date in dates :
	i = 0
	somme_temperature = 0
	for annee in temperature[0].keys() :
		for heure in range (8):
			if (date + (1/8) * heure) in temperature[0][annee]:
				index = temperature[0][annee].index(date + (1/8) * heure)
				i += 1
				somme_temperature += temperature[1][annee][index]
	Moyenne_temperature.append(somme_temperature/i - 273.15)



jour = range (366)
f = []
g = []
h = []
for j in jour :
	pf = -8.37900126*np.cos(2*np.pi*j/365 + 5.95629115) + 285.13810537 - 273.15
	f .append (pf)
	pg = 2.85138181e+02 -8.39742026e+00*np.cos(2*np.pi*j/365 + 5.95627061e+00) -3.56389400e-02 *np.cos(4*np.pi*j/365 + 6.61334074e-03) - 273.15
	g .append (pg) 
	ph = 2.85138253e+02 -8.39738900e+00*np.cos(2*np.pi*j/365 + 5.95626734e+00 ) -3.55282083e-02 *np.cos(4*np.pi*j/365 + 6.59654426e-03) -7.80736324e-02*np.cos(4*np.pi*j/365 + 6.27876991e+00) - 273.15
	h.append (ph)

plt.plot(dates, Moyenne_temperature, label = "moyenne")
plt.plot (jour, f, label = "f")
plt.plot (jour, g, label = "g")
plt.plot (jour, h, label = "h")
plt.legend()
plt.savefig("CourbeAnneeT.png")

