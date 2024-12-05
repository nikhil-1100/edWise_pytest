from playwright.sync_api import Page,expect
import random
from test.page_objects.edWise.common_page import Common,Action

class RequestPage(Common):
    def random_number(page:Page):
        return random.randint(0, 9)

    def request_dropdown(page:Page, dropdown:str, element:str):
        dropdown_locator=page.locator(f'xpath=(//label[normalize-space(text())="{dropdown}"]/..//div[@class="rz-dropdown valid w-100"])[1]')
        element_locator=page.locator(f'xpath=(//span[normalize-space()="{element}"]/..)[2]')


        Action.click_on(dropdown_locator,f"{dropdown} Dropdown")
        Action.click_on(element_locator,f"{element} Element")

    def fill_text_box(page: Page, text_box: str, text: str):
        box = page.locator(f'xpath=(//input[@name="{text_box}"])[1]')
        randon_num=RequestPage.random_number(page)

        Action.click_on(box,f"{text_box}")
        text= text+str(randon_num)
        Action.fill_text_box(box, text, f"{text_box}")

    def add_reason_for_change(page: Page, reason: str):
        reason_box = page.locator(f'xpath=(//textarea[@name="ReasonForChange"])[1]')
        random_num = RequestPage.random_number(page)
        reason_with_number = reason + str(random_num)
        Action.fill_text_box(reason_box, reason_with_number, "reason")

    def save_button(page:Page):

        save_button=page.locator('xpath=(//button[@type="submit"])[1]')
        save_button.wait_for()
        Action.click_on_button(save_button,"save button")



