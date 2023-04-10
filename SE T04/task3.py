# Triathalon input variables
swim_time = input("Please input your swimming time in minutes: ")
cycle_time = input("Please input your cycling time in minutes: ")
run_time = input("Please input your running time in minutes: ")

# Total time sum of all inputted times, added int() method to ensure adds up correctly and doesnt concat.
total_time = int(swim_time) + int(cycle_time) + int(run_time)

# Print total time
print("Your total triatholon time is: " + str(total_time))

# If statements to match criteria
if total_time <= 100:
    print("You get Provincial Colours!")
elif 100 < total_time < 105:
    print("You get Provincial Half Colours!")
elif 105 < total_time < 110:
    print("You get Provincial Scroll!")
# No need for logical statement if all previous logic checks have failed because total_time is not < 100+10.
else:
    print("Sorry you didn't get an award")
