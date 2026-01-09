dNames = {101: "rahul",
         102: "sham",
         103: "ram",
         104: "aniket",
         105: "akshay"}

print("original dictionary: ",dNames)
dNames.update({104:'Tejas'})
print("updated dictionary: ",dNames)


vals = {201: "rahul",
         202: "sham",
         203: "ram",}
dNames.update(vals)

print("updated: ",dNames)
dNames.pop(102)
print("after pop",dNames)

print()
print("original dictionary: ",dNames)
dNames.popitem()
print("after pop ", dNames)