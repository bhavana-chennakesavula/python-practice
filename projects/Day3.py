#name formatter
name = input("enter a name: ")
formatted_name = name.strip().title()
print(f"formatted name: {formatted_name}")


#word counter
sentence = input("enter a sentence: ")
word_count = len(sentence.strip().split())
print(f"total no.of words: {word_count}")
