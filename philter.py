import requests


def filter(philter_endpoint, text, verify=True):
    headers = {"Content-Type": "text/plain"}
    response = requests.post(philter_endpoint + "/api/filter", headers=headers, data=text, verify=verify)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Error response received from Philter.")


def explain(philter_endpoint, text, verify=True):
    headers = {"Content-Type": "text/plain"}
    response = requests.post(philter_endpoint + "/api/explain", headers=headers, data=text, verify=verify)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error response received from Philter.")
