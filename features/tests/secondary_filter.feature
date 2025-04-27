Feature: Filtering secondary products by "Want to buy" tag

  Scenario: User can filter products by "Want to buy"
    Given I open the main page
    And I log in to the page
    When I click on the "Secondary" option from the left menu
    Then The "Secondary" page should be displayed
    When I click on Filters
    And I filter the products by "Want to buy"
    And I click on Apply Filter
    Then All product cards should have the "Want to buy" tag
