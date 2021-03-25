d = {}

file = open('input.txt', 'r')

for line in file: 
    coor = line.split()
    key, x, y = coor[0], coor[2], coor[1] 
    d[key] = (x,y) 

del d['Station']

print(d)

