import json

with open ('json_test.txt', 'r+', newline='') as file:
    l = ['List', 'pringls', 'Showmaker', 'Tarkov123']
    num = [2, 3, 6, 9, 10]
    ser = zip(l, num)
    
    for el in ser:
        file.write(str(el[0]))
        file.write('\n')

myDict = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zipcode": "12345"
    },
    "email": "[email protected]",
    "age": 32
}
        
with open('json.json', 'w') as file2:
    json.dump(myDict, file2)
    
        