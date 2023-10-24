from Game import updateStatus

# test all paths of updateStatus()

def test_updateStatus():
    # Initial values
    collaboration = 0
    skill = 0
    confidence = 0

    days = ["1", "2", "3", "4", "5.txt"]

    # Initialize a list for choices
    choices = ["1", "2", "3"]

    # Initialize current values
    current_collaboration = collaboration
    current_skill = skill
    current_confidence = confidence

    # List to store all sums
    all_sums = []

    # Walk through days 1 to 5.txt
    for day1_choice in choices:
        for day2_choice in choices:
            for day3_choice in choices:
                for day4_choice in choices:
                    for day5_choice in choices:
                        day_choices = [day1_choice, day2_choice, day3_choice, day4_choice, day5_choice]

                        # Reset for each 5.txt-day path
                        current_collaboration, current_skill, current_confidence = collaboration, skill, confidence

                        # Apply updates for each day
                        for i, day in enumerate(days):
                            choice = day_choices[i]
                            current_collaboration, current_skill, current_confidence = updateStatus(day, choice,
                                                                                                    current_collaboration,
                                                                                                    current_skill,
                                                                                                    current_confidence)

                        # Calculate the sum for this path and store it
                        sum_values = current_collaboration + current_skill + current_confidence
                        all_sums.append(sum_values)

    # Print the range (min and max) of sums
    print(f"Range of sums: ({min(all_sums)}, {max(all_sums)})")


# Run the test
test_updateStatus()