# 🚀 WorkedIn - Employment Made Easy 🛠️

## 📌 About the Project
WorkedIn is a **job portal desktop application** developed as my **first-semester project** for the **Application of ICT course**. It consists of **over 1000 lines of well-structured Python code**, following **good programming practices**, including modular design, code reusability, and database integration.

This application bridges the gap between **employers** and **tradespersons/laborers**, enabling efficient job posting and job search based on city and job type. 🌍

## ✨ Features
### 🔐 **Authentication System**
- Secure **login and signup** for both employers and tradespersons.
- Password management (reset and recovery ). 🔑

### 🏢 **Employer Features**
- 📌 **Post Jobs** with job title, description, city, and type.
- 👀 **View Available Workers** filtered by city/type.
- 🗑️ **Delete Job Postings** when the position is filled.
- ✏️ **Manage Profile** (update business details, contact information, etc.).

### 👷 **Tradesperson Features**
- 🔍 **View Available Jobs** posted by employers.
- 🏙️ **Search Jobs** by city and job type.
- 👤 **Profile Management** (update skills, experience, and contact details).

## 🛠️ Tech Stack
### 🎨 **Frontend**
- CustomTkinter (GUI Framework)
- Tkinter Calendar

### ⚙️ **Backend**
- Firebase Admin SDK
- Firebase Authentication
- Firebase Firestore Database

### 💻 **Development Tools**
- Python 3.x 🐍
- VS Code 🖥️

## 📂 Project Structure
```
/CODE
  /lib
    - authentication_firebase.py  # Handles user authentication
    - backend_functions.py        # Core backend logic
    - urdu_interface.py           # User interface in Urdu
    - english_interface.py        # User interface in English
  - workedin.py                   # Main application file
```

## 🎯 Who Will Benefit from This Project?
### 👷‍♂️ **1. Tradespersons and Laborers:**
- Easily **find jobs** without relying on middlemen.
- Connect directly with potential employers.
- Increase their visibility by maintaining an online profile.

### 🏢 **2. Employers & Businesses:**
- Quickly **post job openings** and find skilled laborers.
- Save time by **searching for workers** based on location and skills.
- Manage job postings efficiently in one place.

### 🧑‍💻 **3. Students & Developers:**
- Learn how to integrate **Firebase Firestore** in a Python-based desktop application.
- Understand **good programming practices** with structured, modular code.
- Gain insights into **GUI development using CustomTkinter**.


## ⚡ Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/muneebahmed-nust/Workedin.git
   ```
2. Install required dependencies:
   ```bash
   pip install customtkinter firebase-admin pillow
   ```
3. Run the application:
   ```bash
   python workedin.py
   ```

## 📜 License
This project is open-source and available under the **MIT License**.

---
✨ **Developed by [Sheikh Muneeb Ahmed](https://github.com/muneebahmed-nust) and [Emaan Ahmed](https://github.com/emaan19)** | First Semester ICT Course Project | NUST 🏫

