Feature: Calculator Operations
  Tests different operations in calculator

  Scenario Outline: Sum of integers
    Given the first number is <first>, the second number is <second>
    When the operation is <operation>
    Then the result should be <result>


    Examples:
    |first|second|operation|     result      |
    | 2   |  3   |   +     |       5         |
    |2.53 |3.68  |   +     |     6.21        |
    | 2   |  3   |   -     |      -1         |
    |2.53 |3.68  |   -     |     -1.15       |
    | 2   |  3   |   *     |       6         |
    |2.53 |3.68  |   *     |    9.3104       |
    | 9   |  3   |   /     |       3         |
    |2.53 |3.68  |   /     |    0.6875       |
    | 2   |  0   |   /     |ZeroDivisionError|
