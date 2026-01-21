'''
Docstring for Code.event_planner
'''

# Import os for dealing with file paths
import os

# Import time for recording the speed of
# the brute force and dynamic programming approaches
import time

# Import the brute_force function from the brute_force module
from brute_force import brute_force

# Import the get_activities_from_file function from the file_utils module
from file_utils import get_activities_from_file


if __name__ == "__main__":
    # Get the location of the project directory
    CURRENT_DIR = os.getcwd()
    # FILE_LOC represents the global location of the file containing the list of activities
    FILE_LOC = f"{CURRENT_DIR}/Input_Files/input_large.txt"

    # Get the maximum duration, budget and list of activities from the file
    max_duration, max_budget, activities_list = get_activities_from_file(FILE_LOC)

    # Record the current time in ms before running the brute force function
    start_time_ms = time.time() * 1000

    # Locate the best arrangement of activities for maxmimising
    # enjoyment using a brute force algorithm
    best_activity_order = brute_force(activities_list, max_duration, max_budget)

    # Record the current time in ms after running the brute force function
    end_time_ms = time.time() * 1000

    # Calculate the time the brute force approach took in milliseconds
    brute_force_time = end_time_ms - start_time_ms

    print(f"Brute force took: {brute_force_time}ms")

    print(best_activity_order)
