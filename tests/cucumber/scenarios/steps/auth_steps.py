"""
Author: Piotr Ociepka
Author: Jakub Kudzia
Copyright (C) 2015 ACK CYFRONET AGH
This software is released under the MIT license cited in 'LICENSE.txt'

Module implements pytest-bdd steps for authorization and mounting oneclient.
"""

import pytest
from pytest_bdd import (given, when, then)
from pytest_bdd import parsers

import subprocess
import sys
import time

from environment import docker, env
from common import *


@given(parsers.parse('{users} start oneclient nodes {client_nodes} in\n' +
                     '{mount_paths} on computers {ids} respectively,\n' +
                     'using {tokens}'))
def multi_mount(users, client_nodes, mount_paths, ids, tokens, environment, context, client_ids):
    # TODO many clients for one user, parsing list of lists
    # cleaning to common

    users = list_parser(users)
    client_nodes = list_parser(client_nodes)
    mount_paths = list_parser(mount_paths)
    ids = list_parser(ids)
    tokens = list_parser(tokens)

    # current version is for environment with one GR
    gr_node = environment['gr_nodes'][0]
    gr = gr_node.split('@')[1]

    set_dns(environment)

    for i in range(len(users)):
        user = str(users[i])
        client_node = str(client_nodes[i])
        mount_path = str(mount_paths[i])
        id = int(ids[i])
        token = str(tokens[i])

        # set token for user
        token = set_token(token, user, gr_node)

        # create client object
        client = Client(client_ids[id - 1], mount_path)

        # clean if there is directory in the mount_path
        if run_cmd(client, "ls " + mount_path) == 0:
            clean_mount_path(client)

        cmd = "mkdir -p " + mount_path + " && export GLOBAL_REGISTRY_URL=" + gr + \
              ' && echo ' + token + ' > token && ' + \
              './oneclient --authentication token --no_check_certificate ' + mount_path + \
              ' < token && rm token'

        ret = run_cmd(client, cmd)

        if user in context.users:
            context.users[user].clients[client_node] = client
        else:
            context.users[user] = User(client_node, client)

        # remove accessToken to mount many clients on one docker
        run_cmd(client, "rm -rf ~/.local")

        save_op_code(context, user, ret)


@given(parsers.parse('{user} starts oneclient in {mount_path} using {token}'))
def default_mount(user, mount_path, token, environment, context, client_ids):
    multi_mount(make_arg_list(user), make_arg_list("client1"), make_arg_list(mount_path),
                make_arg_list('1'), make_arg_list(token), environment, context, client_ids)


@then(parsers.parse('{spaces} are mounted for {user}'))
def check_spaces(spaces, user, context):
    time.sleep(3)
    # sleep to be sure that environment is up
    for client_node, client in context.users[user].clients.items():
        spaces = list_parser(spaces)
        spaces_in_client = run_cmd(client, ['ls', make_path("spaces", client)], output=True)
        spaces_in_client = spaces_in_client.split("\n")
        for space in spaces:
            assert space in spaces_in_client


####################################################################################################


def clean_mount_path(client):
    # get pid of running oneclient node
    pid = run_cmd(client,
                  " | ".join(
                      ["ps aux",
                       "grep './oneclient --authentication token --no_check_certificate '" + client.mount_path,
                       "grep -v 'grep'",
                       "awk '{print $2}'"]),
                  output=True)

    if pid != "":
        # kill oneclient process
        run_cmd(client, "kill -KILL " + str(pid))

    # unmount onedata
    run_cmd(client, "umount " + client.mount_path)

    # remove onedata dir
    run_cmd(client, "rm -rf " + client.mount_path)


def set_dns(environment):
    with open("/etc/resolv.conf", "w") as conf:
        dns = environment['dns']
        conf.write("nameserver " + dns)


def set_token(token, user, gr_node):
    if token == "bad token":
        token = "bad_token"
    elif token == "token":
        token = subprocess.check_output(
            ['./tests/cucumber/scenarios/utils/get_token.escript', gr_node, user],
            stderr=subprocess.STDOUT)
    return token
