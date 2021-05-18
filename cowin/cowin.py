import requests


def getStates():
    # to get the covid vaccine session details
    district_id = input("Enter the district ID: ")
    date = input("Enter the date (dd-mm-yyyy): ")
    sessison = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+district_id+"&date="+date
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    my_json = requests.get(sessison, headers=headers).json()

    c = 0
    print(f'Session Details')
    for i in my_json['sessions']:
        c = c + 1
        print('-' * 100)
        print('Place: ', c)
        print("center id: ", i['center_id'], "\nCenter Name:", i['name'], '\nAdrresss: ', i['address'], '\nDistrict: ',
              i['district_name'], '\nState: ', i['state_name'], '\nPincode: ', i['pincode'])
        print('Date: ', i['date'], '\nTotal available capacity: ', i['available_capacity'],
              '\nAvailable Capacity for first dose: ', i['available_capacity_dose1'],
              '\nAvailable Capacity for second dose: ', i['available_capacity_dose2'])
        print('Fee: ', i['fee'], '\nAge limit: ', i['min_age_limit'], '\nVaccine name: ', i['vaccine'])
        print('Available slots', i['slots'])


getStates()
