from peewee import CharField, ForeignKeyField, UUIDField

from src.database.models.BaseModel import BaseModel
from src.database.models.User import User


class Workout(BaseModel):
    '''
    Workout model
    '''
    id = UUIDField(primary_key=True)
    name = CharField()
    description = CharField()
    user = ForeignKeyField(User, backref='workouts')

    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name
