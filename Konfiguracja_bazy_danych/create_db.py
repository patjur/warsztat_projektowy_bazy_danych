CREATE_DB = "CREATE DATABASE workshop;"

CREATE_USERS_TABLE = """CREATE TABLE users(
    id serial PRIMARY KEY, 
    username varchar(255) UNIQUE,
    hashed_password varchar(80))"""

CREATE_MESSAGES_TABLE = """CREATE TABLE messages(
    id SERIAL, 
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""