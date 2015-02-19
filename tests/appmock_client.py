#!/usr/bin/env python

import json
import testutil

appmock_rc_port = 9999


def rest_endpoint_request_count(appmock_ip, endpoint_port, endpoint_path):
    """Returns how many times has given endpoint been requested.
    IMPORTANT: the endpoint_path must be literally the same as in app_desc module,
    for example: '/test1/[:binding]'
    """
    json_data = {
        'port': endpoint_port,
        'path': endpoint_path
    }
    _, _, body = testutil.http_post(appmock_ip, appmock_rc_port,
                                    '/rest_endpoint_request_count', True,
                                    json.dumps(json_data))
    body = json.loads(body)
    if body['result'] == 'error':
        raise Exception('rest_endpoint_request_count returned error: ' + body['reason'])
    return body['result']


def create_endpoint_entry(port, path):
    entry = {
        'endpoint': {
            'path': path,
            'port': port
        }
    }
    return entry

def verify_rest_history(appmock_ip, expected_history):
    """Verifies if rest endpoints were requested in given order.
    The expected_history is a list of tuples (port, path), for example:
    [(8080, '/test1/[:binding]'), (8080, '/test2')]
    """
    json_data = [create_endpoint_entry(port, path) for (port, path) in expected_history]
    _, _, body = testutil.http_post(appmock_ip, appmock_rc_port,
                                    '/verify_rest_history', True,
                                    json.dumps(json_data))
    print(json.dumps(json_data))
    body = json.loads(body)
    if body['result'] == 'error':
        raise Exception('rest_endpoint_request_count returned error: ' + body['reason'])
    return body['result']


expected_history = [
    (8080, '/test1/[:binding]'),
    (8080, '/test1/[:binding]'),
    (8080, '/test2'),
    (8080, '/test2'),
    (8080, '/test2'),
    (9090, '/test_with_state'),
    (9090, '/test_with_state'),
    (9090, '/test_with_state'),
    (9090, '/test_with_state'),
    (9090, '/test_with_state'),
    (443, '/[:binding/[...]]')
]
print verify_rest_history('172.17.0.232', expected_history)

# print rest_endpoint_request_count('172.17.0.232', 9090, '/test_with_state')