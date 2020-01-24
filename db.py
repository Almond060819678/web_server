from peewee import *
import datetime
import os

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
db_name = os.environ['POSTGRES_DB']
host = os.environ['POSTGRES_HOST']

db_handler = PostgresqlDatabase(
    db_name, user=user,
    host=host, password=password
)


class BaseModel(Model):
    class Meta:
        database = db_handler


class News(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "core_news"
        order_by = ('created_at',)
