import random

#WARNING: This took a dumb long amount of time to compile (when I ran the time function in Terminal it took about 1 min 29 secs to be precise).  You've been warned.
filename = "swiss_flag.ppm"
file = open(filename,'w')
file.write('P3 \n 500 500 \n 255 \n')

#Returns a list containing all (x,y) coordinates from start to end.
#Prereq: start and end are lists with two integers (ex: [2,3] and [10,20])
#For now, I only know how to do straight lines so start[x] must equal end[x] XOR start[y] equals end
#[y] (not OR, XOR bc if both are true then whats the use of this function lol)
def line_draw(start,end):
    if start[0] == end[0]:
        if start[1] < end[1]:
            return horizontal_draw(start,end)
        return horizontal_draw(end,start)
    if start[0] < end[0]:
        return vertical_draw(start,end)
    return vertical_draw(end,start)

#Assumes start[1] == end[1], assumes start[0] < end[0]
def vertical_draw(start,end):
    ans = [start,end]
    x = start[0] + 1
    while x < end[0]:
        ans.append([x,start[1]])
        x+=1
    return ans
#Assumes start[0] == end[0], assumes start[1] < end[1]
def horizontal_draw(start,end):
    ans = [start,end]
    x = start[1] + 1
    while x < end[1]:
        ans.append([start[0],x])
        x+=1
    return ans
'''
#Testing functions:
start = [2,3]
end = [10,3]

print line_draw(start,end)
print line_draw(end,start)

v_start = [5,10]
v_end = [5,15]

print line_draw(v_start,v_end)
print line_draw(v_end,v_start)
'''

line = list()
for i in range(50):
   # line += line_draw([75,200+i],[375,200+i])
    line += line_draw([50+i,50],[350+i,50])
#print line
#vertical line 
for i in range(500):
    for j in range(500):
        if [i,j] not in line:
            file.write('{} {} {} '.format(random.randint(0,100),random.randint(100,200),random.randint(201,254)))
        else:
            file.write('0 0 0 ')

