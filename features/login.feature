Feature: User Authentication

    Background:
        Given the user is on the Magento homepage

        Scenario: Successful login with valid credentials
            When the user navigates to the login page
            And logs in with "pao_tester@example.com" and "Password123!"
            Then the user should see their personalized welcome message