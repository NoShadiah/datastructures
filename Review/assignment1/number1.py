import json

mydictionary = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'},
                              {'firstName': 'Mervin', 'lastName':'Friedland'},
                                {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 
                'teachers': [{'firstName': 'Amberly','lastName': 'Calico'},
                            {'firstName': 'Regine', 'lastName': 'Agtarap'}]}

# Createing the json file
with open('the_jsonfile.json', 'w') as f:
    json.dump(mydictionary, f)