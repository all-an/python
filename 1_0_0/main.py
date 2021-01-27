import fork
import guess

def play_main():
    print("----choose your game----")

    print("(1) Fork, (2) Guess the Number")

    game = int(input("Which Game ?"))

    if game == 1:
        print("Playing fork")
        fork.play_fork()
    elif game == 2:
        print("Playing Guess the Number")
        guess.play_guess()

if __name__ == "__main__":
    play_main()
