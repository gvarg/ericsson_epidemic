"""
Ericsson Programozó Bajnokság - 1. forduló

Team - tetszikabarcode
Stallenberger József
Szilágyi Lajos
Varga Gábor
"""

import sys

v_game_id = 0
v_max_tick = 0
v_country_count = 0
v_row = 0
v_columns = 0
v_factor_1 = 0
v_factor_2 = 0
v_factor_3 = 0
v_factor_4 = 0



def get_parameters(input_message):

    global v_game_id
    global v_max_tick
    global v_country_count

    global v_row
    global v_columns

    global v_factor_1
    global v_factor_2
    global v_factor_3
    global v_factor_4

    v_input_list = input_message.split(" ")

    print(v_input_list)


    if v_input_list[0] == "START":
        v_game_id = v_input_list[1]
        v_max_tick = v_input_list[2]
        v_country_count = v_input_list[3]
        print(v_game_id)
    elif v_input_list[0] == "FACTORS":
        v_factor_1 = v_input_list[1]
        v_factor_2 = v_input_list[2]
        v_factor_3 = v_input_list[3]
        v_factor_4 = v_input_list[4]
    elif v_input_list[0] == "FIELDS":
        v_row = v_input_list[1]
        v_columns = v_input_list[2]
    elif v_input_list[0] == "FD":
        return

def calc_factor(factor):
    factor = factor * 48271 % 2147483647
"""
def healing(curr_tick, coord):
    #Clean the coordinates string
    v_coordinates = coord.replace("(","")
    v_coordinates = v_coordinates.replace(")","")
    v_coordinates_list = v_coordinates.split(",")
    v_height = v_coordinates_list[0]
    v_width = v_coordinates_list[1]

    if v_width + v_height < curr_tick:
        return floor(min(i = [1 .. width + height], tick_info[curr_tick - i, coord].infection_rate) * (factor1() % 10) / 20.0) #TODO: translate it to python
    else
        return 0

def infection(curr_tick, coord):
    return ceil(
        (avg(i = [1 .. mini(factor2() % 10 + 10, curr_tick)], 
        infection(curr_tick - i, coord)) + sum(c = {coord, neighbours(coord)}; 
                                                t = factor3() % 7 + 3, 
                                                if tick_info[curr_tick-1, c].infection_rate > (if start_info[coord].district != start_info[c].district : 
                                                                                                    2 
                                                                                                elif coord != c:
                                                                                                    1 
                                                                                                else: 0) * t:
                                                    clamp(start_info[coord].population - start_info[c].population, 0, 2) + 1 
                                                else: 
                                                    0
                                                )
        ) * (factor4() % 25 + 50) / 100.0
       ) #TODO: translate it to python
"""

def get_input():

    global v_game_id
    global v_max_tick
    global v_country_count

    global v_row
    global v_columns

    global v_factor_1
    global v_factor_2
    global v_factor_3
    global v_factor_4

    v_input_file = open("./input/input.txt", "r")

    for line in v_input_file:
        line = line.strip("\n")
        get_parameters(line)

    print(v_game_id)
    print(v_max_tick)
    print(v_country_count)
    print(v_row)
    print(v_columns)
    print(v_factor_1)
    print(v_factor_2)
    print(v_factor_3)
    print(v_factor_4)



def main():
    global v_game_id

    get_input()



if __name__ == '__main__':
    main()