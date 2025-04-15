# Define a dictionary
row = {
    "First name": "<your first name>",
    "Last name": "<your last name>",
    "Favorite food": ["a","b","c"],
}


print(row)      # print the dictionary. The dictionary contains the keys "First name", "Last name", and "Favorite food" and the values "<your first name>", "<your last name>", and ["a","b","c"]
print(type(row))        # print the type of the dictionary. The type of the dictionary is dict.

print(row["First name"])    # print the value of the key "First name". The value is "<your first name>"

row["Hobbies"] = ["1","2"]      # add a new key-value pair to the dictionary. The key is "Hobbies" and the value is ["1","2"]
print(row)      # print the dictionary. The dictionary contains the keys "First name", "Last name", "Favorite food", and "Hobbies" and the values "<your first name>", "<your last name>", ["a","b","c"], and ["1","2"]
print(row["Hobbies"])   # print the value of the key "Hobbies". The value is ["1","2"]

print(row.get("Moto"))      # print the value of the key "Moto". The value is None.
print(row.get("Motto", "World peace!"))     # print the value of the key "Motto". The value is "World peace!".

"""Output

{'First name': '<your first name>', 'Last name': '<your last name>', 'Favorite food': ['a', 'b', 'c']}
<class 'dict'>
<your first name>
{'First name': '<your first name>', 'Last name': '<your last name>', 'Favorite food': ['a', 'b', 'c'], 'Hobbies': ['1', '2']}
['1', '2']
None
World peace!
"""