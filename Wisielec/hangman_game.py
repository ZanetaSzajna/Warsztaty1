import random

word_list=["apart","apartment","apple", "auto","available", 'average','avoid','award', 'bag','bake','balance','ball','ban','band','bank','bar','barely','barrel',
           'barrier','base','birthday', "body",'bottom','boundary','bowl','box','boy','boyfriend','brain','branch','brand','bread','break',
           'breakfast','capable','capacity','capital','captain','capture','car','carbon','card','care','career','careful','carefully','carrier',
           'carry','case','cash','cast','cat','catch','category','cheese','chef','chemical','chest','chicken','despite','destroy','destruction',
           'detail','detailed','detect','determine','develop','dominate','door','double','doubt','down','downtown','dozen','draft','drag',
           'drama','dramatic','easy','eat','economics','economy','edge','edition','editor','educate','garage','garden','garlic','holiday',
           'holy','home','homeless','honest','honey','onion','online','only','onto','open','palm','pan','panel','pant','paper','parent'
           'park','parking','party','piano','pick','picture','pie','piece','pile','sing','singer','single','sink','sir','sister','sit',
           'site','situation','yellow','yes','yesterday','yet','you','young','woman','wonder','wonderful','wood']

# wybiernie hasła
keyword = random.choice(word_list)

# ukrycie hasła

gues_word=list(keyword)

for i in range(len(keyword)):
    gues_word[i]="_"
print(keyword)
# gra

def hangmman_game():
    # określenie liczby rund
    round= 10

    while round > 0:
        print("")
        # poinformowanie gracza  o ilości rund
        print(f" You have {round} rounds to guess the password")
        print(" ")
        #  wyświetenie zaszyfrowaneh=go hasłą
        print(" ".join(gues_word))
        # podanie przez użytkownaika litery
        user_letter= input("Enter yor letter --> ")
        #  sprawdzenie czy podana litera jest w haśle
        if user_letter in keyword:
            for letter in range(len(keyword)):
                if keyword[letter] == user_letter:
                    print("congratulations you have successfully guessed the letter ")
                    gues_word[letter] = user_letter

            if "".join(map(str, gues_word)) == keyword:
                print("You win !!!!!!!!!!!!!!!!")
                break;
        # jeżeli nie odejmujemy jedą roundę
        else:
            round -= 1
            print(f"Sorry, {user_letter} is not in the keyword. Try Again ")
        #  wyświetenie zaszyfrowaneh=go hasłą
        print(" ".join(gues_word))
        #Pytaniie czy użytkownik chce odgadąć całe hasło
        question = input("Would you like to guess the word ? Yes/No -->  ")
        #Jezeli tak  to sprawdzamy czy to prawidłowe słowo
        if question == "Yes" or question == "yes":
            user_word = input("Enter word --> ")
            if user_word == keyword:
                    print("You win !!!!!!!!!!!!!!!!")
                    break;
            # jeżeli nie zgadnie hasła wracamy do gry ale tracimy jedną szansę
            else:
                round-= 1
                print("Oh no,  it is not this word, Try Again ")

hangmman_game()