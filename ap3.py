import requests
import matplotlib.pyplot as plt 

main_api = 'https://covid19.gov.im/media/1243/covid-test-data.json'

deathtotal = []
datelist = []
date = ''

json_data = requests.get(main_api).json()
print(json_data)

for each in json_data['data-set']['generateddatetime']['date']['record']:
	print(each['date'])
for each in json_data['data-set']['record']:
	#get the date
	date = each['date'][5:]
	if date[:2] == '05':
		datelist.append(date)
	#get the number of death
		deathtotal.append(int(each['deaths-total']))
#data = json_data['data-set']['record'][0]['deaths-total']
#print(data)
#print(datelist)
#print(deathtotal)
plt.xlabel('deaths')
plt.ylabel('date')
plt.title("coronavirus")
plt.plot(deathtotal,datelist) 
plt.show()

