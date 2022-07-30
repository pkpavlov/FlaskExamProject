from enum import Enum


class UserRole(Enum):
    employee = "Employee"
    store_user = "Store User"
    admin = "Admin"
    accountant = "Accountant"
    warehouseman = "Warehouseman"


class TaskState(Enum):
    in_progress = "In Progress"
    done = "Done"
    cancelled = "Cancelled"
    on_hold = "On Hold"


class PurchaseState(Enum):

    processing = "Processing"
    pending_payment = "Pending payment"
    sent = "Sent"
