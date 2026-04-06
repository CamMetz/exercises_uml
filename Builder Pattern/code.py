from dataclasses import dataclass

@dataclass
class Employee:
    first_name: str = None
    last_name: str = None
    email: str = None
    department: str = None
    position: str = None
    salary: float = 0.0
    start_date: str = None
    manager_id: int = None
    phone: str = None
    address: str = None
    emergency_contact: str = None
    has_parking: bool = False
    has_laptop: bool = False
    has_vpn_access: bool = False
    has_admin_rights: bool = False
    office_location: str = None
    contract_type: str = "permanent"

class EmployeeBuilder:

    def __init__(self):
        self.employee = Employee()

    def with_name(self, first_name: str, last_name: str):
        self.employee.first_name = first_name
        self.employee.last_name = last_name
        return self

    def with_email(self, email: str):
        self.employee.email = email
        return self

    def with_job(self, department: str, position: str, salary: float):
        self.employee.department = department
        self.employee.position = position
        self.employee.salary = salary
        return self

    def with_contact(self, phone: str = None, address: str = None):
        self.employee.phone = phone
        self.employee.address = address
        return self

    def with_equipment(self, laptop=False, parking=False):
        self.employee.has_laptop = laptop
        self.employee.has_parking = parking
        return self

    def with_access(self, vpn=False, admin=False):
        self.employee.has_vpn_access = vpn
        self.employee.has_admin_rights = admin
        return self

    def with_office(self, location: str):
        self.employee.office_location = location
        return self

    def with_contract(self, contract_type: str):
        self.employee.contract_type = contract_type
        return self

    def build(self) -> Employee:
        # Validation centralisée (important 🔥)
        if not self.employee.first_name or not self.employee.last_name:
            raise ValueError("Name is required")

        if not self.employee.email or "@" not in self.employee.email:
            raise ValueError("Valid email is required")

        if self.employee.salary < 0:
            raise ValueError("Salary cannot be negative")

        return self.employee

class DeveloperBuilder(EmployeeBuilder):

    def __init__(self, first_name: str, last_name: str, email: str):
        super().__init__()

        self.with_name(first_name, last_name)
        self.with_email(email)

        # preset automatique 🔥
        self.with_job("Engineering", "Developer", 60000)
        self.with_equipment(laptop=True)
        self.with_access(vpn=True)

    def build(self) -> Employee:
        # règle métier automatique 🔥
        self.employee.has_admin_rights = True
        return super().build()

employee = (
    EmployeeBuilder()
    .with_name("John", "Doe")
    .with_email("john.doe@company.com")
    .with_job("Engineering", "Senior Developer", 75000)
    .with_equipment(laptop=True, parking=False)
    .with_access(vpn=True, admin=True)
    .build()
)

print(employee)

dev = DeveloperBuilder(
    "John",
    "Doe",
    "john.doe@company.com"
).build()

print(dev)
