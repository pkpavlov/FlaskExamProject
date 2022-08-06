from models import UserRole, EmployeesModel, TaskState
from models.tasks import TaskModel
from db import db


class TaskManager:



    @staticmethod
    def register(task):

        task = TaskModel(**task)
        db.session.add(task)
        db.session.commit()
        return task

#get task for one employee or all task
    @staticmethod
    def get_task(user):
        if user.role == UserRole.employee:
            return TaskModel.query.filter_by(employee_id=user.id).all()
        return TaskModel.query.all()

#change task status

    @staticmethod
    def task_update(task_data):

        TaskModel.query.filter_by(id=task_data["id"]).update({"state": TaskState.done,
                                                              "used_parts": task_data["used_parts"],
                                                              "employee_comments":task_data["employee_comments"]})
        db.session.commit()

    @staticmethod
    def delete(task_id):
        task = TaskModel.query.filter_by(id=task_id["id"]).first()
        db.session.delete(task)
        db.session.commit()




