```plantuml
@startuml

class Patient {
  +id: int
  +name: string
  +submitProblem()
  +pay()
}

class Organizer {
  +id: int
  +name: string
  +consultDoctor()
  +sendPrescription()
  +manageSystem()
}

class Doctor {
  +id: int
  +name: string
  +providePrescription()
}

class HealthProblem {
  +description: string
  +date: Date
}

class Prescription {
  +details: string
  +date: Date
}

class Payment {
  +amount: float
  +pay()
}

class Check
class Cash
class CreditCard

' Relationships
Patient "1" --> "1..*" HealthProblem : submits
HealthProblem --> Prescription : results in
Doctor --> Prescription : creates
Organizer --> Doctor : consults
Organizer --> Patient : communicates

Patient --> Payment : makes
Organizer --> Payment : processes
Doctor --> Payment : receives

' Inheritance for payment types
Payment <|-- Check
Payment <|-- Cash
Payment <|-- CreditCard

@enduml


```md
```plantuml
@startuml

actor Patient
participant Organizer
participant Doctor
participant Payment

Patient -> Organizer : submitHealthProblem()
Organizer -> Doctor : consult(problem)
Doctor -> Organizer : prescription
Organizer -> Patient : sendPrescription()

Patient -> Payment : makePayment()
Payment -> Organizer : confirmPayment()
Organizer -> Doctor : transferPayment()

@enduml
