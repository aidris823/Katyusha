import math

filename = "flag.ppm"
file = open(filename,'w')
file.write('P3 \n 500 500 \n 255 \n')
for i in range(500):
    for j in range(500):
        file.write('255 0 0 ') #Red 
