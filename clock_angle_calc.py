from logging import exception
import re

def calc_angle(hour, min):
    if hour > 12:
        hour = hour % 12  #This ensures that it works whether the user inputs in 24hr time or 12hr time

    hour_angle = ((hour * 30) + (min / 60) * 30) #Calculate the angle of the hour hand

    min_angle = (min/60) * 360 #Calculate the angle of the minute hand

    if hour_angle > min_angle:
        if hour_angle - min_angle > 180:
            return 360 - (hour_angle - min_angle)

        else:
            return hour_angle - min_angle

    else:
        if min_angle - hour_angle > 180:
            return 360 - (min_angle - hour_angle)

        else:
            return min_angle - hour_angle

def main():
    #Main method that asks for user input and asks again if the user enters a value not in the format provided.
    # Then passes values to the calc_angle function

    while True:

        time = input("Please enter a time in the format 'HH:MM': ")
        if re.match("^[0-2][0-9]:[0-6][0-9]$", time):
            hour = int(time.split(":")[0])
            min = int(time.split(":")[1])
            if 24 >= hour >= 0 and 60 >= min >= 0:
                print("The lesser angle between the hour and minute hands is {} degrees".format(calc_angle(hour, min)))
                break

        else:
            print('Invalid input, try again')

if __name__ == "__main__":
    main()