import json

customer = {
    'id' : 152352,
    'name' : '강진수',
    'history' : [
        {'date' : '2015-03-11', 'item' : 'iPhone'},
        {'date' : '2016-02-23', 'item' : 'Monitor'},
    ]
}

jsonString = json.dumps(customer, indent=4)

print(jsonString)
print(type(jsonString))