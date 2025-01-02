from itertools import product
import re

DEBUG = False

def find_combinations(n):
    combinations = list(product(['*', '+'], repeat=n))
    return combinations

def validate_line(line):
    target = int(line.split(":")[0])
    numbers = line.split(":")[1]
    numbers_list = numbers.strip().split(" ")
    number_of_operators = len(numbers_list) - 1

    if (DEBUG):
        print("----------")
        print("Target: ", target)
        print("Numbers: ", numbers_list)
        print("Number of operators: ", number_of_operators)

    combinations = find_combinations(number_of_operators)

    for combination in combinations:
        expression = '(' * (len(numbers_list)) + ''.join(f"{number}){combination}" for number, combination in zip(numbers_list, combination)) + numbers_list[-1] + ')'
        results = eval(expression)
        if results == target:
            return True
    return False


if __name__ == '__main__':
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]

    valid_equations = []
    result = 0

    for line in lines:
        if validate_line(line):
            valid_equations.append((line))

    totals = [item.split(':')[0] for item in valid_equations if ':' in item]
    total_sum = sum(int(num) for num in totals)

    print("Total: ", total_sum)
