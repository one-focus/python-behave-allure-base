# Created by Alex Kardash at 14/11/2020
@regression
Feature: 10 Main page
  Validate main page

  Background:
    Given I open home page

  @search
  Scenario: 10 Validate search
    When I type "Test automation" in search field
    When I click on search button
    Then I see "test automation is the use of" on the page

  Scenario Outline: 10 Validate left menu
    When I click on <menu item>
    Then I see "<text>" on the page

    Examples:
      | menu item       | text                  |
      | Contents        | Wikipedia:Contents    |
      | Current events  | Portal:Current events |
      | About Wikipedia | Wikipedia:About       |
      | Contact us      | Wikipedia:Contact us  |
      | Donate          | Donation amount       |
