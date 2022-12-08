from utils.api import get_input
import numpy as np
from functools import reduce

input_str = get_input(8)
input_str_trivial = """30373
25512
65332
33549
35390"""

def execute_first(input_str):
    forest = np.array([ list(map(int,[*i] )) for i in input_str.split("\n")])
    forest_T = forest.T
    visible_trees = ((len(forest[0])+len(forest_T[0]))*2)-4

    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            current_tree = forest[i][j]
            if(any([current_tree>k for k in (max(forest[i][:j]), max(forest[i][j+1:]), max(forest_T[j][:i]), max(forest_T[j][i+1:]))])): visible_trees+=1

    return visible_trees

def get_visibility(tree_list, current_tree):
    count=0
    for i in tree_list:
        count+=1
        if(i>=current_tree): 
            break
    return count

def execute_second(input_str):
    forest = np.array([ list(map(int,[*i] )) for i in input_str.split("\n")])
    forest_T = forest.T
    tree_scores = list()

    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            current_tree = forest[i][j]
            tree_scores.append(reduce(lambda a,b: a*b, map(lambda a: get_visibility(a, current_tree), (np.flip(forest[i][:j]), forest[i][j+1:], np.flip(forest_T[j][:i]), forest_T[j][i+1:]))))
    return max(tree_scores)

def test_easy_input_first(input_str_trivial):
    assert execute_first(input_str_trivial) == 21


def test_easy_input_second(input_str_trivial):
    assert execute_second(input_str_trivial) == 8

if __name__ == '__main__':
    test_easy_input_first(input_str_trivial)
    test_easy_input_second(input_str_trivial)

    print(execute_first(input_str))
    print(execute_second(input_str))
