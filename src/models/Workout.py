from peewee import CharField, ForeignKeyField, UUIDField

from src.models.BaseModel import BaseModel
from src.models.User import User


class Workout(BaseModel):
    id = UUIDField(primary_key=True)
    name = CharField()
    description = CharField()
    user = ForeignKeyField(User, backref='workouts')
