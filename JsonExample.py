import json

SampleDict = {
    'Name': 'Balraj',
    'Marks': [78, 87,90, 85],
    'Pass':   True,
    'age':  28,
    'object': {
        'color': ('Red', 'Blue')
    }
}
with open('demo.json','w') as fh:
    fh.write(json.dumps(SampleDict, indent=2))
#in the write function we are dumping which is nothing but writing data into json file.
fh.close()
#print(json.dumps(SampleDict, indent=2))

fh = open('demo.json', 'r')
json_str = fh.read()
json_data = json.loads(json_str)
# In the above json.load function will convert json string format into a json object i.e dict notation.
print(json_data['age'])
print(json_data['object']['color'])
#print(type(json_data))

