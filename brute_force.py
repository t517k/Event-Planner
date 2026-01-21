'''
Docstring for main
'''

def brute_force(activities:list):
    '''
    Function which takes in a list `activites` and checks every possible
    ordering to find the best legal arrangement of activites

    `activities`: The input list of activites to loop through every arrangement of
    '''

    # Get the length and number of arrangements of the set
    activities_length = len(activities)

    # '- 2' for zero indexing and the ommision of the possibility of an empty list
    arrangement_count = 2**activities_length - 1

    # Loop over every possible arrangement of the set
    for i in range(arrangement_count):
        # Get the binary representation of the current index
        # (Also removes the '0b' string from the start)
        bin_rep = bin(i + 1)[2:]
        # Pad the string with '0' until the length is activities_length
        bin_rep = bin_rep.rjust(activities_length, "0")

        # current_arrangement will be used to store
        # the indexes unique arrangement
        current_arrangement = []

        # Loop through the bits of the binary representation
        for item, char in zip(activities, list(bin_rep)):
            # If the bit is 1 then add the item to the current arrangement
            if char == "1":
                current_arrangement.append(item)

        # Print the current_arrangement
        print(current_arrangement)


brute_force([
    {
        "name": "",
        "length": 0,
        "cost": 0,
        "enjoyment": 0
    }
])
