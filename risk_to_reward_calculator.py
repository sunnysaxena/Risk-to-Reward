# import the streamlit library
import streamlit as st


def risk_to_reward_ratio(entry_price, stop_loss_price, take_profit_price):
    potential_reward = take_profit_price - entry_price
    potential_risk = entry_price - stop_loss_price
    if potential_risk == 0:
        return "Cannot calculate risk-to-reward ratio: division by zero"
    else:
        return potential_reward / potential_risk


def print_risk_to_reward(rr_ratio):
    print("Risk-to-Reward Ratio:", rr_ratio)

    rr_ratio = float(rr_ratio)
    print(rr_ratio)

    if rr_ratio >= 100:
        return "This trade meets the criteria of 1:100 risk-to-reward ratio.", "1:100"

    elif rr_ratio >= 60:
        return "This trade meets the criteria of 1:60 risk-to-reward ratio.", "1:60"

    elif rr_ratio >= 30:
        return "This trade meets the criteria of 1:30 risk-to-reward ratio.", "1:30"

    elif rr_ratio >= 20:
        return "This trade meets the criteria of 1:20 risk-to-reward ratio.", "1:20"

    elif rr_ratio >= 10:
        return "This trade meets the criteria of 1:10 risk-to-reward ratio.", "1:10"

    elif rr_ratio >= 9:
        return "This trade meets the criteria of 1:9 risk-to-reward ratio.", "1:9"

    elif rr_ratio >= 8:
        return "This trade meets the criteria of 1:8 risk-to-reward ratio.", "1:8"

    elif rr_ratio >= 7:
        return "This trade meets the criteria of 1:7 risk-to-reward ratio.", "1:7"

    elif rr_ratio >= 6:
        return "This trade meets the criteria of 1:6 risk-to-reward ratio.", "1:6"

    elif rr_ratio >= 5:
        return "This trade meets the criteria of 1:5 risk-to-reward ratio.", "1:5"

    elif rr_ratio >= 4:
        return "This trade meets the criteria of 1:4 risk-to-reward ratio.", "1:4"

    elif rr_ratio >= 3:
        return "This trade meets the criteria of 1:3 risk-to-reward ratio.", "1:3"

    elif rr_ratio >= 2:
        return "This trade meets the criteria of 1:2 risk-to-reward ratio.", "1:2"

    elif rr_ratio >= 1:
        return "This trade meets the criteria of 1:2 risk-to-reward ratio.", "1:1"

    elif rr_ratio >= -2:
        return "This trade meets the criteria of 2:1 risk-to-reward ratio.", "2:1"

    elif rr_ratio >= -3:
        return "This trade meets the criteria of 3:1 risk-to-reward ratio.", "3:1"

    elif rr_ratio >= -4:
        return "This trade meets the criteria of 4:1 risk-to-reward ratio.", "4:1"
    else:
        return "This trade does not meet the criteria of any risk-to-reward ratio."


# give a title to our app
st.title('Risk to Reward Calculator')

# TAKE WEIGHT INPUT in kgs
entry_price = st.number_input("Enter your entry price (in number)", value=50,
                              placeholder="type an entry price")
stop_loss_price = st.number_input("Enter your stop loss price (in number)", value=45,
                                  placeholder="type a stop loss ""price")
take_profit_price = st.number_input("Enter your take profit price (in number)", value=60,
                                    placeholder="type a take profit price")

rr_ratio = risk_to_reward_ratio(entry_price, stop_loss_price, take_profit_price)
print(type(rr_ratio))
print_rr = print_risk_to_reward(rr_ratio)

# check if the button is pressed or not
if st.button('Calculate Risk to Reward'):
    st.text("Risk-to-Reward ratio is : {0}".format(rr_ratio))
    st.subheader("Risk-to-Reward ratio is : {0}".format(print_rr[1]))

    print("Risk-to-Reward Ratio:", rr_ratio)

    if rr_ratio >= 3:
        st.success("Excellent")
    elif rr_ratio >= 2:
        st.success("Good")
    else:
        st.error(" Require Improvement...")
