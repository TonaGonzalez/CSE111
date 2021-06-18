import random

def main():
    randnums = [16.2, 75.1, 52.3]


    print(randnums)

    append_random_numbers(randnums)
    print(randnums)

    append_random_numbers(randnums,5)
    print(randnums)

    randomwords = []
       
    append_random_words(randomwords,3)
    print(randomwords)



def append_random_numbers(numbers_list, quantity = 1):

    for _ in range(quantity):
        number = random.uniform(0, 100)
        rounded = round(number, 1)
        numbers_list.append(rounded)

def append_random_words(words_list, quantity = 1):
    words_list = ["table", "chair", "toy", "choose", "play", "from", "touch", "hear", "cook", "plead", "strike"]
    for _ in range(quantity):
        word = random.choice(words_list)
        words_list.append(word)
        

main()
    