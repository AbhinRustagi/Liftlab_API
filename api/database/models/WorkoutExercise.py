from enum import Enum

from peewee import CharField, CompositeKey, ForeignKeyField, IntegerField, UUIDField

from api.database.models.BaseModel import BaseModel
from api.database.models.Exercise import Exercise
from api.database.models.Workout import Workout


class SetsTypeEnum(Enum):
    PROGRESSIVE = 'progressive_weight'
    FIXED = 'fixed'
    TIMED = 'timed'
    DROPSET = 'dropset'
    SUPERSET = 'superset'
    GIANTSET = 'giantset'


class WorkoutExercise(BaseModel):
    id = UUIDField(primary_key=True)
    workout = ForeignKeyField(Workout)
    exercise = ForeignKeyField(Exercise)
    sets = IntegerField()
    sets_type = CharField(choices=[(item.name, item.value) for item in SetsTypeEnum])
    