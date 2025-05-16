import streamlit as st

st.set_page_config(page_title="$5 Flip Tracker", layout="centered")
st.title("$5 Flip Risk Tracker")

# Initialize session state
if "balance" not in st.session_state:
    st.session_state.balance = 5.0
if "history" not in st.session_state:
    st.session_state.history = []

# Input risk amount
risk = st.number_input("Risk per Trade ($)", min_value=0.1, max_value=5.0, value=2.0, step=0.1)

# Display current balance
st.metric("Current Balance", f"${st.session_state.balance:.2f}")

# Calculate remaining trades
trades_left = int(st.session_state.balance // risk)
st.write(f"Trades Remaining at current risk: {trades_left}")

col1, col2 = st.columns(2)

# Define win and loss buttons
with col1:
    if st.button("Win Trade"):
        st.session_state.balance += risk
        st.session_state.history.append(("Win", risk, st.session_state.balance))

with col2:
    if st.button("Lose Trade"):
        st.session_state.balance -= risk
        st.session_state.history.append(("Loss", -risk, st.session_state.balance))
        if st.session_state.balance <= 0:
            st.warning("Account busted! Reload to restart.")

# History
if st.session_state.history:
    st.subheader("Trade History")
    for i, (result, change, bal) in enumerate(reversed(st.session_state.history), 1):
        st.write(f"{i}. {result}: {'+' if change > 0 else ''}${change:.2f} → ${bal:.2f}")

# Reset
if st.button("Reset Tracker"):
    st.session_state.balance = 5.0
    st.session_state.history = []
    st.success("Tracker reset to $5.")
