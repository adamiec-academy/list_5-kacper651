def reversed_words():
    result = []
    words = set()
    with open("words.txt", mode="r", encoding="utf-8") as file:
        for word in file:
            words.add(word.strip())
    for word in words:
        rev_word = word[::-1]
        if rev_word in words and tuple(sorted((word, rev_word))) not in result and word != rev_word:
            result.append(tuple(sorted((word, rev_word))))
    result.sort()

    return result
