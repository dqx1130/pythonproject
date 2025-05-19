def acronym(phrase):
    phrase_list = phrase.split()
    new_phrase = ''
    for each in phrase_list:
        new_phrase += each[0].upper()
    return new_phrase

phrase= "central  processing  unit"
print(acronym(phrase))