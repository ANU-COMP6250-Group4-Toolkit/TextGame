SCREEN_LENGTH = 90
SCENARIO_DICT = {}
OPTIONS_DICT = {}
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
            SCENARIO_DICT[id] = [line.split(" // ")[1].replace("\n", "")]
        except:
            SCENARIO_DICT[id].append(line.split(" // ")[1].replace("\n", ""))
        line = f.readline()
    pass

def init_option_jump_link(source):
    if DEBUG: print("===[ init_option_jump_link ]===")
    f = open(source, encoding='utf-8')
    line = f.readline()
    while line:
        id_strings = line.split(" ")
        id = int(id_strings[0])
        # * case
        if id_strings[1] == "*":
            OPTIONS_DICT[(id, -1)] = int(id_strings[2])
        else:
            OPTIONS_DICT[(id, int(id_strings[1]))] = int(id_strings[2])
        line = f.readline()
    return


def end_game():
    pass


def start_game():
    if DEBUG: print("===[ start_game ]===")
    init_scenario_file("scenario.txt")
    init_option_jump_link("options.txt")

    question_id = 0
    while question_id != -1:
        for line in SCENARIO_DICT[question_id]:
            print(line)
        select = input("We choose: ")
        if (question_id, -1) in OPTIONS_DICT.keys():
            question_id = OPTIONS_DICT[(question_id, -1)]
        elif (question_id, select) in OPTIONS_DICT.keys():
            question_id = OPTIONS_DICT[(question_id, select)]
        else:
            question_id = -1
    
    end_game()
    pass


if __name__ == "__main__":
    action = welcome_page()
    if action == "1":
        start_game()