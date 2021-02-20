def find():
    import re
    string1='wateeeer'
    if re.search('wate{4,1}r',string1):
        print ("String Found")
    else :
        print(" No Match")

find()