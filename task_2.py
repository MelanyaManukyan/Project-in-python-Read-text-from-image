def file_reader(file_name: str):
    file = open(file_name, "r")
    content = file.read()
    file.close()
    return content

dictionary = dict()
start_idx = 0
for idx, char in enumerate(text):
    if not char.isalpha():
        dictionary[start_idx:idx + 1] = 1
    start_idx = idx

def sorted_by_values(kwarg):
    return sorted(kwarg.items(), key=lambda x: x[1], reverse=True)


name = "text.txt"
text = file_reader(name)
sorted_words = count_words(text)

result = sort_by_values(sorted_words)
print(dict(result))