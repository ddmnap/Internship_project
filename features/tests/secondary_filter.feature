Feature: Filtering secondary products by "Want to buy" tag

  Feature: Secondary listings page filters

Background:
  Given I open the main page
  Given I log in to the page
  When I click on the "Secondary" option from the left menu
  Then The "Secondary" page should be displayed
  When I click on Filters

Scenario: User can filter products by "Want to buy"
    When I filter the products by "Want to buy"
    And I click on Apply Filter
    Then All product cards should have the "Want to buy" tag

Scenario: User can filter products by price range 1200000 - 2000000 AED
    When I filter the products by price range from 1200000 to 2000000 AED
    And I click Apply Filter after setting price range
    Then All product cards should have prices within the selected range
