"""Common steps used in various GUI testing scenarios
"""

__author__ = "Jakub Liput"
__copyright__ = "Copyright (C) 2016 ACK CYFRONET AGH"
__license__ = "This software is released under the MIT license cited in " \
              "LICENSE.txt"

import re
import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from tests.utils.cucumber_utils import list_parser
from tests.gui.utils.generic import parse_url
from tests.gui.conftest import WAIT_FRONTEND, WAIT_BACKEND
from pytest_bdd import given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits


@given('valid name string')
def name_string():
    return ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for i in range(6))


@then(parsers.parse('user should see that a page title contains "{text}"'))
def title_contains(selenium, text):
    Wait(selenium, WAIT_FRONTEND).until(EC.title_contains(text))


@when('user types valid name on keyboard')
def type_valid_name_string_into_active_element(selenium, name_string):
    selenium.switch_to.active_element.send_keys(name_string)


@then(parsers.parse('user types "{text}" on keyboard'))
@when(parsers.parse('user types "{text}" on keyboard'))
def type_string_into_active_element(selenium, text):
    selenium.switch_to.active_element.send_keys(text)


@then(parsers.parse('user presses enter on keyboard'))
@when(parsers.parse('user presses enter on keyboard'))
def press_enter_on_active_element(selenium):
    selenium.switch_to.active_element.send_keys(Keys.RETURN)


@then(parsers.parse('user presses backspace on keyboard'))
@when(parsers.parse('user presses backspace on keyboard'))
def press_enter_on_active_element(selenium):
    selenium.switch_to.active_element.send_keys(Keys.BACKSPACE)


@then(parsers.parse('user should see {links_names} links'))
def link_with_text_present(selenium, links_names):
    for name in list_parser(links_names):
        assert selenium.find_element_by_link_text(name)


def _click_on_link_with_text(selenium, link_name):
    selenium.find_element_by_link_text(link_name).click()


@given(parsers.parse('user clicks on the "{link_name}" link'))
def g_click_on_link_with_text(selenium, link_name):
    _click_on_link_with_text(selenium, link_name)


@when(parsers.parse('user clicks on the "{link_name}" link'))
def w_click_on_link_with_text(selenium, link_name):
    _click_on_link_with_text(selenium, link_name)


@when(parsers.parse('user is idle for {seconds:d} seconds'))
def wait_n_seconds(seconds):
    time.sleep(seconds)


@when(parsers.re(r'user changes the relative URL to (?P<path>.+)'))
def visit_relative(selenium, path):
    selenium.get(parse_url(selenium.current_url).group('base_url') + path)


@then(parsers.parse('user should see a page with "{text}" header'))
def page_with_header(selenium, text):

    def header_with_text_presence(s):
        headers = s.find_elements_by_css_selector('h1, h2, h3, h4, h5')
        try:
            return any(map(lambda h: h.text == text, headers))
        except StaleElementReferenceException:
            return False

    Wait(selenium, WAIT_BACKEND).until(header_with_text_presence)


@when(parsers.parse('user sees an {notify_type} notify with text matching to: {text_regexp}'))
@then(parsers.parse('user sees an {notify_type} notify with text matching to: {text_regexp}'))
def notify_visible_with_text(selenium, notify_type, text_regexp):
    text_regexp = re.compile(text_regexp)

    def notify_with_text_present(s):
        try:
            notifiers = s.find_elements_by_css_selector(
                '.ember-notify.ember-notify-show.{t} .message'.format(t=notify_type)
            )
            if len(notifiers) > 0:
                matching_elements = [e for e in notifiers if text_regexp.match(e.text)]
                return len(matching_elements) > 0
            else:
                return None
        except NoSuchElementException:
            return None

    Wait(selenium, 2*WAIT_BACKEND).until(notify_with_text_present)


# Below functions are currently unused and should not be used,
# because it involves a knowledge about internals...


@when(parsers.re(r'user changes application path to (?P<path>.+)'))
def on_ember_path(selenium, path):
    selenium.get(parse_url(selenium.current_url).group('base_url') + '/#' + path)