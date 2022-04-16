"""All non-letter symbols should stay on the same places.
E.g. "a1bcd efg!h" => "d1cba hgf!e"
Use Latin alphabet for test only."""

from anagram import make_anagram #, make_list_isalpha

string = 'a1bcd efg!h lkjhdf7,j  zdf121aasf'
print(f'String --> {string}')

result = make_anagram(string)
print(f'Result --> {result}')

# text = 'lkjhdf7,j'
#
# print(make_list_isalpha(text))

if __name__ == '__main__':
    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("1 a", "1 a"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert make_anagram(text) == reversed_text, "Whoops, something went wrong"
    print('True')
