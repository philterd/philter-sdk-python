import requests


def filter(philter_endpoint, text, policy="default", verify=True):
    headers = {"Content-Type": "text/plain"}
    params = {"p": policy}
    response = requests.post(philter_endpoint + "/api/filter", params=params, headers=headers, data=text, verify=verify)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Error response received from Philter.")


def explain(philter_endpoint, text, policy="default", verify=True):
    headers = {"Content-Type": "text/plain"}
    params = {"p": policy}
    response = requests.post(philter_endpoint + "/api/explain", params=params, headers=headers, data=text, verify=verify)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error response received from Philter.")
