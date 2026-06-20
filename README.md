# 🛒 Smart Shop Billing System

A Python-based console application that simulates a small retail shop billing system. The project provides separate dashboards for shop owners and customers, allowing product management, cart operations, bill generation, GST calculation, and UPI QR code payment integration.

---

## 📌 Features

### 👨‍💼 Owner Dashboard

* Secure owner login
* View product list
* Add new products
* Remove existing products
* Manage inventory using file handling

### 🛍️ Customer Dashboard

* View available products
* Add products to cart
* Remove products from cart
* View shopping cart
* Generate bill with GST calculation
* Pay using UPI QR Code

### 💳 Payment Integration

* Dynamic UPI QR code generation
* QR code generated based on the final bill amount
* Compatible with UPI payment applications

---

## 🛠️ Technologies Used

* Python
* File Handling
* Exception Handling
* Functions
* Loops and Conditional Statements
* QR Code Library (`qrcode`)

---

## 📂 Project Structure

```text
Smart-Shop-Billing-System/
│
├── main.py
├── prod_list.txt
├── cart.txt
├── README.md
└── requirements.txt
```

---

## 📋 Product File Format

### prod_list.txt

```text
Laptop|50000
Mouse|500
Keyboard|1200
```

---

## 📋 Cart File Format

### cart.txt

```text
Laptop|50000|1|50000
Mouse|500|2|1000
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Shop-Billing-System.git
cd Smart-Shop-Billing-System
```

### 2. Install Required Package

```bash
pip install qrcode
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 🧾 Billing Process

1. Customer selects products.
2. Products are added to the cart.
3. Total amount is calculated.
4. GST (18%) is added.
5. Final bill is generated.
6. UPI QR code is displayed for payment.

---

## 📊 Sample Output

```text
Smart Shop 🏪

Total Amount : ₹1000
GST (18%)    : ₹180
Final Amount : ₹1180
```

---

## 🚀 Future Improvements

* SQLite/MySQL Database Integration
* Graphical User Interface (Tkinter/PyQt)
* Product Search Feature
* Inventory Tracking
* Bill Number Generation
* Invoice PDF Generation
* Sales Reports and Analytics
* Customer Management System
* Barcode Scanner Support

---

## 🎯 Learning Outcomes

This project helped in understanding:

* Python Programming Fundamentals
* File Handling
* Exception Handling
* Modular Programming
* Data Management
* QR Code Generation
* Real-World Billing System Design

---

## 👨‍💻 Author

**Ashutosh Pathak**

B.Tech Computer Science & Engineering
Aspiring Data Scientist & Software Developer

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
