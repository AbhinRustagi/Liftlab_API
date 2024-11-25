from peewee import CharField, ForeignKeyField

from src.database.models.BaseModel import BaseModel
from src.database.models.User import User

class UserPreference(BaseModel):
    '''
    UserPreference model
    '''
    user = ForeignKeyField(User, primary_key=True)
    preferred_unit = CharField()
    preferred_equipment = CharField()
    preferred_muscle_group = CharField()

    def __str__(self):
        return f'{self.user} | {self.preferred_unit} | {self.preferred_muscle_group} | {self.preferred_equipment}'
    
    def __repr__(self):
        return f'{self.user} | {self.preferred_unit} | {self.preferred_muscle_group} | {self.preferred_equipment}'