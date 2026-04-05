```mermaid
classDiagram
    class Patient {
        +String patientId
        +String name
        +submitProblem(description: String)
        +payBill(amount: Float)
    }

    class Organizer {
        +String organizerId
        +maintainDatabase()
        +forwardPrescription()
        +payDoctor()
    }

    class Doctor {
        +String doctorId
        +String specialty
        +reviewProblem(problemId: String)
        +providePrescription()
    }

    class HealthProblem {
        +String problemId
        +String description
        +String status
    }

    class Prescription {
        +String prescriptionId
        +String medication
    }

    class Payment {
        <<abstract>>
        +float amount
        +process()
    }

    class Check { +String checkNumber }
    class Cash { +float amountReceived }
    class CreditCard { +String cardNumber }

    %% Relations entre les classes
    Patient "1" -- "*" HealthProblem : "submits"
    HealthProblem "*" -- "1" Organizer : "reviewed by"
    Organizer "1" -- "*" Doctor : "consults"
    Doctor "1" -- "*" Prescription : "writes"
    Prescription "*" -- "1" Organizer : "returned to"
    Organizer "1" -- "1" Patient : "forwards prescription"
    
    Patient "1" -- "*" Payment : "makes"
    Payment <|-- Check : "is a type of"
    Payment <|-- Cash : "is a type of"
    Payment <|-- CreditCard : "is a type of"roblem : manages
