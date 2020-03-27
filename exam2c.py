def get_row_range(input_string):
    entries = input_string.split(",")
    entries.remove('\n')
    lowest = 0
    highest = 0
    for val in entries:
        if val < lowest:
            lowest = val
        if val > highest:
            highest = val
    return highest - lowest
