'''
Where the brute force and dynamic programming approaches for finding the optimal 
arrangement of activities based on duration, cost and enjoyment are tested
against each other to compare performance and correctness
'''

# Import os for dealing with file paths
import os

# Import time for recording the speed of
# the brute force and dynamic programming approaches
import time

# Import the brute_force function from the brute_force module
from brute_force import brute_force

# Import the dynamic_solver function from the dynamic_solver module
from dynamic_solver import dynamic_solver

# Import the get_activities_from_file function from the file_utils module
from file_utils import get_activities_from_file


if __name__ == "__main__":
    # Get the location of the project directory
    CURRENT_DIR = os.getcwd()
    # FILE_LOC represents the global location of the file containing the list of activities
    FILE_LOC = f"{CURRENT_DIR}/Input_Files/input_medium.txt"

    # Get the maximum duration, budget and list of activities from the file
    max_duration, max_budget, activities_list = get_activities_from_file(FILE_LOC)

    # Record the current time in ms before running the brute force function
    start_time_ms = time.perf_counter() * 1000

    # Locate the best arrangement of activities for maxmimising
    # enjoyment using a brute force algorithm
    brute_force_activity_order = brute_force(activities_list, max_duration, max_budget)

    # Record the current time in ms after running the brute force function
    end_time_ms = time.perf_counter() * 1000

    # Calculate the time the brute force approach took in milliseconds
    brute_force_time = end_time_ms - start_time_ms

    print(f"Brute force took: {brute_force_time}ms")
    # Output the brute force best arrangement of activities
    print(brute_force_activity_order)

    # Record the current time in ms before running the dynamic solver function
    start_time_ms = time.perf_counter() * 1000

    # Locate the best arrangement of activities for maxmimising
    # enjoyment using the dynamic solver algorithm
    dynamic_solver_activity_order = dynamic_solver(activities_list, max_duration, max_budget)

    # Record the current time in ms after running the dynamic solver function
    end_time_ms = time.perf_counter() * 1000

    # Calculate the time the dynamic programming approach took in milliseconds
    dynamic_solver_time = end_time_ms - start_time_ms

    print(f"Dynamic solver took: {dynamic_solver_time}ms")
    # Reverse the order of the arrangement to match brute forces output
    print(dynamic_solver_activity_order[::-1])
