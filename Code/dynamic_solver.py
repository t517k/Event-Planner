'''
Contains the `dynamic_solver` function for finding the optimal arrangement of activites that
is within a given total budget and total duration
'''

def dynamic_solver(activities:list, maximum_duration:int, maxmimum_budget:int) -> list[dict]:
    '''
    Function which takes in a list `activites` and calculates the best arrangement 
    of activities to maximise joy whilst remaining within a specified duration (`maximum_duration`)

    - `activities`: The input list of activites
    - `maximum_duration`: The maximum total duration of the arrangement of activities
    - `maxmimum_budget`: The maximum total cost of the arrangement of activities
    '''
    # Number of activities
    activity_count = len(activities)
    # Maxmimum activity "weight"
    max_weight = maximum_duration

    mat = []

    # Setup the matrix
    for _row in range(activity_count + 1):
        activity_row = []

        # Fill the row with zeros
        for _column in range(max_weight + 1):
            activity_row.append(0)

        # Add the row to the matrix
        mat.append(activity_row)


    # Loop over the rows in the matrix
    for y, row in enumerate(mat):
        # Skip the first row
        if y == 0:
            continue

        # Get the row's focused activity
        row_activity = activities[y - 1]

        # Get the enjoyment and weight of the activity
        activity_joy = row_activity["enjoyment"]
        activity_weight = row_activity["duration"]

        # Loop through each item in the row
        for x, _ in enumerate(row):
            # The value above the current square in the matrix
            joy_above = mat[y - 1][x]
            # Offset the joy above to counter the weight of the current activity
            joy_above_weight_offset = mat[y - 1][x - activity_weight]

            # If activity's weight is too large then the best solution
            # is the joy above as its too heavy to add in currently
            if x < activity_weight:
                mat[y][x] = joy_above
            else:
                mat[y][x] = max(activity_joy + joy_above_weight_offset, joy_above)


    best_arrangement = []
    column_index = 0

    # Flip the matrix upside down (reverse order)
    rev_mat = mat[::-1]

    # Start at the top right corner (best enjoyment value) and
    # work backwards to figure out which activities should be included
    for y, row in enumerate(rev_mat):
        # Skip the last row
        if y + 1 >= len(rev_mat):
            continue

        # Reverse the order of the row so that now the best
        # enjoyment is at location (0, 0)
        reversed_row = row[::-1]
        reversed_row_above = rev_mat[y + 1][::-1]

        # Reverse the order of the activities to match the
        # reversed matrix row
        reversed_activities = activities[::-1]

        # Get the row activities "weight"
        row_activity = reversed_activities[y]
        row_weight = row_activity["duration"]

        # Get the current square's value and the square above its value
        current_value = reversed_row[column_index]
        value_above = reversed_row_above[column_index]

        # If the 2 values are different then the activity is
        # part of the best arrangement
        if not current_value == value_above:
            # Add the activity to the best_arrangement list
            best_arrangement.append(row_activity)
            # Shift the column index by the row activites weight
            column_index += row_weight

    # Return the best arrangment of activites for maximising enjoyment
    return best_arrangement

