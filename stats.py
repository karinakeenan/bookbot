def get_num_words(text):
    words = text.split()
    return len(words)

def num_of_char(text):
    characters= {}
    for char in text:
        c = char.lower()
        if c not in characters:
            characters[c] = 1
        else:
            characters[c] += 1
    return characters

def sorted_list(characters):
    sort_list = []
    for ch,cnt in characters.items():
        if not ch.isalpha():
            continue
        sort_list.append({"char": ch, "num": cnt})

    def sort_on(item):
        return item["num"]

    sort_list.sort(key=sort_on, reverse=True)
    return sort_list
