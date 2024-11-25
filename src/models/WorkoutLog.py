from peewee import (DateField, ForeignKeyField, IntegerField, TextField,
                    UUIDField)

from src.models.BaseModel import BaseModel
from src.models.Workout import Workout


class WorkoutLog(BaseModel):
    id = UUIDField(primary_key=True)
    date = DateField()
    workout = ForeignKeyField(Workout)
    duration = IntegerField()
    notes = TextField()

    def __str__(self):
        return f'{self.date} | {self.workout}'
    
    def __repr__(self):
        return f'{self.date} | {self.workout}'
