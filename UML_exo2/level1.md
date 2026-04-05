## Task 1.1 : Use Case Diagram

```mermaid
flowchart LR

Member -->|Place Order| UC1[Place Order]
Member -->|Make Payment| UC2[Make Payment]

OrderClerk[Order Processing Clerk] -->|Verify Membership| UC3[Verify Membership]
OrderClerk -->|Process Order| UC4[Process Order]
```

## Task 1.2 : Class Diagram

```mermaid
classDiagram

class Member {
  +id : int
  +name : string
  +status : string
  +placeOrder()
  +makePayment()
}

class Order {
  +orderId : int
  +date : string
  +amount : float
  +createOrder()
  +validateOrder()
}

class OrderProcessingClerk {
  +id : int
  +name : string
  +verifyMembership()
  +processOrder()
}

Member --> Order : places
OrderProcessingClerk --> Order : processes
OrderProcessingClerk --> Member : verifies
```

