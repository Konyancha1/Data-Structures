import time
# Starting time of the program before any code 
start_time = time.time()
# Code start , 
for i in range(20):
    print(i)
time.sleep(1)

#end of the code
end_time = time.time()

#Print the time of execution of the program
print('The runtime of this program is:', {end_time- start_time}, 'seconds')
