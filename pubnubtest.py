from pubnub.callbacks import SubscribeCallback 
from pubnub.enums import PNStatusCategory  
from pubnub.pnconfiguration import PNConfiguration  
from pubnub.pubnub import PubNub  

pnconfig = PNConfiguration() 

pnconfig.subscribe_key = "sub-c-0860b0e2-7ffa-11e7-bdc2-6e5eeb112503" 
pnconfig.publish_key = "pub-c-1dd54001-d20c-423d-8535-a659b6adf606" 

pubnub = PubNub(pnconfig)  

def my_publish_callback(envelope, status):  
  print(envelope, status)

pubnub.publish().channel("pubnub_onboarding_channel").message("Hellloo From Python SDK") .async(my_publish_callback)