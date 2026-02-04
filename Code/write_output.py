import os

def write_brute_force_part(input_filename, max_duration, max_budget, brute_force_activity_order, brute_force_time):
    f = open(f"{os.getcwd}/output.txt", "a")
    f.write("========================================\nEVENT PLANNER - RESULTS\n========================================\n")
    f.write(f"\n\nInput File: {input_filename}")
    f.write(f"\nAvailable Time: {max_duration} hours")
    f.write(f"Available Budget: £{max_budget}")
    f.write("\n--- BRUTE FORCE ALGORITHM ---")
    f.write("\nSelected Activities:")
    total_enjoyment = 0
    total_time_used = 0
    total_cost = 0
    for dict in brute_force_activity_order:
        f.write(f"\n  - {dict["name"]} ({dict["duration"]} hours, £{dict["cost"]}, enjoyment {dict["enjoyment"]})")
        total_enjoyment += dict["enjoyment"]
        total_time_used += dict["duration"]
        total_cost += dict["cost"]
    f.write(f"\n\nTotal Enjoyment: {total_enjoyment}")
    f.write(f"\nTotal Time Used: {total_time_used}")
    f.write(f"\nTotal Cost: {total_cost}")
    f.write(f"\n\nExecution Time: {brute_force_time}")
    f.close()
    
def write_dynamic_solver_part(dynamic_solver_activity_order, dynamic_solver_time):
    f = open(f"{os.getcwd}/output.txt", "a")
    f.write("\n\n--- DYNAMIC PROGRAMMING ALGORITHM ---")
    f.write("\nSelected Activities:")
    total_enjoyment = 0
    total_time_used = 0
    total_cost = 0
    for dict in dynamic_solver_activity_order:
        f.write(f"\n  - {dict["name"]} ({dict["duration"]} hours, £{dict["cost"]}, enjoyment {dict["enjoyment"]})")
        total_enjoyment += dict["enjoyment"]
        total_time_used += dict["duration"]
        total_cost += dict["cost"]
    f.write(f"\n\nTotal Enjoyment: {total_enjoyment}")
    f.write(f"\nTotal Time Used: {total_time_used}")
    f.write(f"\nTotal Cost: {total_cost}")
    f.write(f"\n\nExecution Time: {dynamic_solver_time}")
    f.write(f"\n\n========================================")
    f.close()
