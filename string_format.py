num1 = 3.1415
num2 = 10.29013324

#Previous
#print('num1 is ', num1, 'and num 2 is ', num2)

#Format Method
#print('num 1 is {0:.3} and num 2 is {1:.3}'.format(num1, num2))
#print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(num1, num2))

#using f-strings
#print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# The total in mins from time and duration
total_mins = (hour * 60 + mins + dura)

# Back to time format from total mins
end_hour = (total_mins // 60) % 24
end_min = total_mins % 60

print("Finish time : " + str(end_hour) + ":" + str(end_min))
