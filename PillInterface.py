def setup():
    global position
    global hour1
    global hour2
    global min1
    global min2
    global pill
    global period
    global calibration
    position = 1
    hour1 = 0
    hour2 = 0
    min1 = 0
    min2 = 0
    period = 1
    calibration = 7
    opening_interface()

def opening_interface():
    global position
    global pill
    if position == 1:
        print("PILL 1 | pill 2")
    elif position == 2:
        print("pill 1 | PILL 2")
    #Apparently Python can't underline text, so I just put the highlighted option in capital letters.
    elif position == 3:
        position = 1
    #The only way "position = 3" can be reached is if the user pressed Right and the cursor was on Pill 2. So, position should be moved to 1, and the interface will reset.
        opening_interface()
    elif position == -1:
        position = 2
    #The only way "position = -1" can be reached is if the user pressed Left and the cursor was on Pill 1. So, position should be moved to 2, and the interface will reset.
        opening_interface()
    user = input("> ")
    if user.lower() == "r":
    #AKA Right
        position += 1
        opening_interface()
    elif user.lower() == "l":
    #AKA Left
        position -= 1
        opening_interface()
    elif user.lower() == "s":
    #AKA Select
        if position == 1:
            print("YOU HAVE SELECTED PILL 1")
            pill = 1
            position = 1
            time()
        elif position == 2:
            print("YOU HAVE SELECTED PILL 2")
            pill = 2
            position = 1
            time()
    else:
        print("INVALID INPUT")
        opening_interface()
        
def time():
    global position
    global hour1
    global hour2
    global min1
    global min2
    global pill
    #IT'S CORRECTIONS TIME!
    if hour1 == 3:
        hour1 = 0
        #Because 30 hours don't exist.
        time()
    if hour1 == 2 and hour2 == 4:
        hour2 = 0
        #Because 24 hours don't exist.
        time()
    if hour2 == 10:
        hour2 = 0
        #Because single slots only go up to 9.
        time()
    if min1 == 6:
        min1 = 0
        #Because 60 minutes is an hour.
        time()
    if min2 == 10:
        min2 = 0
        #Because single slots only go up to 9.
        time()
    if hour1 == 2 and hour2 == 4 and min1 == 1:
        min1 == 0
    if hour1 == 2 and hour2 == 4 and min2 == 1:
        min2 == 0
    print(str(hour1) + str(hour2) + ":" + str(min1) + str(min2))
    user = input("> ")
    if user.lower() == "l":
        position -= 1
        if position == -1:
            setup()
        time()
    elif user.lower() == "r":
        position += 1
        if position == 5:
            print("YOU HAVE SELECTED", str(hour1) + str(hour2) + ":" + str(min1) + str(min2), "TO BE YOUR TIME OF DEPOSAL FOR PILL", pill)
            global finalhour
            global finalmin
            finalhour = int(str(hour1) + str(hour2))
            finalmin = int(str(min1) + str(min2))
            position = 1
            period()
        else:
            time()
    elif user.lower() == "s":
        if position == 1:
            hour1 += 1
            time()
        elif position == 2:
            hour2 += 1
            time()
        elif position == 3:
            min1 += 1
            time()
        elif position == 4:
            min2 += 1
            time()
    else:
        print("INVALID INPUT")
        time()

def period():
    global period
    global finalhour
    global finalmin
    global pill
    if period == 1:
        print("Every DAY")
    elif period == 2:
        print("Every WEEK")
    elif period == 3:
        print("Every TWO WEEKS")
    elif period == 4:
        print("Every THREE WEEKS")
    elif period == 5:
        period = 1
        period()
    user = input("> ")
    if user.lower() == "s":
        period += 1
        period()
    elif user.lower() == "r":
        if period == 1:
            period = "DAY"
            print("PILL", str(pill), "WILL DISPENSE EVERY", period, "ON", str(finalhour) + ":" + str(finalmin))
            calibration()
        elif period == 2:
            period = "WEEK"
            print("PILL", str(pill), "WILL DISPENSE EVERY", period, "ON", str(finalhour) + ":" + str(finalmin))
            position = 1
            periodday()
        elif period == 3:
            period = "TWO WEEKS"
            print("PILL", str(pill), "WILL DISPENSE EVERY", period, "ON", str(finalhour) + ":" + str(finalmin))
            position = 1
            periodday()
        elif period == 4:
            period = "THREE WEEKS"
            print("PILL", str(pill), "WILL DISPENSE EVERY", period, "ON", str(finalhour) + ":" + str(finalmin))
            position = 1
            periodday()
    elif user.lower() == "l":
        time()

def periodday():
    if position == 1:
        print("MONDAY")
    elif position == 2:
        print("TUESDAY")
    elif position == 3:
        print("WEDNESDAY")
    elif position == 4:
        print("THURSDAY")
    elif position == 5:
        print("FRIDAY")
    elif position == 6:
        print("SATURDAY")
    elif position == 7:
        print("SUNDAY")
    elif position == 8:
        position == 1
        periodday()
    user = input("> ")
    if user.lower() == "l":
        period()
    elif user.lower() == "s":
        position += 1
        periodday()
    elif user.lower() == "r":
        calibration()
        
def calibration():
    global calibration
    global period
    print("NEXT SLOT")
    user = input("> ")
    if user == "l":
        if period == "DAY":
            period()
        else:
            periodday()
    elif user == "s":
        calibration -= 1
        if calibration == 0:
            print("CALIBRATION COMPLETE")
        else:
            calibration()
setup()
