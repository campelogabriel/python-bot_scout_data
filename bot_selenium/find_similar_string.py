from fuzzywuzzy import fuzz

def find_similar_string(user,system):
    ratio_obj = {
        'nome_liga' : "",
        "ratio" : 0
    }
    for word in system:
        if 'campeonato' in str.lower(word):
            word = " ".join(str.lower(word).split('campeonato'))
        ratio = fuzz.ratio(str.lower(word), str.lower(user)) 
        if ratio > ratio_obj['ratio']:
            ratio_obj['ratio'] = ratio
            ratio_obj['nome_liga'] = word

    return ratio_obj['nome_liga']

