from apiRequests import goal_map, create_polyanet
from helpers import cometh_helper, soloon_helper

def get_and_create_goal_map_matrix():
    """This function gets the goal map and calls the apis to replicate it."""

    # Get goal map response
    goal_response = goal_map()
    if("goal" not in goal_response):
        raise ValueError("missing goal map response")
    
    GOAL_MAP = goal_map()["goal"]
    
    # Iterate through goal map and create the correct objects
    for row_idx, row in enumerate(GOAL_MAP):
        for col_idx, cell in enumerate(row):
            if cell == "POLYANET":
                create_polyanet(row_idx, col_idx)
            elif "COMETH" in cell:
                cometh_helper(cell, row_idx, col_idx)
            elif "SOLOON" in cell:
                soloon_helper(cell, row_idx, col_idx)
            elif cell != "SPACE":
                print("unknown object recieved - no action taken")
    