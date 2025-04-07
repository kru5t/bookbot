def word_count(contents):
    return len(contents.split())

def character_count(contents):
    char_dict = {}

    for char in contents:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def report(char_dict):
    def sort_on(item):
        return item[1]

    sorted_dict = dict(sorted(char_dict.items(), key=sort_on, reverse=True))

    return sorted_dict
