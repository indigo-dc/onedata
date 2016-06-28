"""Module implements pytest-bdd steps for operations on directories in multiclient environment.
"""
__author__ = "Jakub Kudzia"
__copyright__ = "Copyright (C) 2015 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"

from cucumber_utils import *
from tests.utils.client_utils import ls, rm, rmdir, mkdir, cp, client_mount_path, \
    save_op_code, get_client


@when(parsers.parse('{user} creates directories {dirs} on {client_node}'))
@when(parsers.parse('{user} creates directories {dirs}\non {client_node}'))
def create(user, dirs, client_node, context):
    dirs = list_parser(dirs)
    user = context.get_user(user)
    client = user.get_client(client_node)
    for dir in dirs:
        path = client.absolute_path(dir)
        try:
            mkdir(client, path)
            user.mark_last_operation_succeeded()
        except Exception as e:
            user.mark_last_operation_failed()


@when(parsers.parse('{user} creates directory and parents {paths} on {client_node}'))
@when(parsers.parse('{user} creates directory and parents {paths}\non {client_node}'))
def create_parents(user, paths, client_node, context):
    user = context.get_user(user)
    client = user.get_client(client_node)
    paths = list_parser(paths)
    for path in paths:
        dir_path = client.absolute_path(path)
        try:
            mkdir(client, dir_path, recursive=True)
            user.mark_last_operation_succeeded()
        except Exception as e:
            user.mark_last_operation_failed()


@when(parsers.parse('{user} deletes empty directories {dirs} on {client_node}'))
def delete_empty(user, dirs, client_node, context):
    user = context.get_user(user)
    client = user.get_client(client_node)
    dirs = list_parser(dirs)
    for dir in dirs:
        path = client.absolute_path(dir)
        try:
            rmdir(client, path)
            user.mark_last_operation_succeeded()
        except:
            user.mark_last_operation_failed()


@when(parsers.parse('{user} deletes non-empty directories {dirs} on {client_node}'))
def delete_non_empty(user, dirs, client_node, context):
    user = context.get_user(user)
    client = user.get_client(client_node)
    dirs = list_parser(dirs)
    for dir in dirs:
        path = client_mount_path(dir, client)

        def condition():

            try:
                rm(client, path)
                user.mark_last_operation_succeeded()
                return True
            except:
                user.mark_last_operation_failed()
                return False

        client.perform(condition())


@when(parsers.parse('{user} deletes empty directory and parents {paths} on ' +
                    '{client_node}'))
def delete_parents(user, paths, client_node, context):
    user = context.get_user(user)
    client = user.get_client(client_node)
    paths = list_parser(paths)
    for path in paths:
        dir_path = client.absolute_path(path)
        try:
            rmdir(client, dir_path, recursive=True)
            user.mark_last_operation_succeeded()
        except:
            user.mark_last_operation_failed()


@when(parsers.parse('{user} copies directory {dir1} to {dir2} on {client_node}'))
def copy_dir(user, dir1, dir2, client_node, context):
    client = get_client(client_node, user, context)
    src_path = client_mount_path(dir1, client)
    dest_path = client_mount_path(dir2, client)
    ret = cp(client, src_path, dest_path, recursive=True)
    save_op_code(context, user, ret)


@when(parsers.parse('{user} can\'t list {dir} on {client_node}'))
@then(parsers.parse('{user} can\'t list {dir} on {client_node}'))
def cannot_list_dir(user, dir, client_node, context):
    client = get_client(client_node, user, context)
    path = client_mount_path(dir, client)

    def condition():
        try:
            ls(client, path=path)
            return False
        except:
            return True

    assert repeat_until(condition, client.timeout)


@when(parsers.parse('{user} can list {dir} on {client_node}'))
@then(parsers.parse('{user} can list {dir} on {client_node}'))
def list_dir(user, dir, client_node, context):
    client = get_client(client_node, user, context)
    path = client_mount_path(dir, client)

    def condition():
        try:
            ls(client, path=path)
            return True
        except:
            return False

    assert repeat_until(condition, client.timeout)
