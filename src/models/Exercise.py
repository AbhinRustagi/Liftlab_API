from peewee import CharField, ForeignKeyField, UUIDField

from src.models.Tag import Tag
from src.models.BaseModel import BaseModel

class Exercise(BaseModel):
    '''
    Exercise model
    '''
    id = UUIDField(primary_key=True)
    name = CharField()
    tag = ForeignKeyField(Tag, backref='exercises')
    equipment_required = CharField()
    difficulty = CharField()
    
    def __str__(self):
        return f'{self.name} | {self.tag}'
    
    def __repr__(self):
        return f'{self.name} | {self.tag}'
    
    def __eq__(self, other):
        return self.name == other.name and self.tag == other.tag
    
    def __ne__(self, other):
        return self.name != other.name or self.tag != other.tag