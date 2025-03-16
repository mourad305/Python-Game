import time
second = int(input('time wait: '))
for i in range(second): 
    print(str(second - i ), 'Second remian')
    time.sleep(60)
print('Time up')
mou = input('PLease enter you answer :')