"""Test suite for CRUD operations on regular files in onedata.
"""
__author__ = "Jakub Kudzia"
__copyright__ = "Copyright (C) 2015 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"
import pytest
from pytest_bdd import scenario

from tests import *
from tests.utils.path_utils import env_file
from tests.cucumber.steps.env_steps import *


@pytest.fixture(scope="module",
                params=["singleprovider_singleclient_directio",
                        "singleprovider_singleclient_proxy"])
def env_description_file(request):
    return env_file(CUSTOM_CUCUMBER_ENV_DIR, request.param)


@scenario(
    '../features/reg_file_CRUD.feature',
    'Create regular file'
)
def test_create(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Rename regular file'
)
def test_rename(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Delete regular file'
)
def test_delete(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Read and write to regular file'
)
def test_read_write(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Append regular file'
)
def test_append(env_description_file):
    pass


@pytest.mark.xfail_env(envs=["singleprovider_singleclient_directio",
                             "singleprovider_singleclient_proxy"],
                       reason="File disappears after replace")
@scenario(
    '../features/reg_file_CRUD.feature',
    'Replace word in file'
)
def test_replace(env_description_file):
    pass


@pytest.mark.xfail_env(envs=["singleprovider_singleclient_directio",
                             "singleprovider_singleclient_proxy"],
                       reason="Move fails")
@scenario(
    '../features/reg_file_CRUD.feature',
    'Move regular file and read'
)
def test_move(env_description_file):
    pass


@pytest.mark.xfail_env(envs=["singleprovider_singleclient_directio",
                             "singleprovider_singleclient_proxy"],
                       reason="Move fails")
@scenario(
    '../features/reg_file_CRUD.feature',
    'Move big regular file and check MD5'
)
def test_move_big(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Copy regular file and read'
)
def test_copy(env_description_file):
    pass


@scenario(
    '../features/reg_file_CRUD.feature',
    'Copy big regular file and check MD5'
)
def test_copy_big(env_description_file):
    pass
