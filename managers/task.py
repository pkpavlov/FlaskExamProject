from models.tasks import TaskModel
from db import db


class TaskManager:

    @staticmethod
    def register(task):

        task = TaskModel(**task)
        db.session.add(task)
        db.session.commit()
        return task