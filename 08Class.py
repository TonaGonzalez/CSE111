#DICTIONARIES

elements = [ 
    {"Symbol": "Ac",
    "Name" : "Actinium",
    "Mass": 227}
]

#Find items in a dictionary
first_dictionary = {"name": "Jonathan",
                    "LastName": "Smith",
                    "INumber": 123456789,
                    "Address": "Jonny@byui.edu",
                    "Biography": "link.com",
                    }
print(first_dictionary)
print(first_dictionary["name"])


'''loop through a list'''
#for i, value in enumerate(elements):
    #print(f"The Symbol is: " + {value{}

#Add Items to a dictionary
first_dictionary["name"] = "Carlos"
print(first_dictionary)


for i in first_dictionary:
    print(f"{i}: {str(first_dictionary.get(i))}")


