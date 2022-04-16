# def revers(text):
#     list_res = list(text)
#     i = 0
#     j = len(text) - 1
#     # print(list_res)
#     while i < j:
#         if not list_res[i].isalpha():
#             i += 1
#         elif not list_res[j].isalpha():
#             j -= 1
#         else:
#             new_char = list_res[i]
#             list_res[i] = list_res[j]
#             list_res[j] = new_char
#             i += 1
#             j -= 1
#     return ''.join(list_res)

# def make_list_isalpha(text):
#     # return ''.join(reversed([i if i.isalpha else dict.update(i) for i in text]))
#     return ''.join(reversed([i for i in text if i.isalpha()]))


# def make_anagram(text):
#     for word in text.split(' '):
#         print(word)
#         return ''.join(reversed([i for i in word if i.isalpha()]))

def make_revers(text):
        rev_list_with_alpha = [letter for letter in text if letter.isalpha()]
        rev_list_with_alpha.reverse()
        for k, v in enumerate(num for num in (letter for letter in text)):
            if not v.isalpha():
                rev_list_with_alpha.insert(k, v)
        return ''.join(rev_list_with_alpha)

def make_anagram(text):
    return ' '.join([make_revers(i) for i in text.split(" ")])
