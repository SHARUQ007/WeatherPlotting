# importing requests and json
import requests, json
import os
from datetime import datetime

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
##################################################################

   print("id             : "+idn)
   print("latitute       : "+lat)
   print("longitude      : "+lon)
   
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
     
      print(f"Temperature    : {(int)(temperature-273)}")
      print(f"Name           : {name}")
      print(f"Humidity       : {humidity}")
      print(f"Pressure       : {pressure}")
      print(f"Weather Report : {report[0]['description']}")
      print("\n")
      print("----------------------------------------------")
      print("\n")
   else:
      # showing the error message
      print("Error in the HTTP request")



 
   # Data to be written
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
   listObj.append(dictionary)  





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


############################################## formating (for React) ###########################################
# Renaming the file
os.rename('out.json', 'out.js')
os.rename('date.json', 'date.js')



f=open('out.js','a')
f.write("\n export default out;")
f.close()

g=open('date.js','a')
g.write("\n export default date;")
g.close()

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

line_prepender('out.js',"const out = ")  
line_prepender('date.js',"const date = ")


# Absolute path of a file
# old_name = r"E:\demos\files\reports\details.txt"
# new_name = r"E:\demos\files\reports\new_details.txt"

