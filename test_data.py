from faker import Faker
import sqlite3


def add_contacts(a): 
    with sqlite3.connect("contacts.db") as conn:
        cur = conn.cursor()
        
        for i in range(a):
            profile = Faker(locale = "he_IL").simple_profile()
            phone = Faker(locale = "he_IL").phone_number()
            rows = cur.execute(f"INSERT INTO contacts (name , email , phone ) VALUES ('{profile['name']}' , '{profile['mail']}' , '{phone}' )")
        print (rows)
        return rows.fetchall()
    
add_contacts(15)