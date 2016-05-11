"""
Author: Jakub Kudzia
Copyright (C) 2015 ACK CYFRONET AGH
This software is released under the MIT license cited in 'LICENSE.txt'

Module implements pytest-bdd steps for operations on regular files.
"""
from common import *

import subprocess


@when(parsers.parse('{user} writes {megabytes} MB of random characters to {file} on {client_node} and saves MD5'))
def write_rand_text(user, megabytes, file, client_node, context):
    client = get_client(client_node, user, context)
    file_path = make_path(file, client)
    ret = dd(client, megabytes, 1, file_path, user=user, output=False)
    md5 = md5sum(client, file_path, user=user)
    context.md5 = md5.split()[0]
    save_op_code(context, user, ret)


@when(parsers.parse('{user} writes "{text}" to {file} on {client_node}'))
def write_text(user, text, file, client_node, context):
    client = get_client(client_node, user, context)
    file_path = make_path(file, client)
    ret = echo_to_file(client, str(text), file_path, escape=True, user=user)
    save_op_code(context, user, ret)


@when(parsers.parse('{user} reads "{text}" from {file} on {client_node}'))
@then(parsers.parse('{user} reads "{text}" from {file} on {client_node}'))
def read(user, text, file, client_node, context):
    client = get_client(client_node, user, context)
    text = text.decode('string_escape')

    def condition():

        try:
            read_text = cat(client, make_path(file, client), user=user)
            print "READ: ", read_text
            return read_text == text
        except subprocess.CalledProcessError:
            return False

    assert repeat_until(condition, client.timeout)


@then(parsers.parse('{user} cannot read from {file} on {client_node}'))
def cannot_read(user, file, client_node, context):
    client = get_client(client_node, user, context)
    return_code = cat(client, make_path(file, client), user=user, output=False)
    assert return_code != 0


@when(parsers.parse('{user} appends "{text}" to {file} on {client_node}'))
def append(user, text, file, client_node, context):
    client = get_client(client_node, user, context)
    file_path = make_path(file, client)
    ret = echo_to_file(client, str(text), file_path, user=user, overwrite=False)
    save_op_code(context, user, ret)


@when(parsers.parse('{user} replaces "{text1}" with "{text2}" in {file} on {client_node}'))
def replace(user, text1, text2, file, client_node, context):
    client = get_client(client_node, user, context)
    file_path = make_path(file, client)
    ret = replace_pattern(client, file_path, text1, text2, user)
    save_op_code(context, user, ret)


@when(parsers.parse('{user} executes {file} on {client_node}'))
@then(parsers.parse('{user} executes {file} on {client_node}'))
def execute_script(user, file, client_node, context):
    client = get_client(client_node, user, context)
    ret = run_cmd(user, client, make_path(file, client))
    save_op_code(context, user, ret)


@then(parsers.parse('{user} checks MD5 of {file} on {client_node}'))
def check_md5(user, file, client_node, context):
    client = get_client(client_node, user, context)

    def condition():
        try:
            md5 = md5sum(client, make_path(file, client), user=user)
            return md5.split()[0] == context.md5
        except subprocess.CalledProcessError:
            return False

    assert repeat_until(condition, 30)
    #hardcoding this timeout can be replaced by using step "user waits 30 seconds"



@when(parsers.parse('{user} copies regular file {file} to {path} on {client_node}'))
def copy_reg_file(user, file, path, client_node, context):
    client = get_client(client_node, user, context)
    src_path = make_path(file, client)
    dest_path = make_path(path, client)
    ret = cp(client, src_path, dest_path, user=user)
    save_op_code(context, user, ret)


@when(parsers.parse('{user} changes {file} size to {new_size} bytes on {client_node}'))
def do_truncate(user, file, new_size, client_node, context):
    client = get_client(client_node, user, context)
    file_path = make_path(file, client)
    ret = truncate(client, file_path, new_size, user=user)
    save_op_code(context, user, ret)
