from playwright.sync_api import Page, expect
from  test.page_objects.edWise.common_page import Common,Action



class LandingPage(Common):
    dropdown_menu_path = 'xpath=//div[@class="rz-p-0 rz-p-md-12"]//div[@class="rz-dropdown"]/../../..'

    def click_config(page: Page):
        config_button = page.locator('xpath=//span[text()="Configurations"]/parent::div')
        Action.click_on(config_button,"confing button")
        Action.wait_for_load(page)

    def click_user(page : Page):
        select_user = page.locator('xpath=//span[text()="Select User"]/parent::a/parent::div')
        Action.click_on(select_user, "Select User")
        dropdown_menu = page.locator(LandingPage.dropdown_menu_path)
        dropdown_menu.wait_for(state="visible", timeout=10000)


    def fill_drop_down(page: Page,dropdown_name:str,element_name:str):
        dropdown = page.locator(f'xpath=//div[@class="rz-p-0 rz-p-md-12"]//label[text()="{dropdown_name}"]/parent::div')
        element = page.locator(f'xpath=//div[@class="rz-dropdown-panel rz-popup"]//span[text()="{element_name}"]/parent::li')

        dropdown.click()
        element.click()

    def click_select_button(page: Page):
        select_button = page.locator('xpath=//div[@class="rz-p-0 rz-p-md-12"]//span[normalize-space()="Select"]/parent::button')
        Action.click_on_button(select_button, "select button")




