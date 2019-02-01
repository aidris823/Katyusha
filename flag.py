import math

filename = "flag.ppm"
file = open(filename,'w')
file.write('P3 \n 500 500 \n 255 \n')
#Declare a 500x2 2D List
comrade_list = list()
rows = 500
cols = 2
for i in range(rows):
    comrade_list += [[0]*cols]
#Yellow is [255 255 0] before I forget...

x = 100


#AGH I can't get a 2D List with all the yellow coordinates I want =(

for i in range(500):
    for j in range(500):
        file.write('255 {} {} '.format((i * j ) % 256,(i*j)%256)) #Red 
#By now, we have a reddish banner.

x = 100
y = 100
