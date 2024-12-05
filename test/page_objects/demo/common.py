import allure
from playwright.sync_api import Page, Locator, expect


class Actions:
    def click_on(locator: Locator,name : str):

        locator.click()
        print(f"Clicked on {name}")

    def wait_for_page_to_load(page: Page):
        page.wait_for_load_state('networkidle')
        print("Page load complete")

    def text_type(locator : Locator, text: str, name: str):
        locator.fill(text)
        print(f"Typed '{text}' into {name}")

    def click_button(locator: Locator, button_name: str):

        locator.click()
        print(f"Button '{button_name}' clicked")

class Common:
    base_url='https://symonstorozhenko.wixsite.com/website-1'

    def launch_web_app(page: Page):
        page.goto(Common.base_url)
        print(f"Navigated to the URL: {Common.base_url}")

    def open_shop_woman_page(page: Page):
        woman_page= page.locator('xpath=//p[text()="Shop Women"]/..')
        shoe_card = page.locator('xpath=//div[@data-slug="shoes"]/a')
        Actions.click_on(woman_page,"woman page")
        Actions.wait_for_page_to_load(page)
        expect(shoe_card).to_be_visible()
        print("Shop page with products card should be visible")





