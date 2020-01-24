from peewee import *
import datetime

import settings


db_handler = PostgresqlDatabase(
    settings.db_name, user=settings.user,
    host=settings.host, password=settings.password
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
