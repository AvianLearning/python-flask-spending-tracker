from db.run_sql import run_sql

from models.tag import Tag


def save(tag):
    sql = "INSERT INTO tags (category) VALUES (%s) 