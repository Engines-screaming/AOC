'''
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
'''


class Solver:

    def __init__(self, input_file_path):
        self.data = []

        with open(input_file_path) as f:
            for line in f:
                data = int(line)
                self.data.append(data)

    def solve_two(self):
        for item in self.data:
            for index in range(len(self.data)):
                temp = item + self.data[index]
                if temp == 2020:
                    return (item, self.data[index], item*self.data[index])

    def solve_three(self):
        for item in self.data:
            for index1 in range(len(self.data)):
                for index2 in range(len(self.data)):
                    temp = item + self.data[index1] + self.data[index2]
                    if temp == 2020:
                        return (item, self.data[index1], item*self.data[index2], item*self.data[index1]*self.data[index2])


if __name__ == '__main__':
    s = Solver('expense_report.txt')

    # solve first problem
    answer1 = s.solve_two()
    print(f"First answer (first number, second number, multiplied num): {answer1}")

    # solve second problem
    answer2 = s.solve_three()
    print(f"Second answer (first number, second number, third number, multiplied num): {answer2}")