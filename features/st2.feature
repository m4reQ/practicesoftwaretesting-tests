Feature: Cart functionality (ST2)
  Cart functionality is crucial in providing pleasurable shopping experience.

  Scenario: Adding item to cart (PT2.1)
    When user opens main page
    And items cards are visible
    And user clicks on a product card
    And user clicks add item button
    And user opens checkout page
    Then products are visible in cart

  Scenario: Removing item from cart (PT2.2)
    When user opens main page
    And items cards are visible
    And user clicks on a product card
    And user clicks add item button
    And user opens checkout page
    And products can be removed
    And user removes product from cart
    Then cart is empty
  
  Scenario: Trying to add item with negative quantity (PT2.3)
    When user opens main page
    And items cards are visible
    And user clicks on a product card
    And user inputs negative quantity
    Then quantity is 1