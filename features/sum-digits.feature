Feature: Sum two number using Calc

  Scenario: Calc two number sum
    Given a calc
    When sum 7 and 6
    Then the result is 13

  Scenario Outline: Calculate different number sum
    Given a calc
    When sum <first_number> and <second_number>
    Then the result is <result>

    Examples: Different numbers
    | first_number | second_number | result |
    | 1            | 1             | 2      |
    | 3            | 1             | 4      |
    | 1            | 3             | 4      |
    | 5            | 5             | 10     |
    | 3            | 3             | 6      |
