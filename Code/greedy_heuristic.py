def greedy_heuristic(activities:list, maximum_duration:int, maximum_budget:int) -> list[dict]:
    '''
    Function which takes in a list `activites` and uses a greedy heuristic to calculate 
    the best arrangement of activities to maximise joy whilst remaining within a 
    specified duration (`maximum_duration`) and cost ('maximum_budget')

    - `activities`: The input list of activites to loop through every arrangement of
    - `maximum_duration`: The maximum total duration of the arrangement of activities
    - `maxmimum_budget`: The maximum total cost of the arrangement of activities
    '''
    best_arrangement = []
    best_arrangement_enjoyment = 0

    #copies a list of activities to remove them after they are used
    remaining_activities = activities.copy()
    #keep track of current duration and cost
    current_duration = 0
    current_cost= 0
    #only iterates whilst inside the time and cost budgets
    while current_duration < maximum_duration and current_cost < maximum_budget:
        best_ratio = 0
        best_item = None
        #iterates through all activities that have not been selected yet
        for item in remaining_activities:
            #checks that activity is within remaining budget
            if (current_duration + item["duration"] <= maximum_duration
                and current_cost + item["cost"] <= maximum_budget):
                #finds the ratio to determine the best enjoyment per duration and cost (duration and cost are treated equally)
                ratio = item["enjoyment"] / (item["duration"]+item["cost"])
                #makes this item the new best one if the ratio is higher
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_item = item

        #makes sure if no activities fit in timeframe there is not an error
        if best_item is None:
            break

        #adds the best item to the arrangements and increases the current duration and cost accordingly
        best_arrangement.append(best_item)
        current_duration += best_item["duration"]
        current_cost += best_item["cost"]
        #removes activity that was used from the remaining activities
        remaining_activities.remove(best_item)
    
    return best_arrangement

        




