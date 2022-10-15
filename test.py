import json
from faker import Faker

faker = Faker()

def create_table(table,fields):
    sql = ''
    sql += f'CREATE TABLE {table} (\n'
    sql += '\bid SERIAL PRIMARY KEY'
    for field in fields:
        value = eval(f'type(faker.{field}())')
        dtype = 'INT' if value == int else 'VARCHAR(255)' if value == str else ''
        sql += f'\b{field} '
    return

def generator(table,qty,fields):
    pass

with open('static/types.json') as file:
    types =  json.load(file)
    values = []
    for type_ in types:
        cmd = f'type(faker.{type_}())'
        try:
            val = eval(cmd)
        except:
            print('err',type_)
    #     value = eval(f'type(faker.{type_}())')
    #     values.append(value)
    # print(set(values))