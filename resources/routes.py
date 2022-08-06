from resources.auth import (
    RegisterEmployeeResource,
    RegisterStoreUserResource,
    TasksResource,
    ItemsResource,
    LoginEmployeeResource,
    LoginStoreUserResource, TaskStatusEditResource, TaskSDeleteResource,
)

routes = (
    (RegisterEmployeeResource, "/register-employees/"),
    (RegisterStoreUserResource, "/register/"),
    (TasksResource, "/tasks/"),
    (ItemsResource, "/items/"),
    (LoginEmployeeResource, "/loginEmployee/"),
    (LoginStoreUserResource, "/login/"),
    (TaskStatusEditResource, "/task/<int:id>/"),
    (TaskSDeleteResource, "/task/<int:id>/")
)
