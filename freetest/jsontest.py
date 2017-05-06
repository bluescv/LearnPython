import json

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

print(json.loads(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])))

content = json.dumps({'errorcode': '0', 'msg': 'OK'})

errorcode = json.loads(content)

for key, value in errorcode.items():
    if key == 'errorcode':
        print(value)
# print(repr(errorcode))

print('---end---')

'''
codes used to generate json object then dump to json string
'''
result_dict = {}
result_dict['name'] = 'name1'
result_dict['gender'] = 1

for key, value in result_dict.items():
    print(key, value)

result_json = json.dumps(result_dict)
print(result_json)
