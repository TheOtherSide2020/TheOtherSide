#This code reads the json file from the unity front end and parses the template, questions, username, timestamp etc.
import json

with open('../Json/data.txt') as json_file:
    data = json.load(json_file)
    for p in data['template']:
        print('Name: ' + p['name'])
        print('Text: ' + p['text'])
        print('User: ' + p['user'])
        print('')

