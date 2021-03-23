import time
import random
import requests
from datetime import datetime

def is_new_week(ts, cookie):
    headers = {}
    params = {}

    host = "reservation.42network.org"
    url = "api/me/events"
    headers['Cookie'] = cookie
    params['begin_at'] = ts[0]
    params['end_at'] = ts[1]

    # params['begin_at'] = 1616367600   # Exists slots case #
    # params['end_at'] = 1617573600     #                   #

    try:
        response = requests.get(f"https://{host}/{url}",
                                headers=headers,
                                params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # f = open("response.log", "w")             # Log response json #
    # f.write(str(json.dumps(response.json()))) # content in a file #

    # Production-destinated condition
    # if (response.json() == []):
    #     return (False)
    # else:
    #     return (True)

    # Simulate real cases
    return (bool(random.randint(0, 42) % 2)) 

def get_cookie():
    f = open("cookie.txt", "r")
    return (f.readline())

def loop_check(ts, cookie):
    print("Enter in loop check")
    print("Start = " + str(ts[0]) + " -> " + str(datetime.fromtimestamp(ts[0])))
    print("End = " + str(ts[1]) + " -> " + str(datetime.fromtimestamp(ts[1])))
    while (is_new_week(ts, cookie) != True):
        time.sleep(1)
    print("Exit loop check\n")
    pass
