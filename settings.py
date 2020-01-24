import os


def get_value_from_env(key):
    try:
        value = os.environ[key]
    except KeyError:
        raise ValueError(f"{key} is not presented in environment variables")
    else:
        return value


user = get_value_from_env('POSTGRES_USER')
password = get_value_from_env('POSTGRES_PASSWORD')
db_name = get_value_from_env('POSTGRES_DB')
host = get_value_from_env('POSTGRES_HOST')
