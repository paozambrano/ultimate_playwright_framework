Feature: End-to-End Purchase Flow

    Background:
        Given the user is on the homepage "https://magento.softwaretestingboard.com/"

        Scenario: Authenticated user completes a full Purchase
            When the user logs in with "pao_tester@example.com" and "Password123!"
            And searches for "Radiant Tee"
            And selects size "M", color "Blue" and adds it to cart
            And proceeds to the checkout shipping page
            Then the order summary should show the correct total