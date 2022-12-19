import json

def load_candidates():
    with open('data.json', encoding='utf-8') as file:
        info = json.load(file)
    return info 

def load_candidate(pk):
    for i in load_candidates():
        if i['pk'] == pk:
            return i

def get_by_skill(skill):
    return [i for i in load_candidates() if skill.lower().strip() in i['skills']]

