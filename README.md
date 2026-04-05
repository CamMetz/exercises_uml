# exercises_uml

 ```mermaid
classDiagram
    class Patient {
        +String patientId
        +String name
        +String password
        +String email
        +submitProblem(description: String)
        +payBill(amount: Float)
    }

    class Organizer {
        +String organizerId
        +String name
        +String password
        +maintainDatabase()
        +issueCredentials(userType: String)
        +forwardPrescription()
    }

    class Doctor {
        +String doctorId
        +String name
        +String password
        +String specialty
        +reviewProblem(problemId: String)
        +providePrescription()
    }

    Patient "1" -- "1..*" Organizer : submit problem / pay
    Organizer "1" -- "1..*" Doctor : consults / forwards
    Doctor "1" -- "1" Organizer : sends prescription" Doctor : "manages >"
