# Created by Alex Kardash at 14/11/2020
@regression
Feature: Login
  Check user can login with valid username and password

  Scenario: Invalid login - data table
    Given I open login page
    Then I see validation message for
      | username     | password     | text                                                 |
      | sozdai       | sozdai       | Incorrect username or password entered               |
      | 1234qwerqwer | 1234qwerqwer | Incorrect username or password entered.              |
      | !@#$qwerqwer | !@#$qwerqwer | The supplied credentials could not be authenticated. |
