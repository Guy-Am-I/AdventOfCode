

#open file and read its contents into an array as integers
input_file = open("/Users/guy_steinberg/Dropbox/AdventOfCode/Day2_input.txt", "r")

input_arr = []
for line in input_file:
    line_as_arr = line.split(',')
    for number in line_as_arr:
        input_arr.append(int(number))

#replace pos 1 & 2 values as indicated by challange
input_arr[1] = 12
input_arr[2] = 2

#debugging
#input_arr = [1,9,10,3,2,3,11,0,99,30,40,50]
#input_arr = [1,1,1,4,99,5,6,0,99]


#helper funciton for computing values
def perform_operation(input_arr, opcode_index, func):
    #'func is either add or mult'
    try:
        pos1 = input_arr[opcode_index+1]
        pos2 = input_arr[opcode_index+2]
        pos3 = input_arr[opcode_index+3]
        if func == 'add':
            input_arr[pos3] = input_arr[pos1] + input_arr[pos2]
        else:
            input_arr[pos3] = input_arr[pos1] * input_arr[pos2]

        #print(input_arr)
    except:
        print("error")


#keep track of index for the opcode
#opcode_index = 0
for opcode_index in range(0,len(input_arr),4):
    if input_arr[opcode_index] == 1:
        #add nums at positions 1 & 2, store result in pos3
        perform_operation(input_arr, opcode_index, 'add')
    elif input_arr[opcode_index] == 2:
        perform_operation(input_arr, opcode_index, 'mult')
    elif input_arr[opcode_index] == 99:
        #halt program
        break
    else:
        print('error: invalid opcode')


print(input_arr)
