word = "Butterscotch"

def game():
    attempt = input("Manteiga de Caramelo: ")
    if attempt == word:
        print("Congratulations!")
    else:
        print("Wrong, correct is Butterscotch")
        print("Try again!")
        game()

game()
