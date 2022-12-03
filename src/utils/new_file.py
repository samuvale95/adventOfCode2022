import os

l = filter(lambda x: "__" not in x and ".py" in x, os.listdir("src"))
l = list(l)
n = int(sorted(l)[-1][:2]) + 1 if len(l) > 0 else 1

DEFAULT_FILE = f"from utils.api import get_input\n\ninput_str = get_input({n})\n\n# WRITE YOUR SOLUTION HERE\n\ndef execute_first(input_str):\n\tpass\n\ndef execute_second(input_str):\n\tpass\n\nif __name__ == '__main__':\n\tpass"

path = f"src/{n:02d}.py"
with open(path, "w") as f:
    f.write(DEFAULT_FILE)

print(f"Enter your solution in {path}")
