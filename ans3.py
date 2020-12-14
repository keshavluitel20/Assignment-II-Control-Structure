sentence = [" The taste of liquid state of the cream is bad then in ice form.And the act of the cat is hilarious"]
list_ed = (sentence[0]. split())
anagram_list = []
for word1 in list_ed:
    for word2 in list_ed:
        if word1 != word2 and (sorted(word1) == sorted(word2)):
            anagram_list.append(word1)
print(anagram_list)