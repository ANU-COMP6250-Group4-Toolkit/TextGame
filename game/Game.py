isGameOver = False


def initGame():
    isGameOver = False


if __name__ == '__main__':
    # init game
    initGame()
    # run game loop
    while not isGameOver:
        if not isCurrentStoryOver():
            tellStory(currentStory)
        else:
            choice = currentStory.makeChoice()
            currentStory = currentStory.getNextStory(choice)

    # game over, print result
    outcome = calculateOutcome()
    tellStory(outcome)
