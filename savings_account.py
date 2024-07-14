"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
class SavingsAccount:
    def create_savings_account(self, savings_balance, savings_interest_rate, savings_maturity, savings_apr):
        self.balance = savings_balance
        self.interest_rate = savings_interest_rate
        self.months = savings_maturity
        self.apr = savings_apr
        update_balance = savings_balance
        interest_earned = savings_interest_rate * savings_balance
    
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    Account = SavingsAccount(savings_balance)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_rate = (savings_balance * (savings_apr/100 * savings_months/12))

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    SavingsAccount.update_balance = savings_balance + savings_interest_rate

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.update_balance

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    SavingsAccount.interest_earned

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    print("The balance is: $", format(savingsaccount_data.get_balance(), ',.2f'))