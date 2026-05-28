def reverse_string(string):
    """Return a new string which is the reverse of `string`."""
    return string[::-1]

def reverse_string(string):
    # get length of string
    # loop through string
    # while looping start from end of string
    # append to new array
    # return new array
    reversed_string = []
    index = len(string)
    while index > 0:
       reversed_string.append(string[index - 1])
       index -= 1
    return "".join(reversed_string) 