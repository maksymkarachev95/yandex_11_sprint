import configuration
import requests
import data


def Create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.body_new_order,
                         headers=data.header)


def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track,
                        json=None,
                        headers=data.header)
