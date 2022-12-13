from utils.api import get_input
import math
import numpy as np

input_str = get_input(10)
input_str_trivial = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def execute_first(input_str):
    o=[]
    X=1

    for line in input_str.split("\n"):
        if(line[:4] == 'addx'):
            o.append(X)
            o.append(X)
            X+=int(line.split(" ")[1])
        else:
            o.append(X)
    
    return sum([o[i-1]*i for i in [20,60,100,140,180,220]])

def draw_pixel(CRT, sprint, o):
    if(len(o) in sprint):
        CRT[len(o)] = '#'
    return CRT

def execute_second(input_str):
    CRT = ['.' for i in range((40*6))]
    o=[]
    X=1

    for line in input_str.split("\n"):
        if(line[:4] == 'addx'):
            o.append(X)
            o.append(X)
            X+=int(line.split(" ")[1])
        else:
            o.append(X)

    _min=0
    _max=40
    for _ in range(1,7):
        for i in range(_min, _max):
            if(i in [(o[i]+_min), (o[i]+1)+_min, (o[i]-1)+_min]):
                CRT[i]="##"
            else:
                CRT[i]='..'
        _min=_max
        _max+=40
    
    for i in np.reshape(CRT,(6,40)):
        print(''.join(i))

def test_easy_input_first(input_str_trivial):
    assert execute_first(input_str_trivial) == 13140

def test_easy_input_second(input_str_trivial):
    execute_second(input_str_trivial)

if __name__ == '__main__':
    test_easy_input_first(input_str_trivial)
    test_easy_input_second(input_str_trivial)

    print(execute_first(input_str))
    print(execute_second(input_str))
