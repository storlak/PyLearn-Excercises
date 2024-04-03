# Running a car using if, elif, else commands

# Initialize variables
command = ""
mode = "off"  # Default mode is "off"

# Continuous loop to receive commands
while True:
    command = input("> ").lower()

    # Start the car
    if command == "start":
        if mode == "on":
            print("The car is already running.")
        else:
            print("The car started...")
            mode = "on"

    # Stop the car
    elif command == "stop":
        if mode == "off":
            print("The car is already stopped.")
        else:
            print("The car stopped.")
            mode = "off"

    # Show available commands
    elif command == "help":
        print(
            """
Start: Start the car.
Stop: Stop the car.
Exit: Exit the program.
Help: Show available commands."""
        )

    # Exit the program
    elif command == "exit":
        break

    # Handle invalid commands
    else:
        print("Invalid command.")

# Additional check if the car is off after the loop ends
if mode == "off" and command == "stop":
    print("The car is stopped.")
