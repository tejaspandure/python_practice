

nDictionary = {'course':'python','fees':123444,
               1: {'course':'java','fees':444444},
               2: {'course':'ppa','fees':30000},
               3: {'course': "lb", 'fees':78545}}

print(nDictionary['course'])
print(nDictionary['fees'])

print(nDictionary[1]['course'])
print(nDictionary[1]['fees'])

nDictionary['course'] = "Machine Learning"
nDictionary[1]['fees'] = 7837493

print("updated dictionary: ",nDictionary)

