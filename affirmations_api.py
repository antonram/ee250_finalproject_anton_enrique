import requests
import json


def dff_init():

    #requests data from the API
    response = requests.get('https://www.affirmations.dev/')

    if response.status_code == 200:
        # translates response into json
        data = response.json()
        # data_json = json.dumps(data, sort_keys=True, indent=4)
        # print(data_json)
        # above lines for debugging

        # returns the fun fact from the API
        return data["affirmation"]

    else:
        # in case of error
        print('error: got response code %d' % response.status_code)
        print(response.text)
        return 0.0,0.0


AFFIRMATIONS_APP = {
    'name': 'Affirmation',
    'init': dff_init
}

if __name__ == '__main__':
    dff_init()
