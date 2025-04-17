from playwright.sync_api import sync_playwright


def before_all (context):
    context.playwright = sync_playwright().start()
    # context.browser_type = context.playwright.chromium
    context.browser_type = context.playwright.firefox
    context.browser = context.browser_type.launch(headless=False)                  ## run in browser view
    # context.browser = context.browser_type.launch(headless=False,slow_mo=1000)   ## delay 1000 ms every test
    # context.browser = context.browser_type.launch(headless=True)                 ## does not run browser view

def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    context.base_url = "https://lejonmanen.github.io/timer-vue/"


def after_scenario(context, scenario):
    if context.page:
        context.page.close()

def after_all(context):
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()