import time

def print_like_chatgpt(text, delay=0.01):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()  # print a newline at the end

# read text from file
text = open("Stories/1-Introduction.txt", "r", encoding='utf-8').read()

print_like_chatgpt(text)
