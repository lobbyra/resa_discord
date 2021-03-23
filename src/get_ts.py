import json
from os import path
from datetime import datetime
from datetime import timedelta
from termcolor import colored

def get_curr_we_ts():
    ts = {}
    curr_mon = datetime.now()
    curr_sun = datetime.now()

    while (curr_mon.weekday() != 0):
        curr_mon -= timedelta(days=1)
    while (curr_sun.weekday() != 6):
        curr_sun += timedelta(days=1)
    ts[0] = int(curr_mon.timestamp())
    ts[1] = int(curr_sun.timestamp())
    return (ts)

def forward_week(ts):
    dt_monday = datetime.fromtimestamp(ts[0])
    dt_sunday = datetime.fromtimestamp(ts[1])

    dt_monday += (timedelta(days=1) * 7)
    dt_sunday += (timedelta(days=1) * 7)

    new_ts = {}
    new_ts[0] = int(dt_monday.timestamp())
    new_ts[1] = int(dt_sunday.timestamp())
    return (new_ts)

def is_curr_we(ts):
    ts_curr = datetime.now().timestamp()
    if (ts[0] < ts_curr and ts[1] > ts_curr):
        return (True)
    return (False)

def save_ts(ts):
    f = open("./ts.json", "w")
    f.write(json.dumps(ts))
    f.close()
    pass

def is_saved():
    b = (path.exists("./ts.json") and path.isfile('./ts.json'))
    return (b)

def get_saved_ts():
    f = open("ts.json", "r")
    file = f.read()
    json_data = json.loads(file)
    ts = {}
    ts[0] = json_data['0']
    ts[1] = json_data['1']
    return (ts)

def get_ts():
    print(colored('============================', 'blue'))
    if (is_saved() == True):
        print("ts.json exist")
        ts = get_saved_ts()
        if (is_curr_we(ts) == True):
            print("tw is not correct, updating...")
            ts = forward_week(ts)
            save_ts(ts)
            print("Saved.")
    else:
        print("ts.json does not exist")
        ts = get_curr_we_ts()
        ts = forward_week(ts)
        save_ts(ts)
        print("Saved in ts.json")
    print("Target week found : ")
    print("Start = " + str(ts[0]) + " -> " + str(datetime.fromtimestamp(ts[0])))
    print("End = " + str(ts[1]) + " -> " + str(datetime.fromtimestamp(ts[1])))
    print("Target week timestamps ready !")
    print(colored('============================\n', 'blue'))
    return (ts)

def forward_saved(ts):
    ts = forward_week(ts)
    save_ts(ts)
    return (ts)