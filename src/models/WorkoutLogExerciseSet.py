# WorkoutLogExerciseSet(log_id, workout_exercise_set_id, completed_reps)
from peewee import CompositeKey, ForeignKeyField, IntegerField

from src.models.BaseModel import BaseModel
from src.models.WorkoutExerciseSet import WorkoutExerciseSet
from src.models.WorkoutLog import WorkoutLog


class WorkoutLogExerciseSet(BaseModel):
    log_id = ForeignKeyField(WorkoutLog, backref='exercise_sets')
    workout_exercise_set_id = ForeignKeyField(WorkoutExerciseSet, backref='logs')
    completed_reps = IntegerField()
    weight = IntegerField()

    class Meta:
        primary_key = CompositeKey('log_id', 'workout_exercise_set_id')