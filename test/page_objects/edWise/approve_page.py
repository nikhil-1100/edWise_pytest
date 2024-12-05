from playwright.sync_api import Page, expect
from  test.page_objects.edWise.common_page import Common,Action

class ApprovePage(Common):
    approver_queue='xpath=//span[text()="Approval Queue"]/parent::a/parent::div'


    def click_approve_queue(page: Page):
        Action.click_on(page.locator(ApprovePage.approver_queue),"Approval Queue")
        Action.wait_for_load(page)
        Action.spinner_wait(page)

    def click_assign_to_me(page : Page, id: str  ):
        assign_to_me=page.locator(f'xpath=//span[text()="{id}"]/../..//td//button')
        assign_to_me.wait_for()
        Action.click_on(assign_to_me,"Assign to me")
        Action.wait_for_load(page)

    def click_Approver(page: Page, id:str):
        approver_button=page.locator(f'xpath=//span[text()="{id}"]/../..//a[contains(text(),Approver)]')
        approver_button.wait_for()
        Action.click_on(approver_button,"Approver")
        Action.wait_for_load(page)

    def add_comments(page: Page):
        comment_box=page.locator('xpath=//textarea[@tabindex="0"][@name="comments"]')
        Action.fill_text_box(comment_box,"Approved","Commnent Box")

    def choose_status(page:Page, element:str):
        status_dropdown=page.locator('xpath=//textarea[@tabindex="0"][@name="comments"]/../..//div[@class="approval-form-select"]')
        element_dropdown=page.locator(f'xpath=//div[@class="rz-dropdown-panel rz-popup"]//span[text()="{element}"]')

        Action.click_on(status_dropdown,"status Dropdown")
        Action.click_on(element_dropdown,f"{element}")

    def click_submit(page:Page):
        submit_button=page.locator('xpath=//textarea[@tabindex="0"][@name="comments"]/../..//button[@type="submit"]')
        verify_head=page.locator('xpath=//h6[text()="Approval Queue"]')

        Action.click_on(submit_button,"Submit Button")
        verify_head.wait_for()
        Action.wait_for_load(page)