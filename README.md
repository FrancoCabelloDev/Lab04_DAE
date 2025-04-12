# 📚 Lab04: Django Model Relationships

A Django-based Library Management System demonstrating **One-to-One**, **One-to-Many**, **Many-to-Many**, and **Many-to-Many with intermediate table** model relationships.

## 🎯 Objective

Build a practical system that mirrors real-world data relationships using Django ORM. Focus on model organization, data integrity, and interface clarity.

---

## 🛠️ Features

- 👨‍🎨 Author profiles
- 📚 Book management
- 🏷️ Category classification
- 🏢 Publishers with country & publication date
- 🔗 Admin panel with full CRUD support
- 📊 Stats dashboard on homepage
- 🧪 Sample data population script

---

## ⚙️ Installation & Setup

> 🧪 Developed and tested on **Windows** using `python` and `pip`.

1. Clone the repository:

```bash
git clone https://github.com/your-username/library_project.git

## 🌐 Available URLs

| View               | Description                              | URL                                                 |
|--------------------|------------------------------------------|------------------------------------------------------|
| 🏠 Home            | Homepage with stats & highlights         | http://127.0.0.1:8000/                               |
| 📚 Book List       | Displays all books                       | http://127.0.0.1:8000/books/                         |
| 📖 Book Detail     | Individual book details                  | http://127.0.0.1:8000/books/<id>/                    |
| 👨‍🎨 Author List    | Displays all authors                     | http://127.0.0.1:8000/authors/                       |
| 👤 Author Detail   | Shows author and their books             | http://127.0.0.1:8000/authors/<id>/                  |
| 🏷️ Category List   | List of all book categories              | http://127.0.0.1:8000/categories/                    |
| 🏷️ Category Detail | Books by category                        | http://127.0.0.1:8000/categories/<slug>/             |
| 👑 Admin Panel     | Manage data through Django Admin         | http://127.0.0.1:8000/admin/                         |


