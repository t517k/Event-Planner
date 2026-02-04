def greedy_heuristic(activities:list, maximum_duration:int, maxmimum_budget:int) -> list[dict]:
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
        