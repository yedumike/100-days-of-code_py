command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started started...")
        else:
            started = True
            print("car started")
            
    elif command == "stop":
        if not started:
            print("car already started stopped...")
        else:
            started = False
            print("car stopped")
 
    elif command == "help":
        print("""start - to start the car
stop - to stop
quit to exit
""")
    elif command == "quit":
        break
    