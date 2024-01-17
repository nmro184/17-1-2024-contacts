from faker import Faker
import sqlite3


def add_contacts(a): 
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        
        for i in range(a):
            profile = Faker().simple_profile()
            phone = Faker().phone_number()
            rows = cur.execute(f"INSERT INTO contacts (name , email , phone ) VALUES ('{profile['name']}' , '{profile['mail']}' , '{phone}' )")
        print (rows)
        return rows.fetchall()
    
add_contacts(50)