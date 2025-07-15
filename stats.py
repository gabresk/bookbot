def word_count(text):
    return len(text.split())

def count_char(text):
    chars = {}
    for char in text:
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars

def sort_on(items):
    return items["num"]


def sort_dict(d):
    sorted_list = []
    for key in d:
        sub_dict = {}
        sub_dict["char"] = key
        sub_dict["num"] = d[key]
        sorted_list.append(sub_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list





