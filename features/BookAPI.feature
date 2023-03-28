Feature: As a consumer of the BookAPI I want to be able to add and delete books

  Scenario: Verify the AddBook API functionality
    Given I have a book payload
    When I send a POST request containing the book payload to the add book endpoint
    Then book is successfully added





