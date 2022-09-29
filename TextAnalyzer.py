
# Input from the user (text & letters)
question_1 = input("Introduce a Text: ").lower()
question_2 = input("Introduce 3 letters: ".lower())

# Transforming Letter to a List.
list_of_the_letters = list(question_2)

# 1 - How many times appears the letters that the user said on the text.

letter_1 = list_of_the_letters[0]
letter_2 = list_of_the_letters[1]
letter_3 = list_of_the_letters[2]

times_appear_letter1 = question_1.count(letter_1)
times_appear_letter2 = question_1.count(letter_2)
times_appear_letter3 = question_1.count(letter_3)

print(f"La letra {letter_1} aparece {times_appear_letter1} veces.")
print(f"La letra {letter_2} aparece {times_appear_letter2} veces.")
print(f"La letra {letter_3} aparece {times_appear_letter3} veces.")

# 2 - How many words does have the text.

split = question_1.split()
words_text = len(split)

print(f"Tu texto tiene: {words_text} palabras")


# 3 - The first letter and the last letter of the text
first_letters = question_1[0]
last_letters = question_1[-1]

print(f"La primera letra de tu texto es {first_letters} y la ultima es {last_letters}")

# 4 All the words in reverse order.
text_united = " ".join(question_1)
reverse = text_united[::-1]

print(f"Todo tu texto alreves se ve asi. : {reverse}")

# 5 Word 'Python' is on the text
dictionary = {True:"Si, está Python", False:"No, está Python"}
python_word = "Python" in question_1

print(f"La palabra 'Python' {dictionary[python_word]} en el texto")


