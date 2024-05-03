# Script to read elements in the MongoDB 

import pymongo
import json

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")

mydatabase = client['jsonDB']

def convert_numeric_to_str(d):
    cur_type = type(d)

    if cur_type == dict:
        for key, value in d.items():
            d[key] = convert_numeric_to_str(value)

    elif cur_type == list:
        for i, el in enumerate(d):
            d[i] = convert_numeric_to_str(el)

    else:
        if cur_type in [int, float]:
            d = str(d)

    return d


def convert_str_to_numeric(d):
    cur_type = type(d)

    if cur_type == dict:
        for key, value in d.items():
            d[key] = convert_str_to_numeric(value)

    elif cur_type == list:
        for i, el in enumerate(d):
            d[i] = convert_str_to_numeric(el)

    else:
        if cur_type == str:
            try:
                d = int(d)
            except ValueError:
                try:
                    d = float(d)
                except ValueError:
                    pass

    return d


def serialize(data):
    #if isinstance(data, types.GeneratorType):
    #    data = list(data)
    return convert_numeric_to_str(data)

def deserialize(data):
    return convert_str_to_numeric(data)

for obj in mydatabase['jsons'].find({"tests":{"$elemMatch":{"outcome":"failed", "nodeid":"test_pll.py::test_pllautolock"}}}):
    obj = deserialize(obj)
    print('FPGA-hexa-IP',obj['FPGA-hexa-IP'])
    print(len(obj['tests']))
    for el in obj['tests']:
        print(el['outcome'])


# print(list(mydatabase.jsons.find({"tests":{"$elemMatch":{"outcome":"passed", "nodeid":"test_pll.py::test_pllautolock"}}})))