"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
class CD:
    def create_cd_account(self,cd_balance, cd_interest_rate, cd_maturity):
        self.balance = cd_balance
        self.interest_rate = cd_interest_rate
        self.months = cd_maturity
        cd_data = CD(cd_balance, cd_interest_rate, cd_maturity)
       
        """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    Account = CD(cd_balance)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest_rate = (cd_balance * (cd_apr/100 * cd_maturity/12))

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    CD.update_balance = cd_balance + cd_interest_rate

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    CD.update_balance

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    CD.interest_earned

    # Return the updated balance and interest earned.
    # ADD YOUR CODE HERE
    print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
