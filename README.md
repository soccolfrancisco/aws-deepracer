# AWS DeepRacer Repository
Code used to develop and train the 1/18 scale self-driving car that competed in the AWS DeepRacer and won 4th place.

# Reward Function Template for waypoints
def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]
    #racing line
    left_lane = []
    
    center_lane = []
    
    right_lane = []
    
    #Speed
    fast = []
    slow = []
    
    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] >= 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10
        
    
    return float(reward)
    
    # AWS DeepRacer
    https://aws.amazon.com/en/deepracer/
