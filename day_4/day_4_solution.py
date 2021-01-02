'''
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

- byr (Birth Year)
- iyr (Issue Year)
- eyr (Expiration Year)
- hgt (Height)
- hcl (Hair Color)
- ecl (Eye Color)
- pid (Passport ID)
- cid (Country ID)
'''

# read in inputs

with open('input.txt') as f:
    input_txt = f.read()

documents = input_txt.split('\n\n')
print(documents[0])