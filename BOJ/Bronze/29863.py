go_to_sleep = int(input())
wake_up = int(input())



if go_to_sleep <= wake_up:
    print(wake_up - go_to_sleep)

else:
    print((24 - go_to_sleep) + wake_up)

