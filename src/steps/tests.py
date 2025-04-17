
from behave import given, when, then

from src.pages.search_page import SearchPage
from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep

step = 1

@given(u'User chooses the page link')
def choose_link(context):
    context.page.get_by_role("button", name="Add timer").click()
    context.page.get_by_text("⚙️️").click()
    context.page.locator("label").filter(has_text="Counting down").locator("div").nth(2).click()
    context.page.locator("label").filter(has_text="Hide tenths").locator("div").nth(4).click()
    context.page.locator("label").filter(has_text="Show tenths").locator("div").nth(2).click()
    context.page.locator("label").filter(has_text="Counting up").locator("div").nth(4).click()
    context.page.get_by_role("heading", name="Break 🖊️").click()
    context.page.get_by_role("textbox", name="Title").fill("Break info")
    context.page.get_by_role("textbox", name="Title").press("Enter")
    context.page.get_by_role("button", name="Start").click()
    context.page.get_by_role("button", name="Pause").click()
    context.page.get_by_role("button", name="Reset").click()
    context.page.get_by_role("button", name="Add note").click()
    context.page.get_by_role("heading", name="Click to change text").click()
    context.page.get_by_role("textbox", name="Description").fill("enter note here")
    context.page.get_by_role("textbox", name="Description").press("Enter")
    context.page.locator("polyline").nth(1).click()
    context.page.get_by_text("🗑️").first.click()
    context.page.get_by_text("🗑️").click()