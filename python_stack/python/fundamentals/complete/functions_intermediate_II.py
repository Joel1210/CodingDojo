# x = [ [5,2,3], [15,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Bryant'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 30} ]

def iterateDictionary(std):
    count = 0
    fname = ""
    lname = ""
    for key in std:
        for k,v in key.items():
            if k == "first_name":
                fname = v
                count = count + 1
            if k == "last_name":
                lname = v
                count = count + 1
            if count == 2:
                count = 0
                print(f"first_name - {fname}, last_name - {lname}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(keyitem, std):
    count = 0
    fname = ""
    lname = ""
    for key in std:
        for k,v in key.items():
            if k == "first_name":
                fname = v
                count = count + 1
            if k == "last_name":
                lname = v
                count = count + 1
            if count == 2:
                count = 0
                if keyitem == "first_name":
                    print(fname)
                if keyitem == "last_name":
                    print(lname)

# iterateDictionary2('first_name',students)

def printInfo(djinfo):
    loccount = len(djinfo["locations"])
    inscount = len(djinfo["instructors"])
    print(f"{loccount} LOCATIONS")
    for key in djinfo["locations"]:
        print(key)
    print(f"\n{inscount} INSTRUCTORS")
    for key in djinfo["instructors"]:
        print(key)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)


# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

