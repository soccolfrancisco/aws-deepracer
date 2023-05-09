def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]
    #racing line
    left_lane = [2,3,4,5,6,7,8,9,10,11,11,13,14,6,17,18,51,52,53,54,55,56,57,59,59,93,94,95,96,97,98,99,100,101,115,116,117,118]
    
    center_lane = [19,20,21,22,62,63,64,49,50,101,102,103,104,111,112,113,114]
    
    right_lane = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,105,106,107,108,109,110]
    
    #Speed
    fast = [2,3,4,5,6,7,8,9,50,51,52,53,54,55,56,57,59,59,62,63,64,65,66,67,68,69,70,71,72,73,74,75,92,93,94,95,96,97,98,99,100,101,111,112,113,114,115,116,117,118]
    slow = [10,11,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,79,80,81,82,83,84,85,86,105,106,107,108,109,110]
    
    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.5:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10
        
    
    return float(reward)