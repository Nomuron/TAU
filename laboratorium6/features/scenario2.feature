Feature: Shopping Cart Functionality

  Scenario Outline: Verify shopping cart functionality on SauceDemo
    Given I open the website "https://www.saucedemo.com/" using "<browser>" browser
    When I log in with username "standard_user" and password "secret_sauce"
    And I add items to the cart
    Then I should see the correct number of items in the cart

    Examples:
      | browser |
      | Chrome  |
      | Firefox |