Feature: Product filtering (ST4)
  Users want to efficiently filter out products that are not relevant to them at the moment.

  Scenario: Searching products matching query (PT4.1)
    Given valid search query
    When user opens main page
    And user inputs valid search query
    And user clicks search button
    Then search query is displayed in results
    And only products containing query are visible

  Scenario: Filtering products by category (PT4.2)
    When user opens main page
    And user selects products category
    Then only products of category are visible

  Scenario: Filtering products by price range (PT4.3)
    When user opens main page
    And user selects price range
    Then only products within price range are visible
    