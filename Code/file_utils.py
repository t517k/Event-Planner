'''
Contains the `get_activities_from_file` function for loading activities from a given file
'''

def get_activities_from_file(file_loc:str) -> list[dict]:
    '''
    Takes in a file location (`file_log`) and returns a list of dictionaries
    representing the activities stored in the file
    
    - `file_loc`: A string representing the location of the file
    '''

    # activities will store the loaded activites as a list
    activities = []

    # Open the specified file
    with open(file_loc, "r", encoding="utf-8") as f:

        # Get the number of activities in the file (first line)
        activities_count = int(f.readline())

        # Get the maxmimum duration and budget for the event
        # (They are on the same line seperated by a space)
        max_duration, budget = f.readline().split(" ")

        # Convert the max_duration and budget to integers
        max_duration = int(max_duration)
        budget = int (budget)

        # Load all the activities in the file
        for _ in range(activities_count):

            # Load the name, duration, cost and enjoyment of the activity
            # (They are all on the same line seperated by a space)
            name, duration, cost, enjoyment = f.readline().split(" ")

            # Convert the duration, cost and enjoyment to integers
            duration = int(duration)
            cost = int(cost)
            enjoyment = int(enjoyment)

            # Add new activity to the activities list
            activities.append({
                "name": name,
                "duration": duration,
                "cost": cost,
                "enjoyment": enjoyment
            })

    # Return the maxmimum duration, maximum budget and list of activities
    return max_duration, budget, activities
