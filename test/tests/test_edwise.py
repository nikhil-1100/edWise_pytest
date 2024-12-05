
from playwright.sync_api import Page, expect
from test.page_objects.edWise.common_page import Common, Action
from test.page_objects.edWise.landing_page import LandingPage
from test.page_objects.edWise.add_request_page import AddRequest
from test.page_objects.edWise.request_page import RequestPage
from test.page_objects.edWise.approve_page import ApprovePage
import json


class TestEdwise:

    @staticmethod
    def load_test_data():
        """Load test data from the JSON file."""
        with open("test/utilities/testData.json", "r") as file:
            return json.load(file)

    def test_select_user(self, page):
        # Load the test data
        test_data = self.load_test_data()


        # Initialize data from JSON
        dropdowns = test_data.get("dropdowns")
        users = test_data.get("users")
        roles = test_data.get("roles")
        request_dropdown = test_data.get("changeRequestDropdown")
        schools = test_data.get("schools")
        education_category = test_data.get("educationCategory")
        cards = test_data.get("cards")
        card_details = test_data.get("cardDetails")
        cr_ids=[]

        # Step 1: Load URL and log in
        Action.spinner_wait(page)

        # Step 2: Select User and Role
        LandingPage.click_config(page)
        LandingPage.click_user(page)
        expect(page.locator(LandingPage.dropdown_menu_path))

        # Select user and role from dropdowns
        LandingPage.fill_drop_down(page, dropdowns[0], users[0])  # Fill User Dropdown
        LandingPage.fill_drop_down(page, dropdowns[1], roles[0])  # Fill Role Dropdown
        LandingPage.click_select_button(page)  # Click Select Button
        expect(page.locator(AddRequest.change_request_header))

        # Step 3: Create a new request
        AddRequest.click_add_request(page)
        Action.wait_for_load(page)

        # Step 4: Fill dropdowns for the request
        AddRequest.fill_dropdown(page, request_dropdown[0], schools[0])
        AddRequest.fill_dropdown(page, request_dropdown[1], education_category)

        # Step 5: Iterate through each card and fill details
        for card in cards:
            # Select the card
            AddRequest.select_card(page, card)
            Action.spinner_wait(page)

            # Get the current card's details
            current_card = next((detail for detail in card_details if detail["type"] == f"change{card}"), None)
            print(current_card)
            if current_card:
                # Process dropdowns for the card using a traditional for loop
                for i in range(len(current_card["dropdownHeads"])):
                    current_dropdown=current_card["dropdownHeads"][i]
                    current_element=current_card["dropdownValues"][i]
                    print(current_dropdown,current_element)
                    RequestPage.request_dropdown(page,current_dropdown,current_element)

                for i in range(len(current_card["textBox"])):
                    current_textbox=current_card["textBox"][i]
                    current_text=current_card["textBoxValues"][i]
                    print(current_textbox,current_text)
                    RequestPage.fill_text_box(page,current_textbox,current_text)

                reason= f"{current_card['textBoxValues'][-1]}"
                RequestPage.add_reason_for_change(page, reason)

                RequestPage.save_button(page)         #Saving the changes Made

        # Step 6: Click on the Review and Submit Button
        AddRequest.click_save_button(page)

        #Step 7 : Click on the Submit all button
        AddRequest.click_submit_all(page)

        #Step 8 : Collect the Cr ID's

        for card in cards:
            cr_ids.append(AddRequest.fetch_cr_id(page, card))
        print(cr_ids)

        #Approve each request by each approver

        for i in range(1,4):

            #Go to select user page
            LandingPage.click_user(page)
            expect(page.locator(LandingPage.dropdown_menu_path))

            # Select user and role from dropdowns
            LandingPage.fill_drop_down(page, dropdowns[0], users[i])  # Fill User Dropdown
            LandingPage.fill_drop_down(page, dropdowns[1], roles[i])  # Fill Role Dropdown
            LandingPage.click_select_button(page)  # Click Select Button
            expect(page.locator(AddRequest.change_request_header))

            #Click on the Request Queue
            Action.spinner_wait(page)
            ApprovePage.click_approve_queue(page)

            #Approve for each cr ID
            for crId in range(0,len(cr_ids)):
                current_crid=str(cr_ids[crId])
                print(current_crid)

                #Clicking the Assign to me Button
                ApprovePage.click_assign_to_me(page,current_crid)
                ApprovePage.click_Approver(page,current_crid)

                #Approve the changes

                ApprovePage.add_comments(page) #Add comments
                ApprovePage.choose_status(page,"Approved")  #Select the status from dropdown
                ApprovePage.click_submit(page)      #Click on the select button



