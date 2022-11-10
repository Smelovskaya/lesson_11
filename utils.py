import json
def load_candidates_from_json():
    '''загружает список кандидатов из файла json'''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def get_candidates_all():
    '''возвращает список всех кандидатов'''
    return load_candidates_from_json()

def get_candidate(id):
    '''возвращает одного кандидата по его id'''
    for candidate in get_candidates_all():
        if candidate['id'] == id:
            return candidate
    return {}

def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени'''
    candidates = []
    for candidate in get_candidates_all():
        if candidate_name in candidate['name']:
            candidates.append(candidate)
    return candidates

def get_candidates_by_skill(skill):
    '''возвращает кандидатов по навыку'''
    candidates = []
    for candidate in get_candidates_all():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            candidates.append(candidate)
    return candidates

