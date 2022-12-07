import os

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = f"""from utils.api import get_input

input_str = get_input({n})
input_str_trivial = ''

def execute_first(input_str):
    pass

def execute_second(input_str):
    pass

def test_easy_input_first(input_str_trivial):
	assert execute_first(input_str_trivial) == ""
    #ADD MORE TESTS HERE


def test_easy_input_second(input_str_trivial):
    assert execute_first(input_str_trivial) == ""
    #ADD MORE TESTS HERE

if __name__ == '__main__':
    test_easy_input_first(input_str_trivial)
	test_easy_input_second(input_str_trivial)

	print(execute_first(input_str))
	print(execute_second(input_str))
"""

path = f"src/{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
