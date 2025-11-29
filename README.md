# Clean-Architecture-Practice
I'm building a blueprint for a **Library Management System** to practice industry-standard code writing following Clean Architecture principles (inspired by Claudio Shigueo Watanabe's example).

## Entity Mapping:
<p> This image shows the basic entities that are to be calibrated in the first inner layer i.e <b> Entities </b> layer. So the required entities are: </p>

* **Core Entities:**
    * **Book**
    * **User**
    * **Copy** (A specific physical instance of a Book)
    * **Loan** (The record of a Copy being checked out to a User)

<p> The higlighted properties of the entities are <b> Value Object </b>. </p>

### Value Object (VO) Concept

The highlighted properties of these entities are defined as **Value Objects**.

By definition, Value Objects are **immutable** and are compared based on their **value**, not their identity (ID).

> **Analogy:** Consider **Money** as a Value Object. Two separate $10 bills are considered equal if they are both $10 (same currency, same amount). While the currency type (Dollar, Rupee) is also a constraint of the VO, the comparison focuses on the *value*. For example, a `$10` object is compared to a `$5` object by their inherent value (10 is not equal to 5), regardless of which object instance is being held.

<img src="./images/image.png" alt="Clean Architecture Practice">