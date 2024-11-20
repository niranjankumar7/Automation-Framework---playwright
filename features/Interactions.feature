Feature: User Interactions

#  Scenario: 001 - User tries static drag and drop
#    Given I am on the drag and drop page static
#    When I drag and drop the element static
#    Then close the browser

#  Scenario: 002 - User tries dynamic drag and drop
#    Given I am on the drag and drop page dynamic
#    When I drag and drop the element dynamic
#    Then close the browser

#   Scenario: 003 - User tries Selectable functionality
#    Given I am on the selectable page
#    When I select the elements
#    Then close the browser

    #not working properly. It worked but assertion might be the issue.
    Scenario: 004 - User tries Resizable functionality
    Given I am on the resizable page
    When I resize the element
    Then close the browser