import queue

t = int(input())
for i in range(t):
    test_case = eval(input())
    size = len(test_case)
    rooms = [0] * size
    Queue = queue.Queue()
    rooms[0] = 1
    for key in test_case[0]:
        Queue.put(key)
    print('After entry into room number 0 : ' + str(rooms))
    print(list(Queue.queue))
    while not Queue.empty():
        room_number = Queue.get()
        print('Room number = ' + str(room_number))
        if room_number < size:
            rooms[room_number] = 1
            for key in test_case[room_number]:
                if key < size:
                    if rooms[key] == 0:
                        Queue.put(key)
    print(rooms)
    print(rooms == [1] * size)
