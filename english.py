word1 = "Butterscotch"
sentence1 = "The man runs into the house and hurries through the cabinets and shelves. He finds and takes out an hourglass."

def game():
    attempt = input("Manteiga de Caramelo: ")
    if attempt == word1:
        print("Congratulations!")
    else:
        print("Wrong, correct is Butterscotch")
        print("Try again !")
        game()
    attempt2 = input("O homem entra correndo na casa e vasculha com pressa os armários e estantes. Ele encontra e pega uma ampulheta.: ")
    if attempt2 == sentence1:
        print("Congratulations!")
    else:
        print("Wrong, correct is Butterscotch")
        print("Try again !")
        game()    

game()
