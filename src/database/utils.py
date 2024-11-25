from peewee import Model


from src.database.models import models, db

# Initialize the database

def connect_db():
    '''
    Connect to the database
    '''
    if db.is_closed():
        db.connect()

def close_db():
    '''
    Close the database
    '''
    if not db.is_closed():
        db.close()

def initialize_models():
    '''
    Create the tables in the database
    '''
    db.connect()
    try:
        db.create_tables(models)
        print('Tables created successfully')
    except Exception as e:
        print('Error creating tables')
        print(e)

    db.close()