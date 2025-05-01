Feature: Off-plan listings pagination

  Background:
    Given I open the main page
    And I log in to the page

 Scenario: User can navigate to last and first pages
  When I click on the "Off-plan" option from the left menu
  Then The "Off-plan" page should be displayed
  When I click on the last pagination button
  And I click on the first pagination button
