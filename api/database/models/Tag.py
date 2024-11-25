from peewee import CharField, UUIDField

from api.database.models.BaseModel import BaseModel

class Tag(BaseModel):
    '''
    Tag model
    '''
    id = UUIDField(primary_key=True)
    name = CharField()

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name