from utils.api import get_input

input_str = get_input(1)
input_str_trivial= """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

def execute_first(input_str):
    max_calories = 0
    elf_calories = input_str.split("\n\n")
    for i in elf_calories:
        elf_calories = sum([int(j) for j in i.split("\n")])
        if(elf_calories>max_calories):
            max_calories = elf_calories
    return max_calories

def execute_second(input_str):
    calories = []
    elf_calories = input_str.split("\n\n")
    for i in elf_calories:
        calories.append(sum([int(j) for j in i.split("\n")]))
    return sum(sorted(calories, reverse=True)[:3])

def test_easy_input_first(input_str):
   assert execute_first(input_str) == 24000

def test_easy_input_second(input_str):
   return execute_second(input_str) == 45000

if __name__ == '__main__':
    test_easy_input_first(input_str_trivial)
    test_easy_input_second(input_str_trivial)

    print(execute_first(input_str))
    print(execute_second(input_str))