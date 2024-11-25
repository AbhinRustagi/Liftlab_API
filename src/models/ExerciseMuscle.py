from enum import Enum

from peewee import CharField, ForeignKeyField, UUIDField

from src.models.BaseModel import BaseModel
from src.models.Exercise import Exercise
from src.models.Muscle import Muscle


class TargetEnum(Enum):
    '''
    TargetEnum class
    '''
    PRIMARY = 'Primary'
    SECONDARY = 'Secondary'
    STABILIZER = 'Stabilizer'


class ExerciseMuscle(BaseModel):
    '''
    ExerciseMuscle model
    '''
    id = UUIDField(primary_key=True)
    exercise = ForeignKeyField(Exercise, backref='muscles')
    muscle = ForeignKeyField(Muscle, backref='exercises')
    target = CharField(choices=[(target.key, target.value) for target in TargetEnum])
    
    def __str__(self):
        return f'{self.exercise} | {self.muscle}'
    
    def __repr__(self):
        return f'{self.exercise} | {self.muscle}'
    
    def __eq__(self, other):
        return self.exercise == other.exercise and self.muscle == other.muscle
    
    def __ne__(self, other):
        return self.exercise != other.exercise or self.muscle != other.muscle