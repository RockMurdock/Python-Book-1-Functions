# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take varying number of children's names as the argument.

# For example, the run function would be defined as follows:
"""
def run(*kids):
    # Loop through all the kids and print that the child performed the activity.

run("Joe", "Jenna")
# Output: 
# "Joe ran like a fool!"
# "Jenna ran like a fool!"
"""
# Do the same for the following children:
    # Running kids: Pam, Sam, Andrea, Will
    # Swinging kids: Marybeth, Ariel, Kevin, Courtney
    # Sliding kids: Mike, Jack, Jennifer, Earl
    # Hiding kids: Henry, Heather, Hayley, Hugh

def run(*kids):
    [print(f"{kid} loves to run!") for kid in kids]

run("Pam", "Sam", "Andrea", "Will")

print("\n")

def swing(*kids):
    [print(f"{kid} loves to swing!") for kid in kids]

swing("Marybeth", "Ariel", "Kevin", "Courtney")

print("\n")

def slide(*kids):
    [print(f"{kid} loves to slide!") for kid in kids]

slide("Mike", "Jack", "Jennifer", "Earl")

print("\n")

def hide(*kids):
    [print(f"{kid} loves to hide!") for kid in kids]

hide("Henry", "Heather", "Hayley", "Hugh")