# importing requests and json
import os
import requests, json
from datetime import datetime


###################### function to call weather API ##############################################################

def weatherAPI_call(lat,lon,idn):
   # base URL
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   # City Name CITY = "Hyderabad"
   # API key API_KEY = "Your API Key"
   # upadting the URL
   URL = BASE_URL + "lat="+lat+"&lon="+lon+ "&appid=" + "a2df7199551cc39797a0929621d2b43a"
   # HTTP request
   response = requests.get(URL)
   # checking the status code of the request
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      name = data['name']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
   
      # print(f"Temperature    : {(int)(temperature-273)}")
      # print(f"Name           : {name}")
      # print(f"Humidity       : {humidity}")
      # print(f"Pressure       : {pressure}")
      # print(f"Weather Report : {report[0]['description']}")
      # print("\n")
      # print("----------------------------------------------")
      # print("\n")
   else:
      # showing the error message
      print("Error in the HTTP request")
   dictionary ={
    "id": idn,  
    "latitude" : site['lat'],
    "longitude" : site['lang'],
    "city" : name,
    "temperature" : temperature,
    "humidity" : humidity,
    "pressure" : pressure,
    "report" : report[0]['description']
   }
   return dictionary
#####################################################################################################################

############################################### formatting for json ################################################
def write_to_file(listObj,now):
      # Serializing json 
      json_object = json.dumps(listObj, indent = 4)

      # Writing to sample.json
      with open("out.json", "w") as outfile:
         outfile.write(json_object)

            #  import json

      then = datetime.now()
      print("\n") 
      print("start time : ", now)
      print("end time   : ", then)

      dateobj={
         "start time": str(now),
         "end time" : str(then)
      }

      with open("date.json", "w") as outfile:
          json.dump(dateobj, outfile)

#####################################################################################################################          

############################################## formating (for React) ################################################

def formatterReact():

   # Renaming the file
   os.rename('out.json', 'out.js')
   os.rename('date.json', 'date.js')

   # f=open('out.js','a')
   # f.write("\n export default out;")
   # f.close()
   def linepostpender(filename,line):
      g=open(filename,'a')
      g.write(line)
      g.close()

   def line_prepender(filename, line):
      with open(filename, 'r+') as f:
         content = f.read()
         f.seek(0, 0)
         f.write(line.rstrip('\r\n') + '\n' + content)

   linepostpender('date.js', '\n export default date;')
   linepostpender('out.js', '\n export default out;')
   line_prepender('out.js',"const out = ")  
   line_prepender('date.js',"const date = ")

#####################################################################################################################

############################################## main function ########################################################


# datetime object containing current date and time
now = datetime.now()
 
# Opening JSON file
f = open('data.json')  
# returns JSON object as 
# a dictionary
data = json.load(f)
listObj = []
#for storing objects

# Iterating through the json
# list
for site in data['sites']:
   lat=str(site['lat'])
   lon=str(site['lang'])
   idn= str(site['id'])
   # calling the weather API   
   dictionary=weatherAPI_call(lat,lon,idn)
   # Data to be written 
   listObj.append(dictionary)  


write_to_file(listObj,now)
formatterReact()

