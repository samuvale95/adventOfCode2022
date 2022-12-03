from utils.api import get_input

input_str = get_input(2)
input_str_trivial = """A Y
B X
C Z"""

"""
A: Sasso   > Z
B: Carta > X
C: Forbice   > Y
"""
def execute_first(input_str):
    translate = {
        "A":"X",
        "B":"Y",
        "C":"Z"
    }

    shapes = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    winner = {
        "X": "Z",
        "Y": "X",
        "Z": "Y"
    }

    point = 0
    for match in input_str.split("\n"):
        elf, me = match.split(" ")
        if(winner[me] == translate[elf]):
            point += 6
        elif(me == translate[elf]):
            point +=3
        point+=shapes[me]
    
    return point

def execute_second(input_str):
    translate = {
        "X":"lose",
        "Y":"draw",
        "Z":"win"
    }

    shapes = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    loser = {
        "C":"A",
        "A":"B",
        "B":"C"
    }

    winner = {
        "A":"C",
        "B":"A",
        "C":"B"
    }

    point = 0
    for match in input_str.split("\n"):
        me = ""
        elf, code = match.split(" ")
        type = translate[code]
        if(type == "win"):
            point += 6
            me = loser[elf]
        elif(type == "draw"):
            point +=3
            me = elf
        else:
            me = winner[elf]

        point+=shapes[me]
    
    return point

def test_easy_input_first(input_str):
   assert execute_first(input_str) == 15

def test_easy_input_second(input_str):
   assert execute_second(input_str) == 12

if __name__ == '__main__':
    test_easy_input_first(input_str_trivial)
    test_easy_input_second(input_str_trivial)

    print(execute_first(input_str))
    print(execute_second(input_str))
