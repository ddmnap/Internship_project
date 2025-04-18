Feature: Settings Page Verification

  Scenario: Logged-in user can access and verify settings
    Given I open the main page
    And I log in to the page
    When I click on the settings option
    Then The settings page should be displayed
    And There should be 13 settings options visible
    And The 'connect the company' button should be available
