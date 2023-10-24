if __name__ == '__main__':
    # run game loop
    while not isGameOver():
        if not isCurrentStoryOver():
            tellStory(currentStory)
        else:
            choice = currentStory.makeChoice()
            currentStory = currentStory.getNextStory(choice)

    # game over, print result
    outcome = calculateOutcome()
    tellStory(outcome)