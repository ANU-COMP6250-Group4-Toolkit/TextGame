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


def show_interacting_window(fileName):
    print(" ╭" + "─" * (SCREEN_LENGTH - 2) + "╮ ")
    texts, max_length = read_plain_text(fileName)
    for text in texts:
        output = " │" + " " * (SCREEN_LENGTH - 4) + "┃ "
        to_middle_space = (SCREEN_LENGTH - max_length - 4) // 2
        output = output[: 2 + to_middle_space] + text + output[to_middle_space + len(text):]
        print(output)
    print(" ╰" + "━" * (SCREEN_LENGTH - 2) + "╯ ")
    return getChoice()


def calculate_ending(collaboration, skill, confidence):
    num = collaboration + skill + confidence
    if num == 8:
        return "ending1"
    elif num == 9:
        return "ending2"
    elif num == 10:
        return "ending3"
    elif num == 11:
        return "ending4"


def show_endings():
    pass


def updateStatus(day, choice, collaboration, skill, confidence):
    # day 1
    if day == "1":
        if choice == "1":
            collaboration += 1
            skill += 2
            confidence += -1
            return collaboration, skill, confidence
        elif choice == "2":
            collaboration += 2
            skill += -1
            confidence += 2
            return collaboration, skill, confidence
        elif choice == "3":
            collaboration += 2
            skill += 0
            confidence += 1
            return collaboration, skill, confidence
    # day 2
    elif day == "2":
        return collaboration, skill, confidence
    # day 3
    elif day == "3":
        if choice == "1":
            collaboration += 3
            skill += -1
            confidence += 1
            return collaboration, skill, confidence
        elif choice == "2":
            collaboration += 0
            skill += 3
            confidence += 0
            return collaboration, skill, confidence
        elif choice == "3":
            collaboration += -1
            skill += 2
            confidence += 1
            return collaboration, skill, confidence
    # day 4
    elif day == "4":
        return collaboration, skill, confidence
    # day 5
    elif day == "5":
        if choice == "1":
            collaboration += 1
            skill += 3
            confidence += 0
            return collaboration, skill, confidence
        elif choice == "2":
            collaboration += 3
            skill += 0
            confidence += 2
            return collaboration, skill, confidence
        elif choice == "3":
            collaboration += 2
            skill += 0
            confidence += 3
            return collaboration, skill, confidence


def tell_story(story_code):
    story = open("Stories/" + story_code + ".txt", "r", encoding='utf-8').read()
    # split the content into lines
    lines = story.split("\n")
    # print the lines one by one, when user press enter, print the next line
    for line in lines:
        print(line)
        input()


def run_game():
    # init
    collaboration = 0
    skill = 0
    confidence = 0

    # intro
    tell_story("0")

    # loop for five days
    for i in range(5):
        # day i
        tell_story(str(i+1))
        choice = show_interacting_window("Stories/" + str(i+1) + "-choices.txt")
        # collaboration, skill, confidence = updateStatus(str(i+1), choice, collaboration, skill, confidence)
        tell_story(str(i+1) + "-" + choice)

    # game over
    ending_code = calculate_ending(collaboration, skill, confidence)
    tell_story(ending_code)
    show_endings()


if __name__ == '__main__':
    # start game
    code = show_interacting_window("welcome.txt")

    if code == "1":
        run_game()
