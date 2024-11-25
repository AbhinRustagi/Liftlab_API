import uuid
from peewee import CharField, UUIDField
from src.database.models.BaseModel import BaseModel

class User(BaseModel):
    user_id = UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = CharField()
    last_name = CharField(null=True)
    email = CharField(unique=True)
    password = CharField()
    username = CharField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.email} | {self.username}'
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name} | {self.email} | {self.username}'
    
    def __eq__(self, other):
        return self.email == other.email and self.username == other.username
    
    def __ne__(self, other):
        return self.email != other.email or self.username != other.username
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
