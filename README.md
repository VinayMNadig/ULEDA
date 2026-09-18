# 🚀 ULEDA — Universal LLM Enterprise Database Assistant 

<p align="center">
  <strong>AI-Powered Database Intelligence Platform using LLMs, RAG & AI Agents</strong>
</p>

<p align="center">
  <em>Ask questions. Understand databases. Generate SQL. Analyze data.</em>
</p> 

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge\&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge\&logo=react)
![SQL](https://img.shields.io/badge/SQL-Database-orange?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-AI-purple?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Architecture-red?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B35?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge\&logo=docker)

</p>

--- 

## 🧠 What is ULEDA?

**ULEDA (Universal LLM Enterprise Database Assistant)** is an AI-powered database intelligence platform designed to make databases easier to understand and interact with using natural language.

Traditional database interaction requires users to understand:

* Database schemas
* Tables and relationships
* SQL syntax
* Query construction
* Data analysis

ULEDA introduces an AI layer between the user and the database.

Instead of manually writing SQL, users can ask questions such as:

> **"Show me the top 10 customers by total spending."**

ULEDA can understand the question, retrieve relevant database schema information, generate an SQL query, validate the query, execute it against the database, and present the result in an understandable format.

---

# 🎯 Problem

Modern applications generate large amounts of structured data, but extracting useful information often requires technical database knowledge.

A typical workflow looks like:

```text
User
 ↓
Understand Database
 ↓
Find Relevant Tables
 ↓
Understand Relationships
 ↓
Write SQL
 ↓
Debug SQL
 ↓
Execute Query
 ↓
Analyze Results
```

ULEDA aims to simplify this process:

```text
User Question
      ↓
    ULEDA
      ↓
Schema Understanding
      ↓
RAG Retrieval
      ↓
AI SQL Agent
      ↓
SQL Validation
      ↓
Database Execution
      ↓
Results & Insights
      ↓
Charts / Reports
```

---

# ✨ Core Features

| Feature                     | Description                                            |
| --------------------------- | ------------------------------------------------------ |
| 🤖 AI Database Assistant    | Interact with databases using natural language         |
| 🧠 LLM Integration          | Use large language models for database reasoning       |
| 🔍 Schema Understanding     | Extract and understand database structure              |
| 📚 RAG                      | Retrieve relevant schema context before LLM generation |
| 🗃️ ChromaDB                | Store and retrieve schema embeddings                   |
| 🧩 AI SQL Agent             | Convert natural-language questions into SQL            |
| 🔐 Authentication           | Secure user authentication architecture                |
| 💬 Conversational Interface | Support natural-language database conversations        |
| 📊 Analytics                | Analyze structured database results                    |
| 📈 Visualization            | Present data through charts and visualizations         |
| 📄 Reports                  | Generate analytical reports                            |
| 🐳 Docker                   | Containerized deployment architecture                  |
| ☁️ Cloud Ready              | Architecture designed for cloud deployment             |
| 🗄️ Multi-Database          | Extensible architecture for multiple database systems  |

> **Development status:** ULEDA is actively under development. Features marked in the roadmap may not yet be fully implemented.

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │        USER          │
                         │  Natural Language    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   React Frontend     │
                         └──────────┬───────────┘
                                    │
                               REST API
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    FastAPI Backend   │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
              ┌──────────┐   ┌──────────┐   ┌────────────┐
              │ Database │   │   RAG    │   │ AI Agents  │
              │  Layer   │   │ Pipeline │   │            │
              └────┬─────┘   └────┬─────┘   └─────┬──────┘
                   │              │               │
                   │              ▼               │
                   │         ┌──────────┐         │
                   │         │ ChromaDB │         │
                   │         └────┬─────┘         │
                   │              │               │
                   └──────────────┼───────────────┘
                                  ▼
                         ┌──────────────────┐
                         │       LLM        │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Results/Insights │
                         └──────────────────┘
```

---

# 🔥 AI SQL Agent

One of the central components of ULEDA is the **AI SQL Agent**.

The goal is to transform natural-language questions into executable SQL while using the actual database schema as context.

### Example

**User:**

```text
Find the top 5 most expensive products.
```

### AI Pipeline

```text
Natural Language Question
          ↓
Intent Understanding
          ↓
Schema Retrieval
          ↓
Relevant Context
          ↓
SQL Generation
          ↓
SQL Validation
          ↓
Database Execution
          ↓
Result Analysis
```

Example SQL:

```sql
SELECT product_name, price
FROM products
ORDER BY price DESC
LIMIT 5;
```

The generated SQL depends on the schema and structure of the connected database.

---

# 📚 Retrieval-Augmented Generation

ULEDA uses **Retrieval-Augmented Generation (RAG)** to provide relevant database context to the LLM.

### RAG Pipeline

```text
Database
   ↓
Schema Extraction
   ↓
Schema Documentation
   ↓
Embedding Generation
   ↓
ChromaDB
   ↓
Semantic Search
   ↓
Relevant Schema Context
   ↓
LLM
   ↓
SQL / Explanation
```

Instead of blindly asking the LLM to generate SQL, ULEDA first retrieves relevant schema information.

This creates a more structured workflow for database-aware AI interactions.

---

# 🗃️ Database Schema Intelligence

ULEDA can inspect database structures and make schema information available to the AI system.

Example:

```text
Database
│
├── customers
│   ├── id
│   ├── name
│   ├── email
│   └── city
│
├── employees
│   ├── id
│   ├── name
│   └── department
│
├── products
│   ├── id
│   ├── name
│   └── price
│
└── suppliers
    ├── id
    ├── name
    └── contact
```

This schema can then become part of the AI context.

---

# 💬 Natural Language Queries

Users can interact with the database using questions such as:

```text
Show all customers from Bengaluru.
```

```text
How many products are available?
```

```text
Find the five most expensive products.
```

```text
Which employees work in the sales department?
```

```text
Show the number of customers in each city.
```

```text
Which products have the highest sales?
```

The system converts the user's intent into a database operation.

---

# 📊 AI Analytics

ULEDA is designed to provide more than raw SQL output.

The analytical pipeline can transform structured query results into useful information.

```text
SQL Query
   ↓
Database
   ↓
Structured Result
   ↓
Data Processing
   ↓
Analytics
   ↓
AI-Generated Insights
   ↓
Visualization
```

Potential analytical capabilities include:

* Aggregations
* Rankings
* Comparisons
* Trends
* Distributions
* KPIs
* Summary statistics
* AI-generated explanations

---

# 📈 Data Visualization

ULEDA is designed to transform database results into visual representations.

Potential visualizations include:

* 📊 Bar charts
* 📈 Line charts
* 🥧 Pie charts
* 📋 Data tables
* 🔢 KPI cards
* 📉 Trend analysis

Example workflow:

```text
User Question
     ↓
SQL Query
     ↓
Database Result
     ↓
Data Analysis
     ↓
Chart Generation
```

---

# 🧠 AI Agent Architecture

ULEDA is designed around an agent-based workflow.

```text
                    User
                     │
                     ▼
                 ┌───────┐
                 │Planner│
                 └───┬───┘
                     │
                     ▼
              ┌─────────────┐
              │Schema/RAG   │
              │  Retrieval  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ SQL Agent   │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  Validator  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │  Executor   │
              └──────┬──────┘
                     │
                     ▼
                  Results
```

This architecture can be expanded with additional agents for analytics, reporting, validation, and data reasoning.

---

# 🛠️ Technology Stack

## Frontend

* React.js
* JavaScript
* HTML5
* CSS3

## Backend

* Python
* FastAPI
* SQLAlchemy
* REST APIs

## AI

* Large Language Models
* Retrieval-Augmented Generation
* Embeddings
* Prompt Engineering
* AI Agents
* Natural Language → SQL

## Vector Database

* ChromaDB
* Vector Embeddings
* Semantic Search

## Database

* SQLite
* SQLAlchemy
* Extensible database architecture

## Development

* Git
* GitHub
* VS Code
* IntelliJ IDEA
* Postman
* Docker

---

# 📂 Project Structure

```text
ULEDA/
│
├── backend/
│   │
│   ├── app/
│   │   ├── agents/
│   │   ├── ai/
│   │   ├── api/
│   │   ├── assistant/
│   │   ├── auth/
│   │   ├── config/
│   │   ├── core/
│   │   ├── database/
│   │   ├── llm/
│   │   ├── models/
│   │   ├── rag/
│   │   ├── schema/
│   │   ├── security/
│   │   ├── services/
│   │   ├── sql/
│   │   ├── upload/
│   │   └── utils/
│   │
│   ├── .env.example
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .gitignore
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/VinayMNadig/ULEDA.git
```

```bash
cd ULEDA
```

---

# 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create your local environment file:

```text
backend/.env
```

Add your own API key:

```env
GROQ_API_KEY=your_actual_api_key
```

The repository contains:

```text
backend/.env.example
```

with only safe configuration placeholders.

### ⚠️ Security

Never commit:

```text
.env
```

or any API key, password, token, database credential, or other secret to GitHub.

---

# ▶️ Run the Backend

From the `backend` directory:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open a new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

---

# 🧪 API Development

ULEDA APIs can be tested using:

* FastAPI Swagger UI
* Postman
* Frontend requests

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🛡️ Security Architecture

Because ULEDA interacts with databases and external AI services, security is an important part of the system design.

Security considerations include:

* 🔐 Environment-based secret management
* 🚫 `.env` excluded from Git
* 🔑 Authentication
* 🛡️ Input validation
* 🧾 SQL validation
* 🔒 Controlled database execution
* 🚫 Protection against secret exposure
* 📝 Future audit logging
* 👤 Future role-based access control

Production deployment should additionally use appropriate database permissions, secret-management systems, rate limiting, monitoring, logging, and environment-specific security controls.

---

# 🐳 Docker & Deployment

ULEDA is being designed for containerized deployment.

Target architecture:

```text
                 Cloud / Server
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
      Frontend                  Backend
       React                    FastAPI
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
                     Database              ChromaDB
                         │                     │
                         └──────────┬──────────┘
                                    ▼
                                   LLM
```

Future deployment can include:

* Docker
* AWS
* CI/CD
* Cloud databases
* Managed vector databases
* Monitoring
* Logging

---

# 🚧 Development Roadmap

## Phase 1 — Foundation

* [x] FastAPI backend
* [x] Database connectivity
* [x] Database schema extraction
* [x] LLM integration foundation
* [x] RAG foundation
* [x] ChromaDB integration
* [x] Modular backend architecture

## Phase 2 — AI Database Assistant

* [ ] Advanced natural-language database queries
* [ ] AI SQL generation
* [ ] SQL validation
* [ ] Controlled SQL execution
* [ ] Conversational database interaction
* [ ] AI-generated explanations

## Phase 3 — Analytics

* [ ] Automated chart generation
* [ ] Advanced analytics
* [ ] AI-generated insights
* [ ] KPI generation
* [ ] Data exploration

## Phase 4 — Enterprise

* [ ] User authentication
* [ ] Multi-user support
* [ ] Multi-database support
* [ ] Chat history
* [ ] Report generation
* [ ] Role-based access control
* [ ] Audit logging

## Phase 5 — Production

* [ ] Docker deployment
* [ ] AWS deployment
* [ ] CI/CD pipeline
* [ ] Monitoring
* [ ] Performance optimization
* [ ] Production security hardening
* [ ] Scalable infrastructure

---

# 📸 Screenshots

Add application screenshots here as the UI is finalized.

Recommended screenshots:

```text
docs/
└── screenshots/
    ├── dashboard.png
    ├── ai-assistant.png
    ├── database-schema.png
    ├── generated-sql.png
    ├── query-results.png
    ├── analytics.png
    └── reports.png
```

Example:

```markdown
## 📸 Screenshots

### AI Database Assistant

![AI Database Assistant](docs/screenshots/ai-assistant.png)

### Database Analytics

![Analytics Dashboard](docs/screenshots/analytics.png)
```

---

# 🎓 Engineering Concepts

ULEDA demonstrates practical implementation of modern software and AI engineering concepts:

### Software Engineering

* Modular architecture
* REST API design
* Separation of concerns
* Backend service architecture
* Version control

### Database Engineering

* SQL
* Schema inspection
* Database connectivity
* Query execution
* Data processing

### AI Engineering

* LLM integration
* Prompt engineering
* RAG
* Embeddings
* Vector databases
* Semantic search
* AI agents
* Natural-language-to-SQL

### Deployment

* Environment configuration
* Docker
* Cloud architecture
* API deployment
* CI/CD concepts

---

# 🌍 Future Vision

The long-term goal of ULEDA is to evolve into an **AI-powered database intelligence layer** that allows users and organizations to interact with structured data through natural language.

```text
                         ┌───────────────┐
                         │     USERS     │
                         └───────┬───────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │         ULEDA          │
                    │ AI Database Intelligence│
                    └────────────┬───────────┘
                                 │
               ┌─────────────────┼─────────────────┐
               │                 │                 │
               ▼                 ▼                 ▼
          Databases             RAG           AI Agents
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 │
                                 ▼
                       Business Intelligence
```

---

# 🤝 Contributing

Contributions and suggestions are welcome.

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Make your changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Add your feature"
```

Push:

```bash
git push origin feature/your-feature
```

Then create a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Developer

## Vinay M Nadig

**Computer Science & Engineering Student**

### Areas of Interest

* Software Engineering
* Java
* Full-Stack Development
* Artificial Intelligence
* Large Language Models
* RAG Systems
* AI Agents
* Backend Engineering
* Database Systems
* Cloud Computing

---

# ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

---

<p align="center">

### 🚀 ULEDA

<strong>Making databases understandable through AI.</strong>

<br><br>

Python • FastAPI • React • SQL • LLMs • RAG • AI Agents • ChromaDB

</p>
