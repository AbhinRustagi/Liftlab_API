from peewee import ForeignKeyField, IntegerField, UUIDField

from src.database.models.BaseModel import BaseModel
from src.database.models.WorkoutExercise import WorkoutExercise


class WorkoutExerciseSet(BaseModel):
    id = UUIDField(primary_key=True)
    workout_exercise = ForeignKeyField(WorkoutExercise, backref='sets')
    set_no = IntegerField()
    reps = IntegerField()

    class Meta:
        unique_together = ('workout_exercise', 'set_no')