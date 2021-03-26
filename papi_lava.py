import math

def parsefile(input_file):
    d = {}
    file = open(input_file, 'r')

    for line in file: 
        coor = line.split()
        key, x, y = coor[0], coor[2], coor[1] 
        d[key] = (x,y) 

    del d['Station']

    return d 


def compute(input_dict):
    out_dict = {}
    counter = 1
    n_points = len(input_dict)
    while counter <= n_points:
        first_point = counter
        second_point = (counter+1) 
        if second_point > n_points:
            second_point = (counter + 1)%n_points
        f_x_coor = float(input_dict[str(first_point)][0])
        f_y_coor = float(input_dict[str(first_point)][1])
        s_x_coor = float(input_dict[str(second_point)][0])
        s_y_coor = float(input_dict[str(second_point)][1])
        distance = math.sqrt((f_x_coor - s_x_coor)**2 + (f_y_coor - s_y_coor)**2)
        out_dict[f"{first_point}-{second_point}"] = distance 
        counter = counter + 1
    return out_dict 

print(compute(parsefile('input.txt')))