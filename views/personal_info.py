import streamlit as st
from sqlalchemy.orm import Session

from backend.auth import login, signup
from backend.models import User
from views.layout import render_page_header


def render(db: Session):
    """
    Render the personal info page with signup/login forms.
    """
    render_page_header("Personal Info")

    action = st.radio("Action", ["Signup", "Login"])

    if action == "Signup":
        with st.form("signup_form"):
            name = st.text_input("Name")
            surname = st.text_input("Surname")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            base_currency = st.selectbox("Base Currency", ["USD", "EUR", "GBP"])
            target_return_pct = st.number_input(
                "Target Return (%)", min_value=0.0, max_value=100.0, value=5.0
            )
            risk_tolerance = st.selectbox("Risk Tolerance", ["low", "medium", "high"])
            submitted = st.form_submit_button("Signup")

            if submitted:
                try:
                    user: User = signup(
                        db,
                        name,
                        surname,
                        email,
                        password,
                        base_currency,
                        target_return_pct,
                        risk_tolerance,
                    )
                    st.success(f"User {user.email} signed up successfully!")
                except Exception as e:
                    st.error(str(e))

    else:  # Login
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")

            if submitted:
                user = login(db, email, password)
                if user:
                    st.success(f"Welcome back, {user.name}!")
                    st.session_state["user_id"] = user.id
                else:
                    st.error("Invalid email or password")
