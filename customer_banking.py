# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import SavingsAccount  
from cd_account import CD

# Define the main function
def main(savings_balance, savings_interest_rate, savings_maturity,cd_balance,cd_interest_rate, cd_maturity):
    savings_data = SavingsAccount(savings_balance, savings_interest_rate, savings_maturity)
    cd_data = CD(cd_balance, cd_interest_rate, cd_maturity)
    
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """ 
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input('What is your savings account balance?'))
    savings_interest_rate = float(input('What is the APR for the savings account?'))
    savings_maturity= float(input('What is the length of months for YOUR savings?'))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the savings account.')
    print("The balance is: $", format(savings_data.get_balance(), ',.2f'))
    print("APR interest rate is : ", format(savings_data.get_interest(), ',.2f'))
          

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input('What is your initial CD account balance?'))
    cd_interest = float(input('What is the APR dor the CD account?'))
    cd_maturity = float(input('What is the length of months foe your CD?'))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('Here are the details of the CD account.')
    print("The balance is: $", format(cd_data.get_balance(), ',.2f'))
    print("APR interest rate is:", format(cd_data.get_interest(), ',.2f'),'%')

    if __name__ == "__main__":
    #Call the main function.
       main() 