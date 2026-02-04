def greedy_heuristic(activities:list, maximum_duration:int, maximum_budget:int) -> list[dict]:
    '''
    Function which takes in a list `activites` and uses a greedy heuristic to calculate 
    the best arrangement of activities to maximise joy whilst remaining within a 
    specified duration (`maximum_duration`)

    - `activities`: The input list of activites to loop through every arrangement of
    - `maximum_duration`: The maximum total duration of the arrangement of activities
    - `maxmimum_budget`: The maximum total cost of the arrangement of activities
    '''
    best_arrangement = []
    best_arrangement_enjoyment = 0

    remaining_activities = activities.copy()
    current_duration = 0
    current_budget = 0
    while current_duration < maximum_duration:
        best_ratio = 0
        best_item = None
        for item in remaining_activities:
            if (current_duration + item["duration"] <= maximum_duration
                and current_budget + item["cost"] <= maximum_budget):
                ratio = item["enjoyment"] / item["duration"]
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_item = item
                    
        if best_item is None:
            break
            
        best_arrangement.append(best_item)
        current_duration += best_item["duration"]
        current_budget += best_item["cost"]
        remaining_activities.remove(best_item)
    
    return best_arrangement

        

