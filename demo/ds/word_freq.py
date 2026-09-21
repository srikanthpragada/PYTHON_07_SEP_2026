st = "How do   you do today? How did    you do   yesterday?"

words = st.split(" ")

used_words = []
for word in words:
    if word not in used_words and len(word) > 0:
        print(f"{word:10}  {words.count(word)}")
        used_words.append(word)

