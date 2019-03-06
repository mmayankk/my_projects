# CS1010X --- Programming Methodology
#
# Mission 7 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import datetime
import csv

###############
# Pre-defined #
###############

def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

###############
# Station ADT #
###############

def make_station(station_code, station_name):
    return (station_code, station_name)

def get_station_code(station):
    return station[0]

def get_station_name(station):
    return station[1]

test_station1 = make_station('CC2', 'Bras Basah')
test_station2 = make_station('CC3', 'Esplanade')
test_station3 = make_station('CC4', 'Promenade')


############
## Task 1 ##
############

def make_train(train_code):
    ''' Do NOT modify this function'''
    return (train_code,)

test_train = make_train('TRAIN 0-0')

#############
# Task 1a   #
#############

def get_train_code(train):
    return train[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1A
# print("## Task 1a ##")
# print(get_train_code(test_train))

# Expected Output #
# TRAIN 0-0

#############
# Task 1b   #
#############

def make_line(name, stations):
    return (name,)+stations

def get_line_name(line):
    return line[0]

def get_line_stations(line):
    return line[1:]

def get_station_by_name(line, station_name):
    for i in get_line_stations(line):
        if station_name==get_station_name(i):
            return i
    return None  
        

def get_station_by_code(line, code):
    for i in get_line_stations(line):
        if code==get_station_code(i):
            return i
    return None



# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1B
# print("## Task 1b ##")
test_line = make_line('Circle Line', ((test_station1),( test_station2), (test_station3)))
#print(get_line_name(test_line))
#print(get_line_stations(test_line))
#print(get_station_by_name(test_line, 'Bras Basah'))
#print(get_station_by_code(test_line, 'CC4'))

# Expected Output #
# Circle Line
# (('CC2', 'Bras Basah'), ('CC3', 'Esplanade'), ('CC4', 'Promenade'))
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')

#############
# Task 1c   #
#############


def make_train_position(is_moving, from_station, to_station):
    return (is_moving, from_station, to_station)

def get_is_moving(train_position):
    return train_position[0]

def get_direction(line, train_position):
    for i in get_line_stations(line) :
        if i==train_position[1]:
            return 0
        if i==train_position[2]:
            return 1

def get_stopped_station(train_position):
    if get_is_moving(train_position):
        return None
    else:
        return train_position[1]

def get_previous_station(train_position):
    if get_is_moving(train_position):
        return train_position[1]
    else:
        return None

def get_next_station(train_position):
    return train_position[2]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1C
# print("## Task 1c ##")
test_train_position1 = make_train_position(False, test_station1, test_station2)
test_train_position2 = make_train_position(True, test_station3, test_station2)
#print(get_is_moving(test_train_position2))
#print(get_direction(test_line, test_train_position1))
#print(get_stopped_station(test_train_position1))
#print(get_previous_station(test_train_position2))
#print(get_next_station(test_train_position2))

# Expected Output #
# True
# 0
# ('CC2', 'Bras Basah')
# ('CC4', 'Promenade')
# ('CC3', 'Esplanade')

#############
# Task 1d   #
#############

def make_schedule_event(train, train_position, time):
    return (train, train_position, time)

def get_train(schedule_event):
    return schedule_event[0]

def get_train_position(schedule_event):
        return schedule_event[1]

def get_schedule_time(schedule_event):
    return schedule_event[2]


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 1D
# print("## Task 1d ##")
test_bd_event1 = make_schedule_event(test_train, test_train_position2, datetime.datetime(2016, 1, 1, 9, 27))
test_bd_event2 = make_schedule_event(test_train, test_train_position1, datetime.datetime(2016, 1, 1, 2, 25))
#print(get_train(test_bd_event1))
#print(get_train_position(test_bd_event1))
#print(get_schedule_time(test_bd_event1))

# Expected Output #
# ('TRAIN 0-0',)
# (True, ('CC4', 'Promenade'), ('CC3', 'Esplanade'))
# 2016-01-01 09:27:00


############
## Task 2 ##
############

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

#############
# Task 2a   #
#############
def parse_lines(data_file):
    rows = read_csv(data_file)[1:]
    lines = ()
    curr_line_name = rows[0][2]
    curr_line_stations = ()
    i=0
    for row in rows:
        code, station_name, line_name = row
        if line_name == curr_line_name:
            curr_line_stations+=(make_station (code,station_name),)

        else:
            lines=lines+(make_line(rows[i-1][2],curr_line_stations),)
            curr_line_stations=(make_station (code,station_name),)
            curr_line_name=rows[i][2]
        i=i+1
    lines=lines+(make_line(rows[i-1][2],curr_line_stations),)
    return lines

LINES=parse_lines('station_info.csv')
# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2A. THIS IS NOT OPTIONAL TESTING!
#print(parse_lines('station_info.csv'))
CCL = filter(lambda line: get_line_name(line) == 'Circle Line', LINES)[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2A
# print("## Task 2a ##")
#print(get_line_stations(CCL)[5:8])

# Expected Output #
# (('CC6', 'Stadium'), ('CC7', 'Mountbatten'), ('CC8', 'Dakota'))

#############
# Task 2b   #
#############

def parse_events(data_file):
    LINES=parse_lines('station_info.csv')
    rows = read_csv(data_file)[1:]
    events = ()
    for row in rows:
        s1=()
        s2=()
        date,time = row[4],row[5]
        b=time.find(":")
        p=int(time[0:b])
        q=int(time[b+1:])
        b=date.find("/")
        m=int(date[0:b])
        d=date[b+1:].find("/")
        n=int(date[b+1:][0:d])
        o=int(date[b+1:][d+1:])
        for line in LINES:
            if get_station_by_code(line,row[2])!=None:
                s1=get_station_by_code(line,row[2])
            if get_station_by_code(line,row[3])!=None:
                s2=get_station_by_code(line,row[3])
        if row[1]=="True":
            tf=True
        else:
            tf=False
        events+=(make_schedule_event(make_train(row[0]),make_train_position(tf,s1,s2),datetime.datetime(o,n,m,p,q)),)
    return events

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 2B. THIS IS NOT OPTIONAL TESTING!
BD_EVENTS=parse_events('breakdown_events.csv')

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 2B
# print("## Task 2b ##")
#print(BD_EVENTS)[2]

# Expected Output #
# (('TRAIN 1-11',), (False, ('CC23', 'one-north'), ('CC22', 'Buona Vista')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 3 ##
############

#############
# Task 3a   #
#############
def is_valid(bd_event):
    LINES=parse_lines('station_info.csv')
    t=get_schedule_time(bd_event).hour

    if get_is_moving(get_train_position(bd_event)):
        m=get_previous_station(get_train_position(bd_event))
    else:
        m=get_stopped_station(get_train_position(bd_event))

    n=get_next_station(get_train_position(bd_event))
    for line in LINES:
        a,b,c=0,0,0
        for i in get_line_stations(line):
            if (i==m or i==n) and b==0:
                b=a
            if (i==n or i==m) and (b-a==1 or a-b==1) and (b!=0 or (a==1 and b==0)):
                c=1
                break
            a=a+1
        if(c==1):
            break

    if ((t>=7 and t<=22) or (t==23 and get_schedule_time(bd_event).minute==0)) and c==1:
        return True
    else:
        return False

def get_valid_events(bd_events):
    ''' Do NOT modify this function'''
    return filter(is_valid, bd_events)

# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 3A. THIS IS NOT OPTIONAL TESTING!
VALID_BD_EVENTS = filter(is_valid, BD_EVENTS)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3A
# print("## Task 3a ##")
# print(is_valid(test_bd_event1))
# print(is_valid(test_bd_event2))

# Expected Output #
# True
# False

#############
# Task 3b   #
#############

def get_location_id(bd_event):
    if get_is_moving(get_train_position(bd_event)):
        m=get_previous_station(get_train_position(bd_event))
        a=1
    else:
        m=get_stopped_station(get_train_position(bd_event))
        a=2
    n=get_next_station(get_train_position(bd_event))
    k=0
    for i in get_line_stations(CCL):
        if i==m and a==2:
            h=k
            return h
            
        if i==m and a==1:
            j=k+0.5
        if i==n and a==1:
            l=k+0.5
        k+=1
    m=min(j,l)
    return m
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 3B
# print("## Task 3b ##")
test_loc_id1 = get_location_id(test_bd_event1)
test_loc_id2 = get_location_id(test_bd_event2)
# print(test_loc_id1)
# print(test_loc_id2)

# Expected Output #
# 2.5
# 1

############
## Task 4 ##
############

# UNCOMMENT the following to read the entire train schedule
FULL_SCHEDULE = parse_events('train_schedule.csv')    # this will take some time to run

#############
# Task 4a   #
#############

def get_schedules_at_time(train_schedule, time):
    return filter(lambda s:((get_schedule_time(s))-time).seconds==0,train_schedule)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4A
# print("## Task 4a ##")                                                                                
test_datetime = datetime.datetime(2017, 1, 6, 6, 0)
test_schedules_at_time = get_schedules_at_time(FULL_SCHEDULE[:5], test_datetime)
# print(test_schedules_at_time[1])

# Expected Output #
# (('TRAIN 1-0',), (False, ('CC29', 'HarbourFront'), ('CC28', 'Telok Blangah')), datetime.datetime(2017, 1, 6, 6, 0))

#############
# Task 4b   #
#############

def get_schedules_near_loc_id(train_schedule, loc_id):
    return filter(lambda s:abs((get_location_id(s))-loc_id)<=0.5,train_schedule)
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4B
# print("## Task 4b ##")
test_schedules_near_loc_id = get_schedules_near_loc_id(FULL_SCHEDULE[:10], test_loc_id1)
# print(test_schedules_near_loc_id[1])

# Expected Output #
# (('TRAIN 0-0',), (True, ('CC3', 'Esplanade'), ('CC4', 'Promenade')), datetime.datetime(2017, 1, 6, 6, 5))

#############
# Task 4c   #
#############

def get_rogue_schedules(train_schedule, time, loc_id):
    t=()
    m=get_schedules_near_loc_id(train_schedule, loc_id)
    n=get_schedules_at_time(train_schedule, time)
    for i in m:
        if i in n:
            t=t+(i,)
    return t
# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 4C
# print("## Task 4c ##")
test_bd_event3 = VALID_BD_EVENTS[0]
test_loc_id3 = get_location_id(test_bd_event3)
test_datetime3 = get_schedule_time(test_bd_event3)
test_rogue_schedules = get_rogue_schedules(FULL_SCHEDULE[1000:1100], test_datetime3, test_loc_id3)
# print(test_rogue_schedules[2])

# Expected Output #
# (('TRAIN 1-11',), (True, ('CC24', 'Kent Ridge'), ('CC23', 'one-north')), datetime.datetime(2017, 1, 6, 7, 9))

############
## Task 5 ##
############

###############
# Scorer ADT  #
###############

def make_scorer():
    return {}

def blame_train(scorer, train_code):
    scorer[train_code] = scorer.get(train_code, 0) + 1
    return scorer

def get_blame_scores(scorer):
    return tuple(scorer.items())

# Use this to keep track of each train's blame score.
SCORER = make_scorer()

#############
# Task 5a   #
#############

def calculate_blame(full_schedule, valid_bd_events):
    for m in valid_bd_events:
        t=get_schedule_time(m)
        p=get_location_id(m)
        a=()
        for k in get_rogue_schedules(full_schedule, t, p):
            i = get_train(k)
            if not i in a:
                a += (i,)
        for h in a:
            blame_train(SCORER, get_train_code(h))


# UNCOMMENT THE CODE BELOW WHEN YOU ARE DONE WITH TASK 5A. THIS IS NOT OPTIONAL TESTING!
calculate_blame(FULL_SCHEDULE, VALID_BD_EVENTS)

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5A
# print("## Task 5a ##")
# print(sorted(get_blame_scores(SCORER))[7])

# Expected Answer
# ('TRAIN 0-5',2)

#############
# Task 5b   #
#############

def find_max_score(scorer):
    return max(map(lambda x:x[1],get_blame_scores ( scorer )))


# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5B
# print("## Task 5b ##")
test_max_score = find_max_score(SCORER)
# print(test_max_score)

# Expected answer
# 180

#############
# Task 5c   #
#############

# UNCOMMENT THE CODE BELOW TO VIEW ALL BLAME SCORES. THIS IS NOT OPTIONAL TESTING!
print("## Task 5c ##")
train_scores = get_blame_scores(SCORER)
print("############### Candidate rogue trains ###############")
for score in train_scores:
    print("%s: %d" % (score[0], score[1]))
print("######################################################")

''' Please type your answer into the Task 5c textbox on Coursemology '''

#############
# Task 5d   #
#############

def find_rogue_train(scorer, max_score):
    for i in get_blame_scores ( scorer ):
        if i[1]==max_score:
            return i[0]

# UNCOMMENT THE CODE BELOW TO TEST YOUR TASK 5D
# print("## Task 5d ##")
# print("Rogue Train is '%s'" % find_rogue_train(SCORER, test_max_score))

# Expected Answer
# Rogue Train is 'TRAIN 0-4'
