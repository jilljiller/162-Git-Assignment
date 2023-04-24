# Initializing the 3 queues and total number of lines in the text file
premium_queue = []
standard_queue = []
economy_queue = []
total_lines = 0

# Opening the text file that contains the queue data and sorting them into the appropriate queue based off the
# first letter in each line of the text file
with open('bonus_points.txt') as bonus_points:
    for line in bonus_points:
        # Sorting to premium queue
        if line[0] == "P":
            premium_queue.append(line.strip())
        # Sorting to standard queue
        elif line[0] == "S":
            standard_queue.append(line.strip())
        # Sorting to economy queue
        elif line[0] == "E":
            economy_queue.append(line.strip())
        # Getting the total number of lines so we can use that for looping through the queues
        total_lines += 1


# Creating a function that will take in a queue and a number of times to repeat the queue
def packet(queue, repeat):
    for x in range(repeat):
        # Will print the first item from the queue, then delete it
        try:
            print(queue[0])
            queue.pop(0)
        # If nothing is left in the queue, the iteration will end
        except:
            break


# Calling the function for each queue and to be repeated the appropriate number of times for the length of the txt file
while total_lines > 0:
    total_lines -= 1
    packet(premium_queue, 3)
    packet(standard_queue, 2)
    packet(economy_queue, 1)
