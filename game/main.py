SCREEN_LENGTH = 90
def read_plain_text(source):
    max_length = 0
    plain_text = []
    f = open(source)
    line = f.readline()
    while line:
        if len(line) > max_length:
            max_length = len(line)
        plain_text.append(line)
        line = f.readline()
    return plain_text, max_length

def welcome_page():

    print("=" * SCREEN_LENGTH)
    welcome, max_length = read_plain_text("welcome.txt")
    for text in welcome:
        print(" " * ((SCREEN_LENGTH - max_length) // 2) + text, end="")
    print("=" * SCREEN_LENGTH)
    pass


if __name__ == "__main__":
    welcome_page()