from time import sleep

i = 1
j = 1
while i <= 10:
    sleep(0.3)
    print('{} x {} = {}'.format(j, i, i*j))
    i += 1
    if i == 11 and j < 10:
        j += 1
        i -= 10