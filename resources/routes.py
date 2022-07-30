from resources.auth import RegisterEmployeeResource, RegisterStoreUserResource, RegisterTaskResource, \
    RegisterItemResource, LoginEmployeeResource, LoginStoreUserResource

routes = (
    (RegisterEmployeeResource, "/register-employees/"),
    (RegisterStoreUserResource, "/register/"),
    (RegisterTaskResource, "/register-task/"),
    (RegisterItemResource, "/register-item/"),
    (LoginEmployeeResource, "/loginEmployee/"),
    (LoginStoreUserResource, "/login/")
)
