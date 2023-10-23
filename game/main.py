SCREEN_LENGTH = 90
SCENARIO_DICT = {}
DEBUG = True
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


def init_scenario_file(source):
    if DEBUG: print("===[ init_scenario_file ]===")
    f = open(source, encoding='utf-8')
    line = f.readline()
    while line:
        # get question id
        try:
            id = int(line.split(" // ")[0])
            SCENARIO_DICT[id] = [line.split(" // ")[1]]
        except:
            SCENARIO_DICT[id].append(line.split(" // ")[1])
    return


def start_game():
    if DEBUG: print("===[ start_game ]===")
    init_scenario_file("scenario.txt")
    question_id = 0
    while question_id != -1:
        for line in SCENARIO_DICT[question_id]:
            print(line)
        select = input("We choose: ")
    pass


if __name__ == "__main__":
    action = welcome_page()
    if action == "1":
        start_game()