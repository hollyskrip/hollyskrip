import dbm
dbm2=dbm.open("photo_category.keys()","c")
db2["animals.png"]="a large animal"
db2["coffee.png"]="a cup of coffee"
db2["pencil.png"]="a green pencil"
for item in db2:
    print(item,db2[item])
