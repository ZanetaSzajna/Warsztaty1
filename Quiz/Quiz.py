import random

question={ "What is the capital of Hungary?" : "B",
           "Which country produces the most coffee in the world?":"C",
           "What is the smallest planet in our solar system?":"A",
           "What is the smallest country in the world?":"C",
           "In which US state is the Grand Canyon located?":"D",
           "What is the capital of Sweden?":"B",
           "What is the largest country in South America?":"D",
           "What is the capital of Australia?":"A",
           "What is the largest country in Africa?":"C",
           "What is the most populous city in the United States? ":"D",
           "What is the chemical symbol for gold?":"B",
           "What is the fastest land animal?":"A",
           "What is the capital of Canada?":"C",
           "What is the national sport of Japan?":"D",
           "Which country is the land of the kiwi?":"B",
           "What is the capital of Italy?":"C",
           "Which element is represented by the chemical symbol “Na”?":"A",
           "Which country is known for inventing the sauna?":"B",
           "Which country has the most time zones?":"D",
           "What is the world’s second-largest country by land area?":"C",
           "What is the capital of Turkey?":"A",
           "Which country is known for inventing the pizza?":"B",
}

options = [ ["A. Roma", "B. Budapest", "C. Warsaw", "D. Riga"],
            ["A. Romania", "B. USA", "C. Brazil", "D. Australia"],
            ["A. Mercury", "B. Wenus", "C. Mars", "D. Earth"],
            ["A. Andora", "B. Giblartar", "C. Vatican", "D. San Marino"],
            ["A. California", "B. Utah", "C. New York", "D. Arizona"],
            ["A. Oslo", "B. Stockholm", "C. Malmo", "D. Goteborg"],
            ["A. Argentina", "B. Colombia", "C. Uruguay", "D. Brazil"],
            ["A. Canberra", "B. Sydney", "C. Melbourne", "D. Perth"],
            ["A. Egypt", "B. Morocco", "C. Algeria", "D. Congo"],
            ["A. Los Angeles", "B. Miami", "C. San Francisco", "D. New York"],
            ["A. Gl", "B. Au", "C. Na", "D. Cl"],
            ["A. Cheetah", "B. Lion", "C. Tiger", "D. Rhino"],
            ["A. Toronto", "B. Montreal", "C. Ottawa", "D. Vancouver"],
            ["A. Karate", "B. Judo", "C.Kung-Fu", "D.Sumo"],
            ["A. Indonesia", "B.New Zeland", "C.Thailand", "D. Philipines"],
            ["A. Naples", "B. Torino", "C. Rome", "D. Milan"],
            ["A. Sodium", "B. Gold", "C.Helium", "D. Copper"],
            ["A. Norway", "B. Finland", "C. Sweden", "D. Iceland"],
            ["A. USA", "B. Russia", "C. China", "D. France"],
            ["A. Russia", "B. USA", "C. Canada", "D. Australia"],
            ["A. Ankara", "B. Istanbul", "C. Antalya", "D.Bursa"],
            ["A. Greece", "B. Italy", "C. Albania", "D. Croatia"]]

list_question= list(question.keys())
print(list_question)

def new_game():
    round=5
    list_corect_answer=[] # lista poprawnych odpowiedzi do wylosowanych pytań
    list_user_answer =[]  #lista odpowiedzi użytkownika
    user_correct_answer=0  #punkty uzytjownika
    question_number=1      #numer pytania
    for i in range(round):
        random_question=random.choice(list_question)  #losowanie pytań
        print(random_question)   #wyswietlenie losowego pytania

        for option in options[list_question.index(random_question)]:
            print(option)  # wyświetlenie wariantów odpowiedzi
        user_answer=(input("Enter (A,B,C,D): ")).upper()      # wybór użytkownika
        list_user_answer.append(user_answer)                  # dodanie do listy wszystkich odpowiedzi użytkownika
        answer=(question.get(random_question))                # prawidłowa odpowiedź
        list_corect_answer.append(answer)                     # dodanie do listy odpowiedzi poprawnych
        user_correct_answer+=check_answer(answer, user_answer) # funkcja sprawdzająca poprawność
        question_number+=1
    display_score(list_corect_answer,list_user_answer, user_correct_answer)
def check_answer(answer, user_answer):
    if str(answer) == (user_answer):
        #print("CORRECT")
        return 1
    else:
        #print("WRONG")
        return 0
def display_score(list_corect_answer,list_user_answer, user_correct_answer ):
    print("****************************************")
    print("Result")
    print("*****************************************")

    print("Your Answer ", end=" ")
    for i in list_user_answer:
        print(i, end=" ")
    print()

    print("Correct Answer ", end=" ")
    for i in list_corect_answer:
        print(i, end=" ")
    print()

    score = (user_correct_answer/len(list_corect_answer))*100
    print(f"Yor score is: {str(score)} %")

def play_again():
    response = (input("Do you want try again ? ( yes or no )---> ")).lower()
    if response == "yes":
        return True
    else:
        return False

new_game()

while play_again():
    new_game()
print("Thank you for playing, see you later ")




