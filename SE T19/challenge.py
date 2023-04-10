def add_prefix_un(string):
    print('un'+str(string))
    return 'un'+str(string)

add_prefix_un('happy')

def make_word_groups(list):
    prefix = list[0]
    group = []
    for string in list:
        if string == prefix:
            group.append(string)
        else:
            group.append(prefix + string)
    print(' :: '.join(group))
    return ' :: '.join(group)

make_word_groups(['en', 'close', 'joy', 'lighten'])

def remove_suffix_ness(string):
    print(string[:-4])
    return string[:-4]

remove_suffix_ness('sadness')

def adjective_to_verb(sentence, index):
    list_sentence = sentence.replace('.','').split()
    print(list_sentence[index]+'en')
    return list_sentence[index]+'en'

adjective_to_verb('I need to make that bright.', -1 )

print(float(0))