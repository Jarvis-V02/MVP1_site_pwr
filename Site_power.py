import matplotlib.pyplot as plt
import random
import numpy as np


def calc_cover_area(TI, WS, PWR, AS_X, AS_Y):
    x_max = max(AS_X)
    y_max = max(AS_Y)
    calc_sum = 0
    for i in range(0, len(TI)):
        if(TI[i] <= y_max) & (TI[i] <= x_max):
            y_int = np.interp(TI[i], AS_X, AS_Y)
            if y_int >= WS[i]:
                calc_sum = calc_sum + PWR[i]
    return calc_sum


turb = random.sample(range(10, 40), 15)     # feed 15 random turbulence intensity data
wind = random.sample(range(5, 40), 15)     # feed 15 random wind speed list
power = random.sample(range(100, 1000), 15)     # feed 15 random power list
site_pwr = np.sum(power)

plt.figure(figsize=(5,5))    # define plot area size
space = plt.axes()
space.scatter(turb, wind)       # site data in scatter plot

x = [4, 16, 28, 35]
y = [40, 34, 18, 16]        # operational limits of turbine 1

l = [6, 18, 30, 40]
m = [44, 40, 30, 10]        # operational limits of turbine 2

space.plot(x,y)
space.plot(l,m)

space.set_xlabel('TI')
space.set_ylabel('WS')

plt.show()

# cumulative sum of power
res1 = calc_cover_area(turb, wind, power, x, y)
res2 = calc_cover_area(turb, wind, power, l, m)

print("Power= "+str(res1)+" MW || % Site Compatibility= "+str((res1/site_pwr)*100))     # power calc for turbine 1
print("Power= "+str(res2)+" MW || % Site Compatibility= "+str((res2/site_pwr)*100))     # power calc for turbine 2
