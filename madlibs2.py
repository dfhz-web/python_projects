# fruits = ['apple', 'banana', 'orange']

# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")
with open("story.txt", "r") as f:
    story = f.read()


# words = []
#Unique  values when using set()
words = set()
start_of_word = -1

target_start = "<"
target_end = ">"


for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word !=-1:
        word = story[start_of_word : i + 1 ]
        # words.append(word)
        words.add(word)
        start_of_word = -1

# print(words) 

answers = {}

#you add a key , and you find the value by seeking for the key  
#answers["key"]="value"

for word in words:
    answer = input("Enter a word for  "+ word + ": "   )
    answers[word] = answer

#print(answers)

for word in words:
   story =  story.replace(word, answers[word])

print(story)