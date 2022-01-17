# TI-Basic to Python
# Created by Alex Watson and Elijah Rosen
from os import system


screen = ["", "", "", "", "", "", "", ""]
spacing_option = ["", " ", "\u2004\u2006"]
spacing_choice = 1


def test_screen():
    global screen
    for i in range(8):
        screen[i] = "AAAAAAAAAAAAAAAA"


def print_screen():
    for line in screen:
        output_line = ''
        for char in line:
            output_line += char + spacing_option[spacing_choice]
        print(output_line)


def main():
    system('cls')
    global spacing_choice
    spacing_choice = int(input("What is your preferred spacing?\n"
                               "(0 for none\n"
                               "1 for full\n"
                               "2 for unicode): "))
    system('cls')
    test_screen()
    print_screen()


if __name__ == "__main__":
    main()
