import pandas as pd
import numpy as np
from faker import Faker
from app.models import Transaction

import random

fake = Faker()

def generate_fake_data(num_records=1000):
    data = []
    for _ in range(num_records):
        account_holder = fake.name()
        contact_number = fake.phone_number()
        account_number = fake.bban()
        current_location = f"{fake.latitude()}, {fake.longitude()}"
        transaction_amount = round(random.uniform(10, 10000), 2)
        transaction_history = fake.date_time_between(start_date='-1y', end_date='now').isoformat()
        is_mule = random.choice([0, 1])  # 0: Regular, 1: Mule Account
        data.append({
            'account_holder': account_holder,
            'contact_number': contact_number,
            'account_number': account_number,
            'current_location': current_location,
            'transaction_amount': transaction_amount,
            'transaction_history': transaction_history,
            'is_mule': is_mule
        })
    df = pd.DataFrame(data)
    df.to_csv('fake_transactions.csv', index=False)
    print("Fake dataset generated successfully.")

if __name__ == "__main__":
    generate_fake_data()
