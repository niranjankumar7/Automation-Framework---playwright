Feature: User Widgets

  Scenario: 001 User hanldes accordion
    Given The user is on widgets page acoordion section
    When The user handles the widgets accordion
    When The user tries to close the accordion
    Then close the browser

#  Scenario: 002 User hanldes autocomplete
#    Given The user is on widgets page autocomplete section
#    When The user handles the widgets autocomplete
#    Then close the browser
#
#  Scenario: 003 User hanldes datepicker
#    Given The user is on widgets page datepicker section
#    When The user handles the widgets datepicker
#    Then close the browser
#
#  Scenario: 004 User hanldes slider
#    Given The user is on widgets page slider section
#    When The user handles the widgets slider
#    Then close the browser