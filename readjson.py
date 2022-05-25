# readjson.py

import json     # นิยมใช้ export ข้อมูลเป็น json

def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0]['point'])
	return data


def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)   # indent= แบ่งเป็นบรรทัด
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)

data = {'1234567890':['Banana',100,5],
		'1234567891':['Durian',150,99],
		'1234567892':['Apple',200,10],
		'1234567890':['มังคุด',100,5]}

writejson(data)