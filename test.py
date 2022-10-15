import json
from faker import Faker

faker = Faker()

# required = {}
# with open('static/types.json') as file:
#     fields = json.load(file)
#     for key,value in fields.items():
#         cmd = f'faker.{key}()'
#         val = eval(cmd)
#         if type(val) not in [set,list,tuple]:
#             required.update({key:value})
# with open('static/edited.json','w') as file:
#     json.dump(required,file)

with open('static/types.json','r') as file:
    obj =  json.load(file)
    for ob in obj.keys():
        cmd = f'faker.{ob}()'
        val = eval(cmd)
        if type(val) in [set,list,tuple]:
            print(val)
    