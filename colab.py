success = 0   #variable for storing number of event occurence
for i in range(1000000): #repetitions
    runs = uniform(7,5) #Less than 6 deliveries = 5
    for run in runs:
        if run == 6:
           success = success + 1
           break #We need to succeed at most once in a given list of runs[].
print(success/1000000) #probability estimate by Monte Carlo
