import requests


def getStates():
    # to get the
    # district_id = input("Enter the district ID: ")
    # date = input("Enter the date (dd-mm-yyyy): ")
    sessison = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=266&date=20-05-2021"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    my_json = requests.get(sessison, headers=headers).json()

    print(my_json['sessions'])


getStates()
