from playwright.sync_api import Page, expect
from test.page_objects.demo.common import Common, Actions

class HomePage(Common):

    def click_on_shoe_card(page: Page):
        shoe_card = page.locator('xpath=//div[@data-slug="shoes"]/a')
        product_info = page.locator('xpath=//h2[text()="PRODUCT INFO"]')
        Actions.click_on(shoe_card,"Shoe_card")
        Actions.wait_for_page_to_load(page)
        expect(product_info).to_be_visible()



