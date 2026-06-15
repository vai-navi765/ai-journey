with open("sample.txt", "r") as file:
    content = file.read()
content = content.lower()
words = content.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
for word in word_count:
    print(word + " : " + str(word_count[word]))