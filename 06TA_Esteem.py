score = 0

def main():
    score = 0
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly")
    print("apply to yourself. Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.")
    print()

    question_positive = input("1) I feel that I am a person of worth, at least on an equal plane with others: ")
    score += give_positive(question_positive)
    question_positive = input("2) I feel that I have a number of good qualities: ")
    score += give_positive(question_positive)
    question_negative = input("3) All in all, I am inclined to feel that I am a failure: ")
    score += give_negative(question_negative)
    question_positive = input("4) I am able to do things as well as most other people:  ")
    score += give_positive(question_positive)
    question_negative = input("5) I feel I do not have much to be proud of:  ")
    score += give_negative(question_negative)
    question_positive = input("6) I take a positive attitude toward myself:  ")
    score += give_positive(question_positive)
    question_positive = input("7) On the whole, I am satisfied with myself:  ")
    score += give_positive(question_positive)
    question_negative = input("8) I wish I could have more respect for myself:  ")
    score += give_negative(question_negative)
    question_negative = input("9) I certainly feel useless at times: ")
    score += give_negative(question_negative)
    question_negative = input("10) At times I think I am no good at all. ")
    score += give_negative(question_negative)
    result = give_result(score)
    print()
    print(score)
    print(result)

def give_positive(question_positive): 
    if question_positive == "D":
        score = 0
    elif question_positive == "d":
        score = 1
    elif question_positive == "a":
        score = 2
    elif question_positive == "A":
        score = 3

    return score

def give_negative(question_negative):
    if question_negative == "D":
        score = 3
    elif question_negative == "d":
        score = 2
    elif question_negative == "a":
        score = 1
    elif question_negative == "A":
        score = 0

    return score


def give_result(score):
    print("A score below 15 may indicate problematic low self-esteem.")
    if score > 15:
        print("You are good")
    else:
        print("Go to see a doctor")

    main()
