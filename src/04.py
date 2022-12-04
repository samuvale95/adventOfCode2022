from utils.api import get_input
from sortedcontainers import SortedSet

input_str = get_input(4)
input_str_trivial = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def execute_first(input_str):
	count=0
	for line in input_str.split("\n"):
		first,second = line.split(",")
		first  = first.split('-')
		second = second.split('-')

		if((int(first[0])>=int(second[0]) and int(first[1])<=int(second[1])) or (int(second[0])>=int(first[0]) and int(second[1])<=int(first[1]))):
			count+=1
	return count

def execute_second(input_str):
	count=0
	for line in input_str.split("\n"):
		first,second = line.split(",")
		first  = first.split('-')
		second = second.split('-')

		if((int(first[1])>=int(second[0]) and int(first[0])<=int(second[1])) or (int(first[1])>=int(second[0]) and int(first[0])<=int(second[1]))):
			count+=1
	return count

def test_easy_input_first(input_str):
   assert execute_first(input_str) == 2

def test_easy_input_second(input_str):
   assert execute_second(input_str) == 4

if __name__ == '__main__':
	test_easy_input_first(input_str_trivial)
	test_easy_input_second(input_str_trivial)

	print(execute_first(input_str))
	print(execute_second(input_str))

