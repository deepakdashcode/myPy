import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )


cat
bat
pat
mat
rat


coreyms.com
321-555-4321
123.555.1234
123*555*1234
123-232*2322
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence='Start a sentence and then bring it to an end'

# pattern = re.compile(r'(Mr|Ms|Mrs)(\.?\s[A-Z]\w*)')
# matches = pattern.findall(text_to_search)
#print(matches)
#Output -->  [('Mr', '. Schafer'), ('Mr', ' Smith'), ('Ms', ' Davis'), ('Mrs', '. Robinson'), ('Mr', '. T')]




# pattern = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}')
# matches = pattern.findall(text_to_search)
# for match in matches:
#     print(match)

#Output
# 321-555-4321
# 123.555.1234
# 800-555-1234
# 900-555-1234

# pattern = re.compile(r'(\d{3})[-.](\d{3})[-.](\d{4})')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match.groups())
# print(matches)
#
# Output
# ('321', '555', '4321')
# ('123', '555', '1234')
# ('800', '555', '1234')
# ('900', '555', '1234')

pattern = re.compile(r'\d{3}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match.group())