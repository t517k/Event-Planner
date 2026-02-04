'''
Contains the `brute_force` function for finding the optimal arrangement of activites that
is within a given total budget and total duration
'''

def brute_force(activities:list, maximum_duration:int, maximum_budget:int) -> list[dict]:
    '''
    Function which takes in a list `activites` and uses a brute force algorithm
    to calculate the best arrangement of activities to maximise joy whilst remaining
    within a specified duration (`maximum_duration`)

    - `activities`: The input list of activites to loop through every arrangement of
    - `maximum_duration`: The maximum total duration of the arrangement of activities
    - `maxmimum_budget`: The maximum total cost of the arrangement of activities
    '''

    best_arrangement = []
    best_arrangement_enjoyment = 0

    # Get the length and number of arrangements of the set
    activities_length = len(activities)

    arrangement_count = 2**activities_length

    # Loop over every possible arrangement of the set
    for i in range(arrangement_count):
        # Get the binary representation of the current index
        # (Also removes the '0b' string from the start using splicing)
        bin_rep = bin(i)[2:]
        # Pad the string with '0' on the left until the length is activities_length
        bin_rep = bin_rep.rjust(activities_length, "0")

        # Convert the binary string to a list of the bits
        binary_list = list(bin_rep)

        # current_arrangement will be used to store
        # the indexes unique arrangement
        current_arrangement = []

        current_arrangement_joy = 0
        current_arrangment_duration = 0

        # Loop through the bits of the binary representation
        for item, char in zip(activities, binary_list):
            # If the bit is 1 then add the activity to the current arrangement
            # and add the activities's enjoymenet to the total enjoymenet
            if char == "1":
                current_arrangement.append(item)

                current_arrangement_joy += item["enjoyment"]
                current_arrangment_duration += item["duration"]

        # Check the arrangement is within the maximum time frame
        if current_arrangment_duration > maximum_duration:
            continue

        # Check if the current arrangement if better than the saved best
        # and if so then update the best arrangement
        if current_arrangement_joy > best_arrangement_enjoyment:
            best_arrangement = current_arrangement
            best_arrangement_enjoyment = current_arrangement_joy

    # Return the best arrangment of activites for maximising enjoyment
    return best_arrangement


