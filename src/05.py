from utils.api import get_input
import numpy as np
import re

input_str = get_input(5)
input_str_trivial = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

def execute_first(input_str):
	towers,instructions = input_str.replace("    ", "[_]").replace(" ", "").replace("[","").replace("]","").split("\n\n")
	towers = np.array([[*i] for i in towers.split("\n")][:-1])
	towers = [[j for j in i if j!='_']for i in towers.T]

	instructions = [ list(map(int, re.findall(r'\d+', line))) for line in instructions.split("\n")]

	for instr in instructions:
		for i in range(instr[0]):
			towers[instr[2]-1].insert(0,towers[instr[1]-1].pop(0))

	return ''.join([i[0] for i in towers])

def execute_second(input_str):
	towers,instructions = input_str.replace("    ", "[_]").replace(" ", "").replace("[","").replace("]","").split("\n\n")
	towers = np.array([[*i] for i in towers.split("\n")][:-1])
	towers = [[j for j in i if j!='_']for i in towers.T]

	instructions = [ list(map(int, re.findall(r'\d+', line))) for line in instructions.split("\n")]


	for instr in instructions:
		for i in range(instr[0]-1, -1, -1):
			towers[instr[2]-1].insert(0,towers[instr[1]-1].pop(i))

	return ''.join([i[0] for i in towers])

def test_easy_input_first(input_str):
	assert execute_first(input_str) == 'CMZ'

def test_easy_input_second(input_str):
	assert execute_second(input_str) == 'MCD'

if __name__ == '__main__':
	test_easy_input_first(input_str_trivial)
	test_easy_input_second(input_str_trivial)

	print(execute_first(input_str))
	print(execute_second(input_str))