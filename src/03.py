from utils.api import get_input
from sortedcontainers import SortedSet
import numpy as np

input_str = get_input(3)
input_str_trivial = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def execute_first(input_str):
	score = 0
	for backpack in input_str.split("\n"):
		size = len(backpack)
		comp1,comp2 = SortedSet(backpack[:int(size/2)]), SortedSet(backpack[int(size/2):])
		item = comp1.intersection(comp2)[0]
		score+=priority.index(item)+1
	return score

def execute_second(input_str):
	score=0
	allbackpack=np.array(input_str.split("\n"))
	groups =  np.reshape(allbackpack, (int(len(allbackpack)/3), 3))
	for group in groups:
		a,b,c = [SortedSet(i) for i in group]
		item = a.intersection(b).intersection(c)[0]
		score+=priority.index(item)+1
	return score

def test_easy_input_first(input_str):
   assert execute_first(input_str) == 157

def test_easy_input_second(input_str):
   assert execute_second(input_str) == 70

if __name__ == '__main__':
	test_easy_input_first(input_str_trivial)
	test_easy_input_second(input_str_trivial)

	print(execute_first(input_str))
	print(execute_second(input_str))