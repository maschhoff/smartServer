# smartServer
SmartServer for openHAB service bindings

# Installation 
pip3 install flask

# Running
python3 Server.py

# Example  
CometBlue - change temperature for one adapter with the mac 85:99:F7:EF:71:D2  
http://XX.XX.XX.XXX:3247/85:99:F7:EF:71:D2/21  
  
Wheather - send current wheather to openHAB  
http://XX.XX.XX.XXX:3247/weather  
  
Text to Speak - change a text to mp3 and send it to a chromecast device with cast url and remote
http://XX.XX.XX.XXX:3247/sot/CastLRBAD_URI/Badezimmer_Fernbedienung/Text%20to%20speak
