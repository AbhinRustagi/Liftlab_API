from enum import Enum

from peewee import CharField, CompositeKey, ForeignKeyField, IntegerField

from src.models.BaseModel import BaseModel
from src.models.Exercise import Exercise
from src.models.Workout import Workout


class SetsTypeEnum(Enum):
    PROGRESSIVE = 'progressive_weight'
    FIXED = 'fixed'
    TIMED = 'timed'
    DROPSET = 'dropset'
    SUPERSET = 'superset'
    GIANTSET = 'giantset'


class WorkoutExercise(BaseModel):
    workout = ForeignKeyField(Workout)
    exercise = ForeignKeyField(Exercise)
    sets = IntegerField()
    sets_type = CharField(choices=[(item.value, item.value) for item in SetsTypeEnum])
    
    class Meta:
        primary_key = CompositeKey('workout', 'exercise')
