def single_root_words(root_word, *other_words):
    root_word_lower = root_word.lower()
    # Создаем пустой список
    same_words = []

    for word in other_words:
        word_lower = word.lower()
        # Содержит ли одно слово в другом
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    # Возвращаем итоговый список
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)


