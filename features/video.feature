Feature: YouTube Video Tests

  Scenario: Play and Pause Test
    Given The user is on the YouTube video page
    When The user clicks the play button
    Then The video should start playing
    When The user clicks the pause button
    Then The video should pause

  Scenario: Fullscreen Test
    Given The user is on the YouTube video page
    When The user clicks the fullscreen button
    Then The video should enter fullscreen mode
    When The user exits fullscreen mode
    Then The video should exit fullscreen mode