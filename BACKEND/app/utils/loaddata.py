import pandas as pd
from sqlalchemy.orm import Session
from app.models import Transaction
from app.config import SessionLocal
from datetime import datetime

def load_data(csv_file='app/models/fake_transactions.csv'):
    df = pd.read_csv(csv_file)
    db: Session = SessionLocal()
    for _, row in df.iterrows():
        transaction = Transaction(
            account_holder=row['account_holder'],
            contact_number=row['contact_number'],
            account_number=row['account_number'],
            current_location=row['current_location'],
            transaction_amount=row['transaction_amount'],
            transaction_history=datetime.fromisoformat(row['transaction_history']),
            is_mule=row['is_mule']
        )
        db.add(transaction)
    db.commit()
    db.close()
    print("Data loaded into the database successfully.")

if __name__ == "__main__":
    load_data()
