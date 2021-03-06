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

        with open(input_path) as f:
            for line in f:
                self.input_list.append(line)

    def parse_strings(self):
        for input_str in self.input_list:
            char_range, tracked_char, pw = input_str.split(" ")

            temp_dict = {}  # to store parsed info

            # parse char count ranges
            temp_range = char_range.split('-')
            temp_dict['min_count'] = int(temp_range[0])
            temp_dict['max_count'] = int(temp_range[1])

            # parse char to track
            temp_dict['tracked_char'] = tracked_char[0]

            # store pw
            temp_dict['pw'] = pw

            self.parsed_input.append(temp_dict)

    def check_passwords_pt1(self, debug=False):
        valid_count = 0

        for input_dict in self.parsed_input:
            char_count = input_dict['pw'].count(input_dict['tracked_char'])

            if debug:
                print(input_dict, char_count)

            if char_count >= input_dict['min_count'] and char_count <= input_dict['max_count']:
                valid_count += 1

                if debug:
                    print("passed\n")
        
        return valid_count
    
    def check_passwords_pt2(self):
        valid_count = 0

        for input_dict in self.parsed_input:
            # range args are actually position this time:
            pos1 = input_dict['min_count']
            pos2 = input_dict['max_count']

            cond1 = input_dict['pw'][pos1 - 1] == input_dict['tracked_char']
            cond2 = input_dict['pw'][pos2 - 1] == input_dict['tracked_char']

            if cond1 == True and cond2 == False:
                valid_count += 1
            elif cond2 == True and cond1 == False:
                valid_count += 1
        
        return valid_count


if __name__ == '__main__':
    s = Solver('passwords.txt')
    s.parse_strings()
    valid_pws = s.check_passwords_pt1()
    print(f'Amount of valid passwords in pt1: {valid_pws}')

    valid_pws = s.check_passwords_pt2()
    print(f'Amount of valid passwords in pt2: {valid_pws}')