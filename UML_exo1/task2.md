```mermaid
classDiagram
    class Patient {
        +String patientId
        +String name
        +submitProblem(description String)
        +payBill(amount Float)
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
        +reviewProblem(problemId String)
        +providePrescription()
    }

    class HealthProblem {
        +String problemId
        +String description
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

    Payment <|-- Check
    Payment <|-- Cash
    Payment <|-- CreditCard

    Patient -- HealthProblem : submits
    HealthProblem -- Organizer : reviews
    Organizer -- Doctor : consults
    Doctor -- Prescription : writes
    Prescription -- Organizer : returns
    Organizer -- Patient : forwards
    Patient -- Payment : pays

sequenceDiagram
    autonumber
    actor P as Patient
    participant O as Organizer
    participant D as Doctor
    participant Pay as Payment_System

    P->>O: submitProblem(description)
    Note right of O: Organizer logs the problem
    O->>D: reviewProblem(problemId)
    D->>O: providePrescription(medication)
    O->>P: forwardPrescription()
    
    P->>Pay: payBill(amount)
    Pay-->>P: confirmTransaction
    Note over O,D: Organizer forwards fee to Doctor
