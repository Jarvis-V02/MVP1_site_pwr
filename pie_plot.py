import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np


def plot_pie(x, y):
    label = ['Power produced', 'Remaining Power']
    data = [x, y]
    colors = ( "Green", "Grey")
    fig = plt.figure(figsize =(5, 5))
    plt.pie(data, labels = label, startangle = 90, counterclock=False, autopct='%1.2f%%', color = color)  #starts at 12'O clock, rotates in cloclwise direction and shows percentage with 2 digit precision
    plt.show()

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

x = [4, 16, 28, 35]
y = [40, 34, 18, 16]        # operational limits of turbine 1

l = [6, 18, 30, 40]
m = [44, 40, 30, 10]        # operational limits of turbine 2

# cumulative sum of power
res1 = calc_cover_area(turb, wind, power, x, y)
res2 = calc_cover_area(turb, wind, power, l, m)

#send the power params to plot pie chart
plot_pie(res1, site_pwr-res1)         

#res1 variable is the power calculated for AS 1
#calc_cover_area function can also be called within the plot_pie() data initialization part... please send required arguments/globalize those arguments to nest the functions
