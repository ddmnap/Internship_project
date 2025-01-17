# Created by Дашуля at 15.01.2025
Feature: Change Password Functionality

   Scenario: Logged-in user can open the change password page
      Given I open the Reelly main page
      Given I log in with valid credentials
      When I click on the settings button
      And I click on the change password button
      Then I should see the change password form
      And the "Change password" button should be available