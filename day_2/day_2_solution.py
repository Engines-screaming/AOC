'''
For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''

class Solver:

    def __init__(self, input_path):
        self.input_list = []
        self.parsed_input = []
        self.valid_count = 0

        with open(input_path) as f:
            for line in f:
                self.input_list.append(line)

    def parse_strings(self):
        for input_str in self.input_list:
            char_range, tracked_char, pw = input_str.split(" ")

            temp_dict = {}  # to store parsed info

            # parse char count ranges
            temp_dict['min_count'] = char_range[0]
            temp_dict['max_count'] = char_range[-1]

            # parse char to track
            temp_dict['tracked_char'] = tracked_char[0]

            # store pw
            temp_dict['pw'] = pw

            self.parsed_input.append(temp_dict)


if __name__ == '__main__':
    s = Solver('passwords.txt')
    s.parse_strings()
    print(s.parsed_input)