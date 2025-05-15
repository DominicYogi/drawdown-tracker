import streamlit as st

def drawdown_tracker(starting_balance, static_dd_percent, daily_dd_percent, balances):
    static_dd_value = starting_balance * (static_dd_percent / 100)
    static_floor = starting_balance - static_dd_value

    results = []
    for day, balance in enumerate(balances, start=1):
        daily_dd_limit = balance * (daily_dd_percent / 100)
        min_allowed_today = balance - daily_dd_limit
        status = "✅ OK"
        if balance < static_floor:
            status = "❌ Breached Static DD"
        elif balance < min_allowed_today:
            status = "❌ Breached Daily DD"

        results.append({
            "Day": f"Day {day}",
            "Balance": balance,
            "Daily DD Limit": round(daily_dd_limit, 2),
            "Min Allowed Today": round(min_allowed_today, 2),
            "Static Floor": round(static_floor, 2),
            "Status": status
        })

    return results

st.title("Drawdown Tracker Tool for Prop Firm Challenges")

starting_balance = st.number_input("Starting Balance ($)", value=2000)
static_dd_percent = st.number_input("Static Drawdown (%)", value=3.0)
daily_dd_percent = st.number_input("Daily Drawdown (%)", value=2.0)

balance_input = st.text_area("Enter Daily Balances (comma-separated)", "2500, 2450, 2400, 2350, 2300")

if st.button("Calculate"):
    try:
        balances = list(map(float, balance_input.split(',')))
        results = drawdown_tracker(starting_balance, static_dd_percent, daily_dd_percent, balances)

        st.write("### Results:")
        st.table(results)
    except Exception as e:
        st.error(f"Error: {e}")
