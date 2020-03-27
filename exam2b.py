def duplicate_strings(string_list, integer_list):
    new_string = []
    for i in string_list:
        string_list = string_list[0] * integer_list[i]
    return string_list
