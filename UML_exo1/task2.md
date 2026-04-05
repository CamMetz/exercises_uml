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
    }

    class Doctor {
        +String doctorId
        +reviewProblem(problemId: String)
        +providePrescription()
    }

    class HealthProblem {
        +String problemId
        +String description
        +Date datePosted
    }

    class Prescription {
        +String prescriptionId
        +String details
    }

    class Payment {
        <<abstract>>
        +float amount
        +Date date
        +validate()
    }

    class Check { +String checkNumber }
    class Cash { +float tenderedAmount }
    class CreditCard { +String cardNumber }

    %% Héritage pour les paiements
    Payment <|-- Check
    Payment <|-- Cash
    Payment <|-- CreditCard

```mermaid
sequenceDiagram
    autonumber
    actor P as Patient
    participant O as Organizer
    participant D as Doctor
    participant Pay as Payment (CreditCard)

    Note over P, D: Scénario : Soumission, Traitement et Paiement

    P->>O: submitProblem("Mal de gorge")
    O->>D: reviewProblem(problemId)
    D->>O: providePrescription("Antibiotiques")
    O->>P: forwardPrescription()
    
    P->>Pay: payBill(amount)
    Pay-->>P: confirmPayment()
    P->>O: sendPaymentProof()
    O->>D: forwardPaymentToDoctor()

    %% Relations
    Patient "1" *-- "*" HealthProblem : owns
    HealthProblem "1" -- "0..1" Prescription : generates
    Doctor "1" --> "*" Prescription : writes
    Patient "1" -- "*" Payment : makes
    Organizer "1" --> "*" HealthProblem : manages
