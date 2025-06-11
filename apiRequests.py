import requests
import time

BASE_URL = "https://challenge.crossmint.io/api"
CANDIDATE_ID = "544783d6-d06d-4a49-af04-0cbf684476fb" 

def post_object(endpoint, payload, object_type, row, column, max_retries=3):
    """Sends POST API requests. Retries on failure with backoff."""

    attempt = 0
    delay = 2
    while attempt < max_retries:
        try:
            response = requests.post(f"{BASE_URL}/{endpoint}", json=payload)
            response.raise_for_status()
            print(f"created {object_type.upper()} at ({row}, {column})")
            return
        except requests.exceptions.RequestException as e:
            print(f"attempt: {attempt+1} - failed to create {object_type.upper()} at ({row}, {column}): {e}")
            attempt+=1
            if attempt < max_retries:
                time.sleep(delay)
                delay *= 2
            else:
                print(f"giving up after {max_retries} attempts")
                return


def create_polyanet(row, column):
    """Sends POST API request for POLYANET."""

    post_object("polyanets", {
        "row": row,
        "column": column,
        "candidateId": CANDIDATE_ID
    }, "polyanet", row, column)

def create_cometh(row, column, direction):
    """Sends POST API request for COMETH."""

    post_object("comeths", {
        "row": row,
        "column": column,
        "candidateId": CANDIDATE_ID,
        "direction": direction
    }, "cometh", row, column)

def create_soloon(row, column, color):
    """Sends POST API request for SOLOON."""

    post_object("soloons", {
        "row": row,
        "column": column,
        "candidateId": CANDIDATE_ID,
        "color": color
    }, "soloon", row, column)

def goal_map():
    """Sends GET API request for goal map."""

    url = f"{BASE_URL}/map/{CANDIDATE_ID}/goal"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"failed to get goal map: {e}")
        return None