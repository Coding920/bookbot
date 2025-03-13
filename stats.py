def word_count(text: str) -> int:
    words = text.split()
    return len(words)


def letter_count(text: str) -> int:
    word_dict = {}

    for word in text:
        for char in word:
            try:
                word_dict[char.lower()] += 1
            except Exception:
                word_dict[char.lower()] = 1

    return word_dict


def sort_dict(d: dict) -> list[dict]:
    dict_list = []
    for pair in d.items():
        pair = list(pair)
        if pair[0].isalpha():
            new_dict = {"letter": pair[0], "value": pair[1]}
            dict_list.append(new_dict)

    dict_list.sort(reverse=True, key=lambda inner: inner["value"])
    return dict_list
