# WorkoutLogExerciseSet(log_id, workout_exercise_set_id, completed_reps)
from peewee import CompositeKey, ForeignKeyField, IntegerField

from api.database.models.BaseModel import BaseModel
from api.database.models.WorkoutExerciseSet import WorkoutExerciseSet
from api.database.models.WorkoutLog import WorkoutLog


class WorkoutLogExerciseSet(BaseModel):
    '''
    Model for workout log exercise set
    '''
    log_id = ForeignKeyField(WorkoutLog, backref='exercise_sets')
    workout_exercise_set_id = ForeignKeyField(WorkoutExerciseSet, backref='logs')
    completed_reps = IntegerField()
    weight = IntegerField()

    class Meta:
        '''
        Meta class for WorkoutLogExerciseSet
        '''
        primary_key = CompositeKey('log_id', 'workout_exercise_set_id')