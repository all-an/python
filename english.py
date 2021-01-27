word = "Butterscotch"

def game():
    attempt = input("Manteiga de Caramelo: ")
    if attempt == word:
        print("Congratulations!")
    else:
        print("Wrong, correct is Butterscotch")
        game()

game()
