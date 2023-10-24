class Story:
    def __init__(self, story_code):
        self.content = open("Stories/" + story_code + ".txt", "r", encoding='utf-8').read()

    def tell(self):
        # split the content into lines
        lines = self.content.split("\n")
        # print the lines one by one, when user press enter, print the next line
        for line in lines:
            print(line)
            input()


def getChoice():
    while True:
        choice = input("Your choice: ")
        if choice == "1" or choice == "2" or choice == "3":
            return choice
        else:
            print("Invalid choice, please try again.")


def show_title():
    pass


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
    tell_story = Story("0")

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
