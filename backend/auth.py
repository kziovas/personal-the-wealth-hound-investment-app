from typing import Optional

from sqlalchemy.orm import Session

from backend.models import User


def signup(
    db: Session,
    name: str,
    surname: str,
    email: str,
    password: str,
    base_currency: str,
    target_return_pct: float,
    risk_tolerance: str,
) -> User:
    """
    Create a new user in the database.

    Parameters:
    - db: SQLAlchemy Session
    - name, surname, email, password: User credentials
    - base_currency: User's base currency
    - target_return_pct: Required target return %
    - risk_tolerance: Required risk tolerance ('low', 'medium', 'high')

    Returns:
    - Created User object
    """
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValueError("Email already exists")

    user = User(
        name=name,
        surname=surname,
        email=email,
        password=password,
        base_currency=base_currency,
        target_return_pct=target_return_pct,
        risk_tolerance=risk_tolerance,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login(db: Session, email: str, password: str) -> Optional[User]:
    """
    Simple login by email and password.

    Parameters:
    - db: SQLAlchemy Session
    - email: User email
    - password: User password

    Returns:
    - User object if credentials match, None otherwise
    """
    user = db.query(User).filter(User.email == email, User.password == password).first()
    return user
