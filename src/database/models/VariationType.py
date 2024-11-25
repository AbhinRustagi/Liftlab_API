from src.database.models.BaseModel import BaseModel

from peewee import CharField, AutoField

class VariationType(BaseModel):
    '''
    VariationType model
    '''
    id = AutoField(primary_key=True)
    name = CharField(unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def __repr__(self):
        return f'{self.name}'
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __ne__(self, other):
        return self.name != other.name