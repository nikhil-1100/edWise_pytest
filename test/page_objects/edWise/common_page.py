from playwright.sync_api import Page, Locator, expect
from pytest_base_url.plugin import base_url
from pytest_playwright.pytest_playwright import browser


class Action:

    def click_on(locator : Locator, name:str):
        locator.click()
        print(f"Clicked on {name}")

    def click_on_button(locator: Locator, button_name: str):
        locator.click()
        print(f"Clicked on the {button_name}")

    def wait_for_load(page: Page):
        page.wait_for_load_state('networkidle')

    def fill_text_box(locator: Locator,text:str, name: str):
        Action.click_on(locator,"TextBox")
        locator.fill(text)
        print (f"Entered {text}, into {name}")

    def spinner_wait(page: Page):
        spinner = page.locator('xpath=(//div[@class="lds-spinner"])[1]')
        spinner.wait_for(state="hidden", timeout=60000)  # Wait for up to 60 seconds
        print("Spinner disappeared")

    def fill_drop_down(page: Page,dropdown_locator: Locator,element_locator: Locator):
        dropdown_locator.click()
        element_locator.click()


class Common:
    base_url= "https://web-edmaster-test-wtus-ui-01.azurewebsites.net/"

    def load_url(page: Page):
        page.goto(Common.base_url)
        page.set_viewport_size({"width": 1200, "height": 580})

        Action.wait_for_load(page)
        print(f"Navigate to {Common.base_url}")