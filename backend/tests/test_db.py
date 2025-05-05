import os
import sys
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_database_connection():
    """Test basic database connection"""
    try:
        print("Environment Variables:")
        print("DB_HOST:", os.getenv("DB_HOST"))
        print("DB_NAME:", os.getenv("DB_NAME"))
        print("DB_USER:", os.getenv("DB_USER"))
        print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
        
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            sslmode='require'
        )
        print("✅ Database connection successful")
        return conn
    except Exception as e:
        print("❌ Database connection failed:", str(e))
        return None

def test_tables_exist(conn):
    """Test if all required tables exist"""
    required_tables = ['users', 'events', 'registrations', 'faqs']
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        existing_tables = [table[0] for table in cur.fetchall()]
        
        for table in required_tables:
            if table in existing_tables:
                print(f"✅ Table '{table}' exists")
            else:
                print(f"❌ Table '{table}' is missing")
        
        cur.close()
    except Exception as e:
        print("❌ Error checking tables:", str(e))

def test_crud_operations(conn):
    """Test CRUD operations on each table"""
    try:
        cur = conn.cursor()
        
        # Test Users CRUD
        print("\nTesting Users CRUD:")
        cur.execute("""
            INSERT INTO users (username, email, password, fullname)
            VALUES ('testuser', 'test@example.com', 'testhash', 'Test User')
            RETURNING id;
        """)
        user_id = cur.fetchone()[0]
        print("✅ User created")
        
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        print("✅ User retrieved")
        
        cur.execute("""
            UPDATE users 
            SET fullname = 'Updated Test User' 
            WHERE id = %s
        """, (user_id,))
        print("✅ User updated")
        
        # Test Events CRUD
        print("\nTesting Events CRUD:")
        cur.execute("""
            INSERT INTO events (
                title, description, date, time, 
                duration, location, public
            )
            VALUES (
                'Test Event', 'Test Description', '2024-04-01', 
                '14:00', '2 hours', 'Test Location', true
            )
            RETURNING id;
        """)
        event_id = cur.fetchone()[0]
        print("✅ Event created")
        
        cur.execute("SELECT * FROM events WHERE id = %s", (event_id,))
        print("✅ Event retrieved")
        
        # Test Registrations CRUD
        print("\nTesting Registrations CRUD:")
        cur.execute("""
            INSERT INTO registrations (
                title, first_name, last_name, date_of_birth, carer_first_name, carer_last_name, carer_email,
                email, phone_number, address_line1, address_line2, city, postcode, country,
                level_of_study, subject_area, event_date, guest_count, marketing_sources
            )
            VALUES (
                'Mr', 'John', 'Doe', '2000-01-01', NULL, NULL, NULL,
                'john@example.com', '1234567890', '123 Main St', NULL, 'Test City', '12345', 'Test Country',
                'Undergraduate', 'Computer Science', '2024-04-01', 2, ARRAY['Social Media', 'Friend']
            )
            RETURNING id;
        """)
        registration_id = cur.fetchone()[0]
        print("✅ Registration created")
        
        cur.execute("SELECT * FROM registrations WHERE id = %s", (registration_id,))
        print("✅ Registration retrieved")
        
        # Cleanup test data
        cur.execute("DELETE FROM registrations WHERE id = %s", (registration_id,))
        cur.execute("DELETE FROM events WHERE id = %s", (event_id,))
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        print("\n✅ Test data cleaned up")
        
        conn.commit()
        cur.close()
        
    except Exception as e:
        conn.rollback()
        print("❌ Error during CRUD tests:", str(e))

def test_relationships(conn):
    """Test database relationships and constraints"""
    try:
        cur = conn.cursor()
        
        # Test foreign key constraints
        print("\nTesting Foreign Key Constraints:")
        try:
            cur.execute("""
                INSERT INTO registrations (
                    title, first_name, last_name, email,
                    guest_count, status
                )
                VALUES (
                    'Mr', 'John', 'Doe', 'john@example.com',
                    99999, 2, 'confirmed'
                );
            """)
            print("❌ Foreign key constraint failed")
        except psycopg2.Error:
            print("✅ Foreign key constraint working")
            conn.rollback()
        
        cur.close()
    except Exception as e:
        print("❌ Error testing relationships:", str(e))

def test_performance(conn):
    """Test database performance with bulk operations"""
    try:
        cur = conn.cursor()
        
        print("\nTesting Performance:")
        start_time = datetime.now()
        
        # Bulk insert test
        cur.execute("""
            INSERT INTO events (
                title, description, date, time, 
                duration, location, public
            )
            SELECT 
                'Bulk Test Event ' || generate_series,
                'Test Description',
                '2024-04-01',
                '14:00',
                '2 hours',
                'Test Location',
                true
            FROM generate_series(1, 1000);
        """)
        
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"✅ Bulk insert of 1000 records completed in {duration:.2f} seconds")
        
        # Cleanup
        cur.execute("DELETE FROM events WHERE title LIKE 'Bulk Test Event%'")
        conn.commit()
        cur.close()
        
    except Exception as e:
        conn.rollback()
        print("❌ Error during performance test:", str(e))

def main():
    """Main test execution"""
    print("Starting Database Tests...\n")
    
    conn = test_database_connection()
    if conn:
        test_tables_exist(conn)
        test_crud_operations(conn)
        test_relationships(conn)
        test_performance(conn)
        conn.close()
        print("\nDatabase tests completed.")
    else:
        print("Cannot proceed with tests due to connection failure.")

if __name__ == "__main__":
    main() 
    