Feature: Docker container for fastapi service is running

  Scenario Outline: Service should be up and running
    Given an API call is made to <url>
    Then the response status code should be <status>
    Examples:
      | url   | status |
      | /docs | 200    |
