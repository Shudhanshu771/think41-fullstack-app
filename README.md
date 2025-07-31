
# 🛍️ Think41 E-Commerce Product Management System

This is a full-stack project developed as part of the Think41 Internship + Full-time Full Stack Developer program. The application consists of a **Flask-based backend** with **SQLite** for database management and a **React.js frontend** for displaying and interacting with product data.

---

## 🚀 Project Milestones Overview

### ✅ Milestone 1: Setup Project and Load Products into Database

**Goal**: Load `products.csv` into a SQLite database.

- 📁 Dataset: [`products.csv`](https://github.com/recruit41/ecommerce-dataset)
- 📂 Location: All CSV files placed inside `think41backend/data/`
- 🗃️ Database: `products.db` created using SQLite
- 📄 Script: `load_products.py` reads and inserts all 29,120 records into the database.

---

### ✅ Milestone 2: Verify Data Load and Basic API Setup

**Goal**: Verify products from database and expose basic REST API endpoints.

- ✅ Script: `verify_products.py` used to print and verify products from the database
- ⚙️ API Framework: `Flask` with `flask-cors` for cross-origin support
- 🔌 API Endpoints:

| Method | URL | Description |
|--------|-----|-------------|
| `GET`  | `/api/products` | Fetches a list of 100 products |
| `GET`  | `/api/products/<product_id>` | Fetches product by ID |

- 🔐 Error Handling:
  - Returns `404` if product is not found
  - Uses proper HTTP status codes

---

### ✅ Milestone 3: Frontend UI for Products (React.js)

**Goal**: Build a basic frontend to consume the REST API and show product data.

- ⚛️ Framework: React.js (with functional components)
- 🔗 Integration: Uses `fetch()` to connect to Flask backend
- 🧱 Features Implemented:
  - Product List View (grid layout with 100 products)
  - Product Detail View on click
  - Navigation between list and detail view using React Router
  - Basic responsive styling using CSS
  - Error and loading state handling

- 📂 Frontend Directory Structure:
```
think41frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── ProductList.js
│   │   ├── ProductCard.js
│   │   ├── ProductDetail.js
│   ├── App.js
│   ├── index.js
├── package.json
```

---

### ✅ Milestone 4: Refactor Department Field

**Goal**: Normalize database by moving department into a separate table.

- 🧩 Changes Made:
  - Created `departments` table with `id` and `name`
  - Updated `products` table to have a `department_id` foreign key
  - Refactored `load_products.py` to insert into both tables
  - Updated `verify_products.py` to show joined results
  - API `/api/products` and `/api/products/<id>` now return department name via SQL join
- 📦 Example API Output:
```json
{
  "id": 1,
  "price": 27.04,
  "category": "Tops & Tees",
  "name": "Seven7 Women's Long Sleeve Stripe Belted Top",
  "brand": "Seven7",
  "retail_price": 49.0,
  "gender": "Women",
  "product_code": "C4CA4238...",
  "department": "Clothing"
}
```

---

## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|------------------|
| Backend API  | Python, Flask, SQLite |
| Frontend     | React.js, CSS     |
| DB Tools     | SQLite3           |
| Others       | flask-cors, fetch API, React Router |

---

## 📌 Run Locally

### 1. Backend (Flask)

```bash
cd think41backend
python load_products.py
python app.py
# Runs on http://localhost:5000
```

### 2. Frontend (React)

```bash
cd think41frontend
npm install
npm start
# Runs on http://localhost:3000
```

---

## 🔗 Sample API URLs

- GET All Products: `http://localhost:5000/api/products`
- GET Product by ID: `http://localhost:5000/api/products/2`

---

## ✅ Milestones Completed

- [x] Milestone 1: Load CSV into DB
- [x] Milestone 2: Create and verify API
- [x] Milestone 3: Build UI to consume API
- [x] Milestone 4: Normalize DB with departments

---

## 👨‍💻 Author

Shudhanshu Prasad   
Email: shudhanshup4321@gmail.com | GitHub: [(https://github.com/Shudhanshu771)]

---
