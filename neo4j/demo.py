import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load Neo4j credentials from .env
load_dotenv()
URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD")

class Neo4jCRUD:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def test_connection(self):
        try:
            self.driver.verify_connectivity()
            print("Connection successful!")
        except Exception as e:
            print(f"Connection failed: {str(e)}")

    # Create operation
    def create_person(self, name, age):
        with self.driver.session() as session:
            result = session.execute_write(
                lambda tx: tx.run("CREATE (p:Person {name: $name, age: $age}) RETURN p",
                                name=name, age=age).data())
            return result

    # Read operation
    def get_person(self, name):
        with self.driver.session() as session:
            result = session.execute_read(
                lambda tx: tx.run("MATCH (p:Person {name: $name}) RETURN p",
                                name=name).data())
            return result

    # Update operation
    def update_person_age(self, name, new_age):
        with self.driver.session() as session:
            result = session.execute_write(
                lambda tx: tx.run("MATCH (p:Person {name: $name}) SET p.age = $age RETURN p",
                                name=name, age=new_age).data())
            return result

    # Delete operation
    def delete_person(self, name):
        with self.driver.session() as session:
            result = session.execute_write(
                lambda tx: tx.run("MATCH (p:Person {name: $name}) DELETE p",
                                name=name))
            return "Person deleted successfully"

# Main execution
if __name__ == "__main__":
    # Create instance
    db = Neo4jCRUD(URI, USER, PASSWORD)
    
    try:
        # Test connection
        db.test_connection()
        
        # # Create a person
        # print("\nCreating person...")
        # result = db.create_person("John", 30)
        # print(f"Created: {result}")
        
        # # Read person
        print("\nReading person...")
        result = db.get_person("John")
        print(f"Found: {result}")
        
        # # Update person
        # print("\nUpdating person...")
        # result = db.update_person_age("John", 31)
        # print(f"Updated: {result}")
        
        # # Delete person
        # print("\nDeleting person...")
        # result = db.delete_person("John")
        # print(result)
        
    finally:
        # Close the connection
        db.close()