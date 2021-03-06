import numpy as np
import json
from matplotlib import pyplot as plt



with open('../json/temperature.json') as jsonfile :
	temperature = json.load(jsonfile)


s = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
compt = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
r = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

for annee in temperature[0].keys() :
	for date in temperature[0][annee] :
		i1 = (date - int(date) )* 8
		#print (i1)
		i = int (i1)
		compt[i] += 1
		s [i] += temperature[1][annee][temperature[0][annee].index(date)]

for j in range (len (s)) :
	r[j] = (s[j] / compt[j]) - 273.15

mesure = [1,2,3,4,5,6,7,8]


f = []
g = []
h = []
for m in mesure :
	pf = -3.75735475*np.cos(2*np.pi*(m-1)/8 + 5.61376937) + 285.13810537 - 273.15
	f .append (pf)
	pg = 2.85138181e+02 + -3.77024667e+00*np.cos(2*np.pi*(m-1)/8 + 5.61243708e+00) + 6.64813028e-01 *np.cos(4*np.pi*(m-1)/8 + 6.19368036e+00) - 273.15
	g .append (pg) 
	ph = 2.85138253e+02 + -3.77025815e+00*np.cos(2*np.pi*(m-1)/8 + 5.61243713e+00 ) + 6.64829296e-01 *np.cos(4*np.pi*(m-1)/8 + 6.19366499e+00) + 8.58689428e-02 *np.cos(4*np.pi*(m-1)/8 + 6.27803532e+00) - 273.15
	h.append (ph)
#print (str (r))
plt.plot (mesure, r, label = "moyenne")
plt.plot (mesure, f, label = "f")
plt.plot (mesure, g, label = "g")
plt.plot (mesure, h, label = "h")

plt.legend()
plt.savefig("moyenne_sur_la_journeeT.png")
