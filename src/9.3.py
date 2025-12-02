workers = [
    [[12, 14]],
    [[9, 12], [13, 15]],
    [[10, 14], [16, 18]]
]

events = [[time, type]
    for worker in workers
    for start, end in worker
    for time, type in [[start, 1], [end, -1]]]

events = sorted(events, key=lambda x: x[0])

# print(events)

for i in range(len(events) - 1):
    if events[i][0] == events[i+1][0] and events[i][1] > events[i+1][1]:
        events[i], events[i+1] = events[i+1], events[i]

online_time = 0
max_online_time = 0
only_one_online_time = 0


prev = 0

cur_online = 0

for event in events:
    time = event[0] - prev

    if cur_online: online_time += time
    if cur_online == len(workers): max_online_time += time
    if cur_online == 1: only_one_online_time += time

    cur_online += event[1]
    prev = event[0]


print(f"Online: {online_time-1}h")
print(f"Max online: {max_online_time}h")
print(f"Only 1 online: {only_one_online_time}h")
