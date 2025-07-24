import streamlit as st
from bank import Bank

Bank.load_data()
st.set_page_config(page_title="Bank App", layout="centered")

st.title("🏦 Simple Bank System")

menu = st.sidebar.selectbox("Choose Action", [
    "Create Account", "Deposit", "Withdraw", "View Details", "Update Info", "Delete Account"
])

if menu == "Create Account":
    st.subheader("Create a New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if not (name and email and pin.isdigit()):
            st.error("All fields are required.")
        else:
            success, result = Bank.create_account(name, int(age), email, int(pin))
            if success:
                st.success("Account Created!")
                st.json(result)
            else:
                st.error(result)

elif menu == "Deposit":
    st.subheader("Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)

    if st.button("Deposit"):
        success, message = Bank.deposit(acc, int(pin), int(amount))
        st.success(message) if success else st.error(message)

elif menu == "Withdraw":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)

    if st.button("Withdraw"):
        success, message = Bank.withdraw(acc, int(pin), int(amount))
        st.success(message) if success else st.error(message)

elif menu == "View Details":
    st.subheader("View Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        success, user = Bank.get_details(acc, int(pin))
        st.json(user) if success else st.error(user)

elif menu == "Update Info":
    st.subheader("Update Account Info")
    acc = st.text_input("Account Number")
    pin = st.text_input("Current PIN", type="password")
    new_name = st.text_input("New Name")
    new_email = st.text_input("New Email")
    new_pin = st.text_input("New PIN (4 digits)", type="password")

    if st.button("Update"):
        success, msg = Bank.update_details(acc, int(pin), new_name or None, new_email or None, int(new_pin) if new_pin else None)
        st.success(msg) if success else st.error(msg)

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        success, msg = Bank.delete_account(acc, int(pin))
        st.success(msg) if success else st.error(msg)
