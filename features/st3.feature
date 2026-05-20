Feature: Contact form functionality (ST3)
  Contact form is an useful functionality, providing users and
  sellers an efficient form of communication.

  Scenario: Sending message through contact form (ST3.1)
    Given valid contact form data
    When user opens contact form page
    And user inputs valid contact form data
    And user submits message
    Then contact message is sent

  Scenario: Failing to send message with invalid email address (ST3.2)
    Given invalid contact form data
    When user opens contact form page
    And user inputs invalid contact form data
    And user submits message
    Then invalid email error is displayed

  Scenario: Failing to send message without providing email address (ST3.3)
    Given missing contact form data
    When user opens contact form page
    And user inputs missing contact form data
    And user submits message
    Then invalid email error is displayed