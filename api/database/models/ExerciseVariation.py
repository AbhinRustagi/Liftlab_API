from peewee import CharField, ForeignKeyField, UUIDField

from api.database.models.BaseModel import BaseModel
from api.database.models.Exercise import Exercise
from api.database.models.VariationType import VariationType


class ExerciseVariation(BaseModel):
    '''
    VariationType model
    '''
    id = UUIDField(primary_key=True)
    exercise = ForeignKeyField(Exercise, backref='variations')
    variation_type = ForeignKeyField(VariationType, backref='variations', null=True)
    name = CharField()
    
    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name