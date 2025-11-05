# 🚀 FastAPI REST API with Azure PostgreSQL

A RESTful API built using **FastAPI** and connected to an **Azure PostgreSQL** database.  
Implements CRUD operations with proper environment configuration and modular code structure.

---

## 🧱 Tech Stack

- **Framework:** FastAPI  
- **Database:** Azure PostgreSQL  
- **ORM:** SQLAlchemy / psycopg2 (adjust if you use another)  
- **Language:** Python 3.x  
- **Hosting:** Azure App Service (optional)

---

## 📁 Project Structure

project_root/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── models.py # SQLAlchemy models
│ ├── database.py # Database connection
│ ├── routes/ # All route files
│ └── schemas.py # Pydantic models
│
├── requirements.txt
├── .env # Environment variables (not pushed)
└── README.md


---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables
Create a .env file:
DATABASE_URL=postgresql://<username>:<password>@<azure-host>:5432/<dbname>

5️⃣ Run the Server
uvicorn app.main:app --reload
