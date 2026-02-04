def greedy_heuristic(activities:list, maximum_duration:int, maxmimum_budget:int) -> list[dict]:
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

    # Get the length and number of arrangements of the set
    activities_length = len(activities)

    current_duration = 0
    while current_duration < maximum_duration:
        best_ratio = 0
        best_item = None
        for item in activities:
            current_ratio = item["enjoyment"]/item["duration"]
            current_duration += item["duration"]
            if current_ratio > best_ratio and current_duration <= maximum_duration:
                best_ratio = current_ratio
                best_item = item
                current_duration += item["duration"]
            current_duration -= item["duration"]
        best_arrangement.append(best_item)
        best_arrangement_enjoyment += best_item["enjoyment"]
    
    return best_arrangement

        
