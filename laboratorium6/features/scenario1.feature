Feature: Login functionality test

  Scenario Outline: Validate login functionality in <browser> browser
    Given I open the website "http://www.scrapethissite.com/" on specific "<browser>"
    When I click on the login button
    And I enter "example@onet.pl" and "example"
    And I click the login button
    Then I should see an error message "No user with that email address"

    Examples:
      | browser |
      | Chrome  |
      | Firefox |