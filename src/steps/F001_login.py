
from behave import given, when, then

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

step = 1

@given(u'User chooses the page link')
def choose_link(context):

    context.page.goto(context.base_url)
    search_page = SearchPage(context.page)
    sleep(0)

@when(u'User browse the button options')
def check_buttons(context):
    search_page = SearchPage(context.page)
    context.page.get_by_role("button", name="Light").click()
    sleep(step)
    context.page.get_by_role("button", name="Dark").click()
    sleep(step)
    context.page.get_by_role("button", name="Forest").click()
    sleep(step)
    context.page.get_by_role("button", name="Orange").click()

@then(u'first page is show')
def see_first_page(context):

    expect(context.page.get_by_text('This app was written in Vue 3')).to_be_visible()
    sleep(0)
