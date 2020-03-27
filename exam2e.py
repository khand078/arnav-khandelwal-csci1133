def remove_comments(line_list):
    clines = 0
    for i in range(len(line_list)-1, -1, -1):
        if '#' in line_list[i]:
            clines += 1
            line_list.pop(i)
    return clines
