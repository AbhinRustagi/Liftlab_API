from peewee import CharField, ForeignKeyField, UUIDField

from api.database.models.BaseModel import BaseModel
from api.database.models.MuscleGroup import MuscleGroup


class Muscle(BaseModel):
    '''
    Muscle model
    '''
    id = UUIDField(primary_key=True)
    name = CharField()
    muscle_group = ForeignKeyField(MuscleGroup, backref='muscles')
    
    def __str__(self):
        return f'{self.name} | {self.muscle_group}'
    
    def __repr__(self):
        return f'{self.name} | {self.muscle_group}'
    
    def __eq__(self, other):
        return self.name == other.name and self.muscle_group == other.muscle_group
    
    def __ne__(self, other):
        return self.name != other.name or self.muscle_group != other.muscle_group