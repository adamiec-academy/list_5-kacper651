def longest_word():
    longest = ""
    file = open("words.txt", mode="r", encoding="utf-8")
    for word in file:
        if len(word) > len(longest):
            longest = word

    return longest.strip()


print(len(longest_word()))
