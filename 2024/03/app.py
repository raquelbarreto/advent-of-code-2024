import re

def find_valid_instructions(string):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, string)
    results = [(int(a), int(b)) for a, b in matches if len(a) <= 3 and len(b) <= 3 ]

    return results

def calculate(results):
    numbers = []
    for result in results:
        multiplication = result[0] * result[1]
        numbers.append(multiplication)

    return(sum(numbers))

if __name__ == '__main__':

    file = open("input.txt")
    file_content = file.read()
    results = find_valid_instructions(file_content)
    result = calculate(results)
    print("Result: ", result)