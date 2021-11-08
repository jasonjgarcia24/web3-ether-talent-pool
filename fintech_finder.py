# Cryptocurrency Wallet

################################################################################
# For this Challenge, you will assume the perspective of a Fintech Finder
# customer in order to do the following:

# * Generate a new Ethereum account instance by using your mnemonic seed phrase
# (which you created earlier in the module).

# * Fetch and display the account balance associated with your Ethereum account
# address.

# * Calculate the total value of an Ethereum transaction, including the gas
# estimate, that pays a Fintech Finder candidate for their work.

# * Digitally sign a transaction that pays a Fintech Finder candidate, and send
# this transaction to the Kovan testnet.

# * Review the transaction hash code associated with the validated blockchain transaction.

# Once you receive the transaction’s hash code, you will navigate to [Kovan’s
# Etherscan](https://kovan.etherscan.io/) website to review the blockchain
# transaction details. To confirm that you have successfully created the
# transaction, you will save screenshots to the README.md file of your GitHub
# repository for this Challenge assignment.

################################################################################
# Imports
import streamlit as st
import streamlit.components.v1 as components

from streamlit_custom_components.copycontent_button   import _copycontent_button
from streamlit_custom_components.crypto_account_stack import _crypto_account_stack

from dataclasses import dataclass
from typing      import Any, List

################################################################################
# Step 1:
# Import Ethereum Transaction Functions into the Fintech Finder Application

# In this section, you'll import several functions from the `crypto_wallet.py`
# script into the file `fintech_finder.py`, which contains code for Fintech
# Finder’s customer interface, in order to add wallet operations to the
# application. For this section, you will assume the perspective of a Fintech
# Finder customer (i.e., you’ll provide your Ethereum wallet and account
# information to the application).

# Complete the following steps:

# 1. Review the code contained in the `crypto_wallet.py` script file. Note that
# the Ethereum transaction functions that you have built throughout this
# module-including `wallet`, `wallet.derive_acount`, `get_balance`, `fromWei`,
# `estimateGas`, `sendRawTransaction`, and others&mdash;have now been
# incorporated into Python functions that allow you to automate the process of
# accessing them.

# 2. Add your mnemonic seed phrase and your Infura project id (both of which
# you created earlier in the module) to the starter code’s `SAMPLE.env` file.
# When the information has been added, rename the file `.env`.

# 3. Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# 4. Within the Streamlit sidebar section of code, create a variable named
# `account`. Set this variable equal to a call on the `generate_account`
# function. This function will create the Fintech Finder customer’s (in this
# case, your) HD wallet and Ethereum account.

# 5. Within this same section of the `fintech_finder.py` file, define a
# new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function
# and pass it your Ethereum `account.address`.

################################################################################
# Step 1 - Part 3:
# Import the following functions from the `crypto_wallet.py` file:
# * `generate_account`
# * `get_balance`
# * `send_transaction`

# @TODO:
# From `crypto_wallet.py import the functions generate_account, get_balance,
#  and send_transaction
from crypto_wallet import (
    generate_account,
    get_balance,
    send_transaction
)


import base64

from static.style import set_style


set_style()

################################################################################
# Fintech Finder Candidate Information

# Database of Fintech Finder candidates including their name, digital address, rating and hourly cost per Ether.
# A single Ether is currently valued at $1,500
candidate_database = {
    "Lane":    ["Lane",    "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", "4.3", .20, "img/lane.jpeg"],
    "Ash":     ["Ash",     "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", "5.0", .33, "img/ash.jpeg"],
    "Jo":      ["Jo",      "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.7", .19, "img/jo.jpeg"],
    "Kendall": ["Kendall", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", "4.1", .16, "img/kendall.jpeg"]
}

# A list of the FinTech Finder candidates first names
people = list(candidate_database.keys())


def get_condense_address(address):
    return f"{address[:5]}...{address[-4:]}"


def get_address_html(address, condense=True, html=True, type="address"):
    if condense:
        address_text = get_condense_address(address)
    else:
        address_text = address

    if html:
        return f"<a href='https://kovan.etherscan.io/{type}/{address}' target='_blank'>{address_text}</a>"
    else:
        return f"https://kovan.etherscan.io/{type}/{address_text}"


def get_people():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(candidate_database.values())

    for number in range(len(people)):
        name    = db_list[number][0]
        address = db_list[number][1]
        rating  = db_list[number][2]
        rate    = db_list[number][3]
        image   = base64.b64encode(open(db_list[number][4], 'rb').read()).decode()

        with st.expander(name):
            st.markdown(f"<img class='professional-photo' src='data:image/png;base64,{image}'><br>", unsafe_allow_html=True)

            _copycontent_button(
                str=address,
                lead_str="Ethereum Account Address:",
                copy_str=address,
                href=get_address_html(address),
                key=f"{name}-{address}",
                font_size="16px",
                font_weight="none",
                color="#122221",
                padding="0",
                margin="0px 0px 0px 0px",
                background="none",
            )

            st.markdown(f"<p class='expander-p'>Fintech Finder Rating: {rating}</p>"  , unsafe_allow_html=True)
            st.markdown(f"<p class='expander-p'>Hourly Rate per Ether: {rate} ETH</p>", unsafe_allow_html=True)


################################################################################
# Streamlit Code

# Streamlit application headings
page_title    = f"<h1 class='page-header'>🕵️ <span class='fintech-span'>Fintech</span> Finder 👩‍💻</h1>"
page_subtitle = f"<h2 class='page-subheader'>Hire A Fintech Professional!</h2>"
page_header   = f"<div><header>{page_title}{page_subtitle}</header></div>"

st.markdown(page_header, unsafe_allow_html=True)

################################################################################
# Streamlit Sidebar Code - Start
# st.sidebar.markdown("## Client Account Address and Ethernet Balance in Ether")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
account = generate_account()

##########################################

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
balance = get_balance(account.address)

style_kwargs = dict(
    color="#122221",
    font_size="14px",
    width="100%",
    padding="0px",
    margin="0 auto",
    text_align="center",
    background="none",
)

with st.sidebar:
    _crypto_account_stack(
        header_str="Client",
        address_str_val=get_condense_address(account.address),
        address_str_hdr="Address:",
        balance_str_val=f"{get_balance(account.address):.4f}",
        balance_str_unit="ETH",
        balance_str_hdr="Balance:",
        copy_str=account.address,
        href=get_address_html(account.address, condense=False, html=False),
        **style_kwargs,
    )

##########################################
with st.container():
    # Create a select box to chose a FinTech Hire candidate
    person = st.sidebar.selectbox('Select a Person', people)

    # Create a input field to record the number of hours the candidate worked
    hours = st.sidebar.number_input("Number of Hours")

    # Identify the FinTech Hire candidate
    candidate = candidate_database[person][0]

    # Write the Fintech Finder candidate's name to the sidebar
    st.sidebar.markdown(f"<p class='candidate-info-header'>{candidate}'s Info:</p>", unsafe_allow_html=True)

    # Identify the FinTech Finder candidate's ethereum address, rating, and hourly rate
    candidate_address     = candidate_database[person][1]
    candidate_rating      = candidate_database[person][2]
    candidate_hourly_rate = candidate_database[person][3]

    # Write the Fintech Finder candidate's ethereum address, rating, and hourly rate
    table_header = "|Address|Rating|Hourly Rate (ETH)|\n"
    table_sep    = "|:---:  |:---: |:---:            |\n"
    table_data   = f"|{get_address_html(candidate_address)}|{candidate_rating}|{candidate_hourly_rate}\n<br>"

    st.sidebar.markdown(table_header + table_sep + table_data, unsafe_allow_html=True)

################################################################################
# Step 2: Sign and Execute a Payment Transaction

# Complete the following steps:

# 1. Fintech Finder customers will select a fintech professional from the
# application interface’s drop-down menu, and then input the amount of time for
# which they’ll hire the worker. Code the application so that once a customer
# completes these steps, the application will calculate the amount that the
# worker will be paid in ether. To do so, complete the following steps:

    # * Write the equation that calculates the candidate’s wage. This equation
    #  should assess the candidate’s hourly rate from the candidate database
    # (`candidate_database[person][3]`) and then multiply this hourly rate by
    # the value of the `hours` variable. Save this calculation’s output as a
    # variable named `wage`.

    # * Write the `wage` variable to the Streamlit sidebar by
    # using `st.sidebar.write`.

# 2. Now that the application can calculate a candidate’s wage, write the code
# that will allow a customer (you, in this case) to send an Ethereum blockchain
# transaction that pays the hired candidate. To accomplish this, locate the
# code that reads `if st.sidebar.button("Send Transaction")`. You’ll need to
# add logic to this `if` statement that sends the appropriate information to
# the `send_transaction` function (which you imported from the `crypto_wallet`
# script file). Inside the `if` statement, add the following functionality:

    # * Call the `send_transaction()` function and pass it three parameters:
        # - Your Ethereum `account` information. (Remember that this `account`
        # instance was created when the `generate_account` function was called.)
        #  From the `account` instance, the application will be able to access the
        #  `account.address` information that is needed to populate the `from` data
        # attribute in the raw transaction.
        #- The `candidate_address` (which will be created and identified in the
        # sidebar when a customer selects a candidate). This will populate the `to`
        # data attribute in the raw transaction.
        # - The `wage` value. This will be passed to the `toWei` function to
        # determine the wei value of the payment in the raw transaction.

    # * Save the transaction hash that the `send_transaction` function returns
    # as a variable named `transaction_hash`, and have it display on the
    # application’s web interface.

##########################################
# Step 2 - Part 1:
# * Write the equation that calculates the candidate’s wage. This equation
# should assess the candidate’s hourly rate from the candidate database
# (`candidate_database[person][3]`) and then multiply this hourly rate by
# the value of the `hours` variable. Save this calculation’s output as a
# variable named `wage`.
# * Write the `wage` variable to the Streamlit sidebar by using `st.sidebar.write`.

# @TODO
# Calculate total `wage` for the candidate by multiplying the candidate’s hourly
# rate from the candidate database (`candidate_database[person][3]`) by the
# value of the `hours` variable
wage = candidate_database[person][3] * hours

# @TODO
# Write the `wage` calculation to the Streamlit sidebar
st.sidebar.markdown(f"<p class='wage-text' style='text-align:center'><strong>Total Wage</strong>: {wage:.4f} (ETH)</p>", unsafe_allow_html=True)

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.
if st.sidebar.button("Send Transaction 🤝🏽"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    try:
        transaction_hash = send_transaction(account, candidate_address, wage).hex()

        # Markdown for the transaction hash
        with st.sidebar:        
            _copycontent_button(
                str=get_condense_address(transaction_hash),
                lead_str="Transaction Hash:",
                copy_str=transaction_hash,
                href=get_address_html(transaction_hash, condense=False, html=False, type="tx"),
                font_size="16px",
                font_weight="none",
                color="#122221",
                padding="0",
                margin="0",
                background="none",
            )

        # Celebrate your successful payment
        st.balloons()
    except Exception as e:
        print(e)

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
st.text(" \n")
get_people()


################################################################################
# Step 3: Inspect the Transaction on Etherscan

# Send a test transaction by using the application’s web interface, and then
# look up the resulting transaction hash on the Kovan Etherscan block explorer
# to verify the transactions.

# Complete the following steps:

# 1. From your terminal, navigate to the project folder that contains
# your `.env` file and the `fintech_finder.py` and `crypto_wallet.py` files.
# Be sure to activate your Conda `dev` environment if it is not already active.

# 2. To launch the Streamlit application,
# type `streamlit run fintech_finder.py`.

# 3. On the resulting webpage, select a candidate that you would like to hire
# from the appropriate drop-down menu. Then, enter the number of hours that you
# would like to hire them for. (Remember, you do not have a lot of ether in
# your account, so you cannot hire them for long!)

# 4 Click the Send Transaction button to sign and send the transaction with
# your Ethereum account information. If the transaction is successfully
# communicated to the Ethereum Kovan testnet, validated, and added to a block,
# a resulting transaction hash code will be written to the Streamlit
# application sidebar.

# 5. Copy the customer’s (your) Ethereum address from the Streamlit application
# page, and navigate to [Kovan Etherscan](https://kovan.etherscan.io/).
# Paste your copied Ethereum address into the Kovan Etherscan search bar.
    # * Take a screenshot of your address balance and history on Etherscan.
    # Save this screenshot to the README.md file of your GitHub repository for
    #  this Challenge assignment.

# 6. On the Kovan Etherscan page, click on the Txn Hash number associated with
# the transaction that paid the Fintech Finder candidate.
    # * Take a screenshot of the transaction details on Etherscan. Save this
    # screenshot to the README.md file of your GitHub repository for this
    # Challenge assignment.

# 7. Return to the original transaction, and click the transaction’s To address.
    # * Take a screenshot of the recipient’s address balance and history on
    # Etherscan. Save this screenshot to the README.md file of your GitHub
    # repository for this Challenge assignment.
