# 🚀 FastAPI REST API with Azure PostgreSQL

FastAPI-based REST API integrated with Azure PostgreSQL and automated CI/CD pipeline using GitHub Actions, Docker, Azure Container Registry, and Azure Web App for seamless containerized deployment.<br>This project demonstrates a full production-grade REST API built with FastAPI and PostgreSQL (Azure Database for PostgreSQL) as the backend. The application is containerized using Docker and fully automated with a CI/CD pipeline powered by GitHub Actions. The pipeline builds and pushes Docker images to Azure Container Registry (ACR) and automatically deploys the containerized API to Azure Web App for Containers. This setup ensures consistent builds, automated deployments, and scalable cloud infrastructure—ideal for modern backend service delivery

---

## 🧱 Tech Stack

- **Framework:** FastAPI  
- **Database:** Azure PostgreSQL  
- **ORM:** SQLAlchemy (adjust if you use another)  
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
```bash

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on Mac/Linux
```bash

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```bash

### 4️⃣ Add Environment Variables
Create a .env file:
DATABASE_URL=postgresql://<username>:<password>@<azure-host>:5432/<dbname>

### 5️⃣ Run the Server
```bash
uvicorn app.main:app --reload
```bash
