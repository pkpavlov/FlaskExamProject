from resources.auth import (
    RegisterEmployeeResource,
    RegisterStoreUserResource,
    TasksResource,
    ItemsResource,
    LoginEmployeeResource,
    LoginStoreUserResource,
    TaskStatusEditResource,
    TaskDeleteResource,
    DeleteItemsResource,
    BuyStoreItemResource,
    SalaryPaymentResource,
    SalaryUpdateResource,
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
    (SalaryPaymentResource, "/salary/<int:id>/payment/"),
    (SalaryUpdateResource, "/salary/<int:id>/update/"),
)
