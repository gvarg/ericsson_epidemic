"""
Ericsson Programozó Bajnokság - 1. forduló

Team - tetszikabarcode
Stallenberger József
Szilágyi Lajos
Varga Gábor
"""

def get_parameters(input_message):
    v_input_list = input_message.split(" ")
    if v_input_list[0] == "START":
        print("startol")
        return v_input_list
    elif v_input_list[0] == "FACTORS":
        print("faktoriális")
        return v_input_list
    elif v_input_list[0] == "FIELDS":
        print("fieldek")
        return v_input_list
    else:
        print("Wrong input")
        quit()

def calc_factor(factor):
    factor = factor * 48271 % 2147483647

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


def main():
    for i in range(0,2):
        input_message = input("Waiting for server message:")
        v_input_list = get_parameters(input_message)
        if v_input_list != "ERROR":
            print(v_input_list)




if __name__ == '__main__':
    main()