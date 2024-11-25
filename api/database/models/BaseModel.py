from datetime import datetime

from peewee import DateTimeField, Model, SqliteDatabase

db = SqliteDatabase('app.db')

class BaseModel(Model):
    '''
    Base model for all models
    '''
    created = DateTimeField(default=datetime.now)
    updated = DateTimeField(default=datetime.now)

    class Meta:
        '''
        Meta class for BaseModel
        '''
        database = db
