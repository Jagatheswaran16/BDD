Feature: Product order
  Background: Product added
    Given Open Greenkart website
    When Search product name
    And Add a product to Cart
    And Go to the cart

  Scenario: Order Product in Greenkart
    Then Verify Product name

  Scenario: Promocode apply
    When   Promocode is applied
    Then   Promocode code sucessfull message should be displayed
    Then   Dicount must be applied

  Scenario: Place order without terms and conditions
    When promocode2 is applied
    When Place order button is pressed
    And country is selected
    And Terms & Conditions is not selected
    And Proceed button is clicked
    Then Terms & Conditions warning message is displayed

  Scenario: verify sucessfull place order message
    Then promocode3 is applied and country and Terms & Conditions is selected




