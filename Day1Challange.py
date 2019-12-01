#open file
#read contents of file
#for each module calculate sum
#keep track of total sum
import math

input_file = open("/Users/guy_steinberg/Dropbox/AdventOfCode/Day1_Challange1_Input.txt","r")

###calculate mass of given module
def calc_fuel_for_mass(module):
    return int(math.floor(module / 3) - 2)

def total_fuel_for_mass(module):
    '''
            Params: module - mass to calculate fuel for
            Returns: total fuel required for that mass, inc each fuel required for all the fuels (recursively)
    '''
    #print("Module: {0}".format(module))
    current_fuel = int(math.floor(module / 3) - 2)
    if (current_fuel <= 0):
        return 0

    return current_fuel + total_fuel_for_mass(current_fuel)

# def total_fuel_part1(input_file):
#     total_sum = 0
#     for line in input_file:
#         mass = int(line)
#         total_sum += calc_fuel_for_mass(mass)
#     return total_sum

def total_fuel_part2(input_file):
    total_sum = 0
    for module in input_file:
        mass = int(module)
        val = total_fuel_for_mass(mass)
        #print("fuel for module {0} = {1}".format(mass, val))
        total_sum += val

    return total_sum

#print 'Part 1 Total Fuel: {0}'.format(total_fuel_part1(input_file))

print 'Part 2 Total Fuel: {0}'.format(total_fuel_part2(input_file))

#Debugging
# mass = 1969
# val = total_fuel_for_mass(mass)
# print("fuel for module {0} = {1}".format(mass, val))
# mass = 100756
# val = total_fuel_for_mass(mass)
# print("fuel for module {0} = {1}".format(mass, val))
# print 'mass of 12: {0}'.format(calc_fuel_for_mass(12))
# print 'mass of 14: {0}'.format(calc_fuel_for_mass(14))
# print 'mass of 1969: {0}'.format(calc_fuel_for_mass(1969))
# print 'mass of 100756: {0}'.format(calc_fuel_for_mass(100756))
