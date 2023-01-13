import json
from vars import *


def write_in_output():
    str_json_output['address'] = data['address']['value']
    str_json_output['allow_messages'] = True
    str_json_output['billing_types'] = "packageOrSingle"
    str_json_output['business_area'] = 1
    str_json_output['contacts'] = contacts_in
    str_json_output['coordinates'] = {'latitude': data['address']['lat'], 'longitude': data['address']['lng']}
    str_json_output['description'] = data['description']
    str_json_output['experience'] = {'id': 'noMatter'}
    str_json_output['html_tags'] = True
    str_json_output['image_url'] = "https://img.hhcdn.ru/employer-logo/3410666.jpeg"
    str_json_output['name'] = data['name']
    str_json_output['salary'] = data['salary']['to']
    str_json_output['salary_range'] = {'from': data['salary']['from'], 'to': data['salary']['to']}
    str_json_output['schedule'] = {'id': data['employment']}


def get_phone():
    phone['city'] = data['contacts']['phone'][1:4]
    phone['country'] = data['contacts']['phone'][0]
    phone['number'] = data['contacts']['phone'][4:7] + '-' + data['contacts']['phone'][7:9] + '-' + data['contacts']['phone'][9:]
    return phone


def get_contacts():
    contacts['email'] = data['contacts']['email']
    contacts['name'] = data['contacts']['fullName']
    contacts['phone'] = phone_in
    return contacts


str_json_output = {}
contacts = {}
phone = {}
data = json.loads(str_json_input)
phone_in = get_phone()
contacts_in = get_contacts()
write_in_output()
new_json = json.dumps(str_json_output, indent=2)
print(new_json)

with open('data.json', 'w') as data_out:
    json.dump(str_json_output, data_out, indent=2)




''' 
Переменные: "allow_messages", "billing_type", "business_area", "html_tags", "image_url" были прописаны вручную, так как отсутствовали в исходных данных. Как я понимаю, эти данные сформированны через API hh.ru, но в тестовом разговора об использовании API не было. Также исходные данные я не стал помещать отдельно в JSON-файл, так как это прописано тоже не было. Но вывод я сделал уже в Json-файл. Pydantic не использовал, если честно, ни разу не сталкивался.
'''