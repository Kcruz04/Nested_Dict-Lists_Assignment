# Note: Avoid using class keywords like int, str, list, and dict as variable/parameter names.



# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)


# Change the last_name of the first student from 'Jordan' to 'Bryant'

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] ='Bryant'
print(students)
# In the sports_directory, change 'Messi' to 'Andres'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
#the key of 'y' is in index 0 because the curly brackets encapsulate both keys as index 0
#could not target 'y' key because I thought it was index 1
z[0]['y'] = 30
print(z)


#Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, 
# given a list of dictionaries, the function loops 
# through each dictionary in the list and prints each 
# key and the associated value. For example, given 
# the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for keys in students:
        print(keys)
iterateDictionary(students)


def iterateDictionary(other_list):
    for keys in students:
        print(f'first_name','-',keys['first_name']+',','last_name',' - ',keys['last_name'])
        #use keys[] to target value of each key
iterateDictionary(students)



# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#Get Values From a List of Dictionaries

#Create a function iterateDictionary2(key_name, some_list)
#that, given a list of dictionaries and a key name, the function
#prints the value stored in that key for each dictionary. 
# For example, iterateDictionary2('first_name', students) should output:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name, some_list):
    for keys in students:
        print(keys['first_name'])
iterateDictionary2('first_name',students)

def iterateDictionary2(key_name, some_list):
    for keys in students:
        print(keys['last_name'])
iterateDictionary2('last_name',students)


# Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict)
# that given a dictionary whose values are all lists,
# prints the name of each key along with the size of
# its list, and then prints the associated values
# within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for keys in dojo.keys():
        print(len(dojo[keys]),keys)
    print(dojo['locations'])
    print(dojo['instructors'])
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
