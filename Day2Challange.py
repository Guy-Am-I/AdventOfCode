

#open file and read its contents into an array as integers
filename = "/Users/guy_steinberg/Dropbox/AdventOfCode/Day2_input.txt"
def parse_input(filename, input_arr):
    input_file = open(filename, "r")

    for line in input_file:
        line_as_arr = line.split(',')
    for number in line_as_arr:
        input_arr.append(int(number))

#debugging
#input_arr = [1,9,10,3,2,3,11,0,99,30,40,50]
#input_arr = [1,1,1,4,99,5,6,0,99]


#helper funciton for computing values
def perform_operation(arr, opcode_index, func):
    #'func is either add or mult'
    try:
        pos1 = arr[opcode_index+1]
        pos2 = arr[opcode_index+2]
        pos3 = arr[opcode_index+3]
        if func == 'add':
            arr[pos3] = arr[pos1] + arr[pos2]
        else:
            arr[pos3] = arr[pos1] * arr[pos2]

        #print(input_arr)
    except:
        print("error")

#keep track of index for the opcode
#opcode_index = 0
def part1_solution(arr) :

    for opcode_index in range(0,len(arr),4):
        if arr[opcode_index] == 1:
            #add nums at positions 1 & 2, store result in pos3
            perform_operation(arr, opcode_index, 'add')
        elif arr[opcode_index] == 2:
            perform_operation(arr, opcode_index, 'mult')
        elif arr[opcode_index] == 99:
            #halt program
            break
        else:
            print('error: invalid opcode')

#replace pos 1 & 2 values as indicated by challange
# part1_arr = []
# parse_input(filename, part1_arr)
# part1_arr[1] = 12
# part1_arr[2] = 2
# print(input_arr)

def part2_solution(arr):
    #inefficient and simple way, but it works for now (also are numbers are only
    # in range of 0-99 -> O(100^2*len(array)) worst case
    for noun in range(0,99):
        for verb in range(0,99):
            #reset input
            arr = []
            parse_input(filename, arr)
            print(noun, verb)
            arr[1] = noun
            arr[2] = verb
    
            if(arr[0] == 19690720):
                return (noun, verb)

part2_arr = []
# parse_input(filename, part2_arr)
print(part2_solution(part2_arr))
print(100*25+5)
