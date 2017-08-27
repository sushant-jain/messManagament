#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import software2
import printer

#from pubnub.callbacks import SubscribeCallback 
#from pubnub.enums import PNStatusCategory  
#from pubnub.pnconfiguration import PNConfiguration  
#from pubnub.pubnub import PubNub  

#pnconfig = PNConfiguration() 

#pnconfig.subscribe_key = "sub-c-0860b0e2-7ffa-11e7-bdc2-6e5eeb112503" 
#pnconfig.publish_key = "pub-c-1dd54001-d20c-423d-8535-a659b6adf606" 

#pubnub = PubNub(pnconfig)  

def my_publish_callback(envelope, status):  
  print(envelope, status)




continue_reading = True
# GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)  #SETTING UP GPIO BOARD
#GPIO.setup(29,GPIO.OUT)   #SETTING PIN 29 AS OUTPUT PIN TO RELAY 
#GPIO.output(29,True)    #SETTING INITIAL VALUE AS TRUE AS RELAY IS TRIGGERED ON GROUND
lock_delay=3
# Capture SIGINT for cleanup when the script is aborted



# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
 


# This loop keeps checking for RFID cards. If one is near it will get the UID and authenticate
while continue_reading:
    #Setting default Trigger for Relay
    #GPIO.output(29,True)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print("Card detected")
        # Get the UID of the card
        time.sleep(0.6)
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print(uid)
         
        #Authentication
        auth,uidString,meal=software2.auth(uid)
        time.sleep(3)
        if(auth==1):
                print("Welcome"+meal)
                printer.printTicket(uidString,meal)
                #pubnub.publish().channel("mess").message(uidString).async(my_publish_callback)
                #Trigerring Relay
                #GPIO.output(29,False)
                time.sleep(lock_delay)
        elif(auth==0):
                #pubnub.publish().channel("mess").message("Unauthorised").async(my_publish_callback)
                
                print("Unauthorized")
        else:
            print("YOu already ate")

            
    time.sleep(0.1)
