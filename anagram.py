def revers(text):
    list_res = list(text)
    i = 0
    j = len(text) - 1
    while i < j:
        if not list_res[i].isalpha():
            i += 1
        elif not list_res[j].isalpha():
            j -= 1
        else:
            new_char = list_res[i]
            list_res[i] = list_res[j]
            list_res[j] = new_char
            i += 1
            j -= 1
    return ''.join(list_res)


def create_list(text):
    return list(text.split(" "))


def make_anagram(text):
    res = []
    for i in create_list(text):
        res.append(revers(i))
    return ' '.join(res)
