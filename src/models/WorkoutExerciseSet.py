from peewee import CompositeKey, ForeignKeyField, IntegerField

from src.models.BaseModel import BaseModel
from src.models.WorkoutExercise import WorkoutExercise


class WorkoutExerciseSet(BaseModel):
    workout_exercise = ForeignKeyField(WorkoutExercise, backref='sets')
    set_no = IntegerField()
    reps = IntegerField()

    class Meta:
        primary_key = CompositeKey('workout', 'exercise', 'set_no')