import pywhatkit 
  
try: 
  # sending message to reciever 
  pywhatkit.sendwhatmsg("+31xxxxxxxxxx",  
                        "Hello World",  
                        21, 30) 
  print("Successfully Sent!") 
  
except: 
  print("An Unexpected Error!")






  