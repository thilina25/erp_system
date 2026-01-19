# Smart Inventory & Order Management System (ERP-Style Backend)

## 📌 Project Overview

This project is a **backend-focused ERP-style system** designed to simulate real-world business workflows used in enterprise applications. It is built using **Django** and **Django REST Framework**, following clean architecture principles, secure authentication, and proper business logic separation.

The system manages **inventory, suppliers, orders, invoices, and analytics**, making it suitable for medium-scale business operations. This project demonstrates backend engineering skills required for enterprise software development.

---

## 🎯 Key Objectives

* Build a scalable and secure RESTful backend
* Implement real-world business rules and workflows
* Apply role-based access control
* Automate stock management
* Generate management-level analytics
* Follow industry-standard API design

---

## 🛠️ Tech Stack

* **Backend:** Python, Django, Django REST Framework
* **Authentication:** JWT (JSON Web Tokens)
* **Database:** MySQL
* **API Style:** RESTful APIs
* **Security:** Token-based authentication, role permissions
* **Architecture:** Modular, service-oriented design

---

## 📦 Core Modules

### 1. User & Role Management

* Custom user model
* Roles: Admin, Manager, Staff
* JWT-based authentication
* Permission-based access control

---

### 2. Product & Inventory Management

* CRUD operations for products
* Category and supplier management
* Real-time stock tracking
* Reorder level monitoring
* Low-stock alerts

---

### 3. Order Management

* Order creation with multiple items
* Automatic stock deduction
* Order status workflow:

  * Pending
  * Approved
  * Shipped
  * Completed
  * Cancelled

---

### 4. Invoice System

* Auto invoice creation on order placement
* One-to-one mapping with orders
* Future-ready for PDF generation

---

### 5. Business Logic Automation

* Prevents orders with insufficient stock
* Automatically calculates total order value
* Uses database transactions for data consistency
* Stock safety validation

---

### 6. Dashboard & Analytics APIs

* Total orders count
* Total revenue
* Best-selling products
* Low-stock summary
* Orders per day
* Monthly revenue

---

## 🔐 Authentication & Security

* JWT-based login system
* Access token + refresh token mechanism
* Secured endpoints
* Role-based authorization
* Protected API routes

---

## 📂 Project Structure

```
erp_system/
│
├── users/
│   ├── models.py
│   ├── permissions.py
│   ├── admin.py
│
├── inventory/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── orders/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── signals.py
│   ├── urls.py
│
├── erp_system/
│   ├── settings.py
│   ├── urls.py
│
└── manage.py
```

---

## 🔁 API Testing

All APIs were tested using tools like:

* Postman
* Thunder Client

Test cases include:

* JWT authentication
* Role-based access
* Stock validation
* Order creation logic
* Dashboard analytics

---

This project follows real enterprise design patterns:

✔ Separation of concerns
✔ Business rule enforcement
✔ Secure authentication
✔ Role-based access
✔ Data integrity via transactions
✔ Scalable API design
✔ Modular architecture

---

## 👨‍💻 Author

**Thilina Kumarasiri**
Backend Developer | Django | REST APIs

---
