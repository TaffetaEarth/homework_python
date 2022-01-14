def string_part(string_to_get_part_from, starts_with=None, end_with=None, step=None):
    return string_to_get_part_from[starts_with:end_with:step]


# print(string_part("abcdefghijklmn", 4, 10, 2)


# def strings(text, symb):
#     indexes = []
#     for i in range(len(text)):
#         if text[i] == symb:
#             indexes.append(i)
#     return indexes
#
# print(strings("aaabaaa", 'a'))
