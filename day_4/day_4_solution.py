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

VERBOSE = True  # debugging

# read in inputs
# input_file = 'test_input.txt'
input_file = 'input.txt'

with open(input_file) as f:
    input_txt = f.read()

documents = input_txt.split('\n\n')  # put each doc in a list

# make a list of dicts. each dict is key value pairs of fields in doc. 
parsed_docs = []
for doc in documents:
    doc_dict = {}
    doc = doc.replace('\n', ' ')
    kv_pairs = doc.split(' ')

    for pair in kv_pairs:
        k, v = pair.split(':')
        doc_dict[k] = v
    
    parsed_docs.append(doc_dict)
    
# check for validity
check_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_count = 0
invalid_count = 0
for doc in parsed_docs:
    valid = True
    for field in check_fields:
        if field not in doc:
            valid = False
            
            if VERBOSE:
                print(f"key not in check field: {field}")

    if valid == False:
        invalid_count += 1
    else:
        valid_count += 1
        
        if VERBOSE:
            print(f'dict not valid:{doc}\n')

print(f'The amount of valid passports: {valid_count}.\nInvalid passports: {invalid_count}')
    