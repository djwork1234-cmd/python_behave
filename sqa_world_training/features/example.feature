Feature: Skip Examples
@run
Scenario: First scenario
    Given I Print " this will be run"

@skip
Scenario: Second scenario
    Given I Print " this should be skipped"


# to run tests with tags need to run in specfic file or all other tests in the other files will run as well : behave example.feature --tags=-skip will only the the tagged run test in this file and skip the skip tagged test

