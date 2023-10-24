SCREEN_LENGTH = 90

def getChoice():
    while True:
        choice = input("Your choice: ")
        if choice == "1" or choice == "2" or choice == "3":
            return choice
        else:
            print("Invalid choice, please try again.")


def read_plain_text(source):
    max_length = 0
    plain_text = []
    f = open(source, encoding='utf-8')
    line = f.readline()
    while line:
        if len(line) > max_length:
            max_length = len(line)
        plain_text.append(line.replace("\n", ""))
        line = f.readline()
    return plain_text, max_length

def show_title():
    print(" ╭" + "─" * (SCREEN_LENGTH - 2) + "╮ ")
    welcome, max_length = read_plain_text("welcome.txt")
    for text in welcome:
        output = " │" + " " * (SCREEN_LENGTH - 4) + "┃ "
        to_middle_space = (SCREEN_LENGTH - max_length - 4) // 2
        output = output[: 2 + to_middle_space] + text + output[to_middle_space + len(text):]
        print(output)
    print(" ╰" + "━" * (SCREEN_LENGTH - 2) + "╯ ")


def calculate_ending(collaboration, skill, confidence):
    pass


def show_endings():
    pass


def updateStatus(day, choice, collaboration, skill, confidence):
    pass


def tell_story(story_code):
    story = open("Stories/" + story_code + ".txt", "r", encoding='utf-8').read()
    # split the content into lines
    lines = story.split("\n")
    # print the lines one by one, when user press enter, print the next line
    for line in lines:
        print(line)
        input()


if __name__ == '__main__':
    # init
    collaboration = 0
    skill = 0
    confidence = 0

    # intro
    tell_story("0")

    # start game
    show_title()

    # loop for five days
    for i in range(5):
        # day i
        tell_story(str(i))
        choice = getChoice()
        collaboration, skill, confidence = updateStatus(str(i), choice, collaboration, skill, confidence)
        tell_story(str(i) + choice)

    # game over
    ending_code = calculate_ending(collaboration, skill, confidence)
    tell_story(ending_code)
    show_endings()
