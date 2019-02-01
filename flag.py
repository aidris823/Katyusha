import math

filename = "flag.ppm"
file = open(filename,'w')
file.write('P3 \n 500 500 \n 255 \n')


#AGH I can't get a 2D List with all the yellow coordinates I want =(

for i in range(500):
    for j in range(500):
        file.write('255 {} {} '.format((i * j ) % 256,(i*j)%256)) #Red 
#By now, we have a reddish banner.
