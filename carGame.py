
command = ""
car = "stopped"
while command != "quit":
    command = input("< :").lower()
    if(command == "help"):
        print("""
        start - start the car
        stop - stop the car
        quit - quit the game
""")
             
    elif (command == "start"):
        if car=="started":
            print("Car is already running")
        else:
            car = "started"
            print("Car started. Ready to go!")
        
    elif (command == "stop"):  
        if car == "stopped": 
            print("Car is already stopped")
        else:
            car = "stopped"
            print("Car started. Ready to go!")

    else : 
        print("Sorry I don't understand.")

