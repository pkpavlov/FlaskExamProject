from resources.auth import (
    RegisterEmployeeResource,
    RegisterStoreUserResource,
    TasksResource,
    ItemsResource,
    LoginEmployeeResource,
    LoginStoreUserResource, TaskStatusEditResource, TaskDeleteResource, DeleteItemsResource, BuyStoreItemResource,
)

routes = (
    (RegisterEmployeeResource, "/register-employees/"),
    (RegisterStoreUserResource, "/register/"),
    (TasksResource, "/tasks/"),
    (ItemsResource, "/items/"),
    (LoginEmployeeResource, "/loginEmployee/"),
    (LoginStoreUserResource, "/login/"),
    (TaskStatusEditResource, "/task/<int:id>/"),
    (TaskDeleteResource, "/task/<int:id>/"),
    (DeleteItemsResource, "/item/<int:id>/"),
    (BuyStoreItemResource, "/items/buy/"),

)
