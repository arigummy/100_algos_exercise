# temps = []

def long_rise(data):
    max_rise = 0
    cur_rise = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            cur_rise += 1 if cur_rise > 0 else 2
        else:
            if max_rise < cur_rise and cur_rise != 0:
                max_rise = cur_rise
                cur_rise = 0
    return max_rise

def get_average(data):
    sum = 0;
    for x in data:
        sum += x
    return sum / len(data)

def find_max_dev(data, average):
    d = 0
    temp = data[0]
    for x in data:
        if abs(x - average) > d:
            d = abs(x - average)
            temp = x
    return temp

def find_holes(data):
    res = []
    for i in range(1, len(data) - 1):
        if data[i] < data[i-1] and data[i] < data[i+1]: res.append(data[i])
    return res

temps = list(map(int, input().split()))

# print(long_rise(temps))

print(find_holes(temps))
