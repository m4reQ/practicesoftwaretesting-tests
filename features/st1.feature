Feature: Registration (ST1)
  In order to be able to use some more advanced features of the service
  users should be able to create own accounts.

  Scenario: Registration with valid data (PT1.1)
    Given valid registration data
    When user registers with valid registration data
    Then registration succeeds

  Scenario: Registration with already taken email (PT1.2)
    Given valid registration data
    When user registers with valid registration data
    And user tries to register again with the same data
    Then registration fails

  Scenario: Login with goole account (PT1.3)
    When user opens login page
    And user logs in using google
    Then google account popup shows up
