import json
from faker import Faker

faker = Faker()

def create_table(table,fields):
    sql = ''
    sql += f'CREATE TABLE {table} (\n'
    sql += '\tid SERIAL PRIMARY KEY,\n'
    i = 0
    for field in fields:
        cmd = f'type(faker.{field}())'
        value = eval(cmd)
        if value not in [list,set,tuple]:
            dtype = 'INT' if value == int else 'VARCHAR(255)' if value == str else 'FLOAT'
            sql += f'\t{field} {dtype}\n' if len(fields) -1 == i else f'\t{field} {dtype},\n'
        i += 1
    sql += ');\n'
    return sql

def insert_into(table,fields):
    sql = f'INSERT INTO {table} {tuple(fields)} VALUES ('
    i = 0
    for field in fields:
        cmd = f'faker.{field}()'
        value = eval(cmd)
        value =  f"'{value}'" if type(value) == str else value
        sql += f'{value});\n' if len(fields) -1 == i else f'{value},'
        i += 1
    return sql


def gen_sql(table,qty,fields):
    sql = ''
    sql += create_table(table,fields)
    for i in range(qty):
        sql += insert_into(table,fields)
    return sql


