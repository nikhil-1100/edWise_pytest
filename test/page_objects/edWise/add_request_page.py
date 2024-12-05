from playwright.sync_api import Page,expect
from test.page_objects.edWise.common_page import Common,Action

class AddRequest(Common):
    change_request_header='xpath=//h6[text()="Change Requests"]'
    add_request_button='xpath=//span[text()="Add Request"]/parent::button/..'

    def click_add_request(page: Page):
        Action.click_on_button(page.locator(AddRequest.add_request_button),"Add Request")

    def fill_dropdown(page:Page,dropdown:str,element:str):
        dropdowns=page.locator(f'xpath=//span[normalize-space(text())="{dropdown}"]/../../div[@class="rz-dropdown"]')
        element=page.locator(f'xpath=//span[text()="{element}"]/parent::li')
        Action.fill_drop_down(page,dropdowns,element)
        Action.wait_for_load(page)

    def select_card(page: Page, card:str):
        card=page.locator(f'xpath=//p[text()="{card}"]/../..')
        Action.click_on(card,f"{card} Card")
        Action.wait_for_load(page)

    def click_save_button(page:Page):
        save_and_submit=page.locator('xpath=//button[normalize-space(text())="Review and Submit"]')
        Action.click_on(save_and_submit,"save and sumbit")
        Action.wait_for_load(page)


    def click_submit_all(page:Page):

        submit_all=page.locator('xpath=(//span[normalize-space(text())="Submit All"]/..)[1]')
        submit_page = page.locator('xpath=(//p[normalize-space(text())="Category"])[1]')
        success_icon=page.locator('xpath=//img[@class="success-icon"]')
        submit_page.wait_for(state="visible")
        Action.click_on(submit_all,"Sumit all button")
        success_icon.wait_for(state="visible")
        # Action.wait_for_load(page)


    def fetch_cr_id(page: Page, card:str):
        cr_id_list=page.locator(f'xpath=//span[text()="{card}"]/../../..//span[@class="request-value"]')
        cr_id=cr_id_list.text_content()
        return cr_id



