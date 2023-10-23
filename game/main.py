SCREEN_LENGTH = 90
def read_plain_text(source):
    max_length = 0
    plain_text = []
    f = open(source)
    line = f.readline()
    while line:
        if len(line) > max_length:
            max_length = len(line)
        plain_text.append(line.replace("\n", ""))
        line = f.readline()
    return plain_text, max_length

def welcome_page():

    print(" ╭" + "─" * (SCREEN_LENGTH - 2) + "╮ ")
    welcome, max_length = read_plain_text("welcome.txt")
    for text in welcome:
        output = " │" + " " * (SCREEN_LENGTH - 4) + "┃ "
        to_middle_space = (SCREEN_LENGTH - max_length - 4) // 2
        output = output[: 2 + to_middle_space] + text + output[to_middle_space + len(text):]
        print(output)
    print(" ╰" + "━" * (SCREEN_LENGTH - 2) + "╯ ")
    return input("Number: ")


def start_game():
    pass


if __name__ == "__main__":
    action = welcome_page()
    if action == "1":
        start_game()