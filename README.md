# Marine Smart Automation System

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Marine%20Engineering-blue?style=for-the-badge" alt="Marine Engineering">
  <img src="https://img.shields.io/badge/AI-Deep%20Learning-orange?style=for-the-badge" alt="Deep Learning">
  <img src="https://img.shields.io/badge/Android-Kotlin-green?style=for-the-badge&logo=android" alt="Android">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge" alt="FastAPI">
  <img src="https://img.shields.io/badge/Database-SQL%20Server-red?style=for-the-badge" alt="SQL Server">
  <img src="https://img.shields.io/badge/ML-Python-yellow?style=for-the-badge&logo=python" alt="Python">
</p>

<p align="center">
  <b>AI-Powered Marine Engineering and Vessel Operations Platform</b>
</p>

<p align="center">
  Leveraging deep learning, data-driven analytics, and mobile technologies
  to improve marine engineering operations and vessel monitoring.
</p>

---

## Overview

The **Marine Smart Automation System** is a multidisciplinary software platform designed to address challenges in marine engineering and improve vessel operations through data-driven intelligence.

The system combines:

- Machine Learning / Deep Learning
- Marine operational datasets
- REST APIs
- Database management
- Android mobile application
- RAG-based AI assistance
- Web-based monitoring/dashboard capabilities
- Edge deployment concepts

The overall repository is organized as a modular system where different components can be developed and maintained independently.

---

## Problem Statement

Marine vessels generate and depend on large amounts of operational data.

Traditionally, vessel monitoring and engineering analysis can involve:

- Manual monitoring
- Large volumes of sensor/operational data
- Delayed identification of abnormal conditions
- Difficult access to historical information
- Dependency on experienced personnel for analysis
- Limited accessibility of operational information

The goal of this project is to create an integrated platform that can use machine learning and intelligent software components to assist with vessel operations and marine engineering analysis.

---

## Proposed Solution

The system combines multiple software components into a unified architecture.

```text
                    Marine Vessel Data
                           │
                           ▼
                  ┌──────────────────┐
                  │   Data / Dataset │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │ Machine Learning │
                  │     Models       │
                  └────────┬─────────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │   Backend API    │
                  │    FastAPI       │
                  └────────┬─────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        Android App    Web Dashboard   AI Agent
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                 Marine Operations
                 & Decision Support
```

---

## Major Features

### Android Mobile Application

The project contains a dedicated native Android application for interacting with the marine monitoring system.

The application is located under:

```text
Mobile-App (Android app)/
└── Marine/
```

The Android module provides a mobile interface through which marine/vessel-related information can be presented to users.

### Machine Learning

The repository contains a dedicated machine-learning module:

```text
ml_model/
├── data/
├── evaluation/
├── models/
├── src/
├── API_GUIDE.md
├── compress_model.py
├── main.py
└── new_maritime_dataset.csv
```

The ML module contains:

- Dataset resources
- Model resources
- Source code
- Evaluation components
- Model compression utilities
- API documentation
- Maritime dataset

### AI Agent

The project also contains an AI-agent component based around:

- RAG
- LangChain
- Marine-domain information retrieval
- Intelligent question answering

Module:

```text
AI-Agent (RAG + Langchain system) [Akhand]/
└── marine_ai_intelligence_module/
```

The purpose of this component is to provide an intelligent interface for interacting with marine-domain information.

### Backend API

The repository contains a backend integration module based on FastAPI.

The backend provides an API layer between the application clients, machine-learning components, and database.

The documented setup uses:

- FastAPI
- Uvicorn
- SQL Server
- Python

The backend can be started using:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The FastAPI interactive documentation is available at:

```text
http://localhost:8000/docs
```

### Database

The backend is configured to work with a SQL Server database.

Example configuration:

```env
DB_SERVER=YOUR_SERVER
DB_NAME=MarineAI
DB_DRIVER=SQL Server
```

The database layer is responsible for persistent storage and retrieval of marine-related application data.

---

## System Architecture

The overall architecture can be represented as:

```text
                         ┌───────────────────────┐
                         │   Marine Data /       │
                         │   Operational Data    │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │    ML / DL Models     │
                         │       Python          │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │      FastAPI          │
                         │     Backend API       │
                         └───────────┬───────────┘
                                     │
                  ┌──────────────────┼──────────────────┐
                  │                  │                  │
                  ▼                  ▼                  ▼
          ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
          │   Android    │   │ Web Dashboard│   │  AI / RAG    │
          │     App      │   │   Frontend   │   │    Agent     │
          └──────────────┘   └──────────────┘   └──────────────┘
                  │                  │                  │
                  └──────────────────┼──────────────────┘
                                     │
                                     ▼
                           ┌──────────────────┐
                           │    SQL Server    │
                           │    Database      │
                           └──────────────────┘
```

---

## Android Application

### Technology Stack

The mobile application is developed as a native Android application.

### Core Technologies

| **Technology** | **Purpose** |
|---|---|
| Kotlin | Android application development |
| Android SDK | Native Android platform |
| XML | UI layouts |
| Gradle | Build and dependency management |
| Android Studio | Development environment |

### Android Module Structure

```text
Mobile-App (Android app)/
│
└── Marine/
    │
    ├── app/
    │
    ├── gradle/
    │
    ├── .gitignore
    ├── build.gradle.kts
    ├── gradle.properties
    ├── gradlew
    ├── gradlew.bat
    └── settings.gradle.kts
```

---

## Android Application Architecture

The Android application acts as a client of the backend system.

The basic communication flow is:

```text
User
 │
 ▼
Android UI
 │
 ▼
Application Logic
 │
 ▼
HTTP Request
 │
 ▼
FastAPI Backend
 │
 ▼
Database / ML Services
 │
 ▼
JSON Response
 │
 ▼
Android Application
 │
 ▼
UI Update
```

The Android client does not need direct access to the database.

Instead, the backend exposes controlled APIs.

This provides a cleaner separation:

```text
Android
   │
   │ REST API
   ▼
Backend
   │
   ├── Database
   │
   └── ML / AI Services
```

---

## Database Management

Database management was one of the important parts of the project.

The database layer is responsible for:

- Persistent storage
- Structured marine-related data
- Querying operational information
- Supporting backend API operations
- Maintaining relationships between stored entities
- Providing data to application-level services

The backend configuration uses:

```text
Database Server
      │
      ▼
SQL Server
      │
      ▼
MarineAI Database
```

---

## Database Request Flow

A typical database request follows:

```text
Android Application
        │
        ▼
     REST API
        │
        ▼
     FastAPI
        │
        ▼
 Database Query
        │
        ▼
    SQL Server
        │
        ▼
 Query Result
        │
        ▼
   FastAPI Response
        │
        ▼
    JSON Response
        │
        ▼
 Android Application
```

This architecture avoids exposing database credentials or direct database connectivity to the Android client.

---

## Machine Learning Module

The repository contains a dedicated:

```text
ml_model/
```

directory.

Its structure includes:

```text
ml_model/
│
├── data/
│
├── evaluation/
│
├── models/
│
├── src/
│
├── API_GUIDE.md
│
├── compress_model.py
│
├── main.py
│
└── new_maritime_dataset.csv
```

### Responsibilities

The ML module provides a dedicated environment for:

- Dataset processing
- Model development
- Model evaluation
- Model storage
- Model execution
- Model compression
- API integration

---

## Dataset

The repository includes a maritime dataset:

```text
new_maritime_dataset.csv
```

The dataset is used as part of the machine-learning workflow for the marine intelligence component.

The exact preprocessing and modeling pipeline can evolve independently from the Android application.

---

## AI / RAG Module

The project contains:

```text
AI-Agent (RAG + Langchain system) [Akhand]/
```

with

```text
marine_ai_intelligence_module/
```

The AI component is intended to provide marine-domain intelligence using Retrieval-Augmented Generation concepts.

### High-Level Flow

```text
User Question
      │
      ▼
AI Agent
      │
      ▼
Retrieval
      │
      ▼
Marine Knowledge / Documents
      │
      ▼
Context
      │
      ▼
Language Model
      │
      ▼
Generated Response
```

---

## Backend API

The backend module acts as the integration layer.

### Technology

- Python
- FastAPI
- Uvicorn
- SQL Server
- REST APIs

### API Responsibilities

- Accept client requests
- Validate request data
- Communicate with database
- Interface with ML services
- Return structured JSON responses
- Provide API endpoints to application clients

---

## Backend Setup

### 1. Clone Repository

```bash
git clone https://github.com/aishwaryguptadz/MajorProject.git
```

Move into the backend directory:

```bash
cd MajorProject/Backend-API
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Database

Create a `.env` file.

Example:

```env
DB_SERVER=YOUR_SQL_SERVER
DB_NAME=MarineAI
DB_DRIVER=SQL Server
```

Replace the server configuration with the SQL Server instance being used in your environment.

### 4. Start the API

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### 5. Open API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://localhost:8000/docs
```

---

## Android Setup

### Requirements

Install:

- Android Studio
- Android SDK
- JDK compatible with the project
- Android emulator or physical Android device

### Clone the Repository

```bash
git clone https://github.com/aishwaryguptadz/MajorProject.git
```

Navigate to:

```text
MajorProject/
└── Mobile-App (Android app)/
    └── Marine/
```

Open the `Marine` project in Android Studio.

### Build the Application

Allow Android Studio to:

- Index the project.
- Download Gradle dependencies.
- Sync the project.
- Build the application.

Then connect an Android device or start an emulator.

Run:

```text
Run → Run 'app'
```

---

## Component Communication

The different modules can be viewed as independent services/components:

```text
                         ┌──────────────┐
                         │  ML Models   │
                         └──────┬───────┘
                                │
                                ▼
┌──────────────┐       ┌────────────────┐
│ Android App  │──────►│  FastAPI API   │
└──────────────┘       └───────┬────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        ┌──────────┐    ┌─────────────┐   ┌──────────┐
        │ SQL      │    │ ML Services │   │ AI/RAG   │
        │ Server   │    │             │   │ Agent    │
        └──────────┘    └─────────────┘   └──────────┘
```

---

## My Contribution

### Android Application & Database Management

My primary contribution to this project was focused on the Android application and database/DBMS-related work.

#### Android Development

I worked on:

- Native Android application development.
- Android UI implementation.
- Application screens and navigation.
- Connecting the Android application with backend services.
- Consuming API responses.
- Displaying backend data on the mobile application.
- Handling application-side data flow.
- Testing Android functionality.
- Testing Android functionality.

#### Database / DBMS

I also worked on the database side of the project, including:

- Understanding the database schema.
- Structuring application-related data.
- Writing SQL queries.
- Retrieving data required by application features.
- Working with relational database concepts.
- Connecting backend functionality with stored data.
- Maintaining data consistency.
- Understanding relationships between marine-domain entities.

#### Integration

A major part of the contribution was understanding the communication between:

```text
Android Application
        │
        ▼
      API
        │
        ▼
    Backend
        │
        ▼
   Database
```

This allowed the Android application to consume data without directly accessing the database.

---

## Team Contributions

The project is organized into multiple modules corresponding to different areas of development.

| **Module** | **Responsibility** |
|---|---|
| Mobile-App | Android application |
| Android application | Backend-API |
| Dashboard-Web | Dashboard-Web |
| AI-Agent | RAG + LangChain marine intelligence |
| ml_model | Machine-learning pipeline |
| Data | Dataset/data resources |
| Edge-Module | Edge deployment / lightweight model |
| Docs | Project documentation |
| Scripts | Utility scripts |

The repository structure reflects a collaborative development approach, with different components maintained as separate modules.

---

## Technologies Used

### Mobile

- Kotlin
- Android
- Android Studio
- XML
- Gradle

### Backend

- Python
- FastAPI
- Uvicorn
- REST API

### Database

- Microsoft SQL Server
- SQL
- DBMS concepts

### Machine Learning

- Python
- Deep Learning
- Machine Learning
- Maritime datasets
- Model evaluation
- Model compression

### AI

- RAG
- LangChain
- AI Agent
- Information Retrieval

### Development Tools

- Git
- GitHub
- Android Studio
- VS Code
- SQL Server tools

---

## Repository Structure

```text
MajorProject/
│
├── AI-Agent (RAG + Langchain system) [Akhand]/
│   └── marine_ai_intelligence_module/
│
├── Backend-API (Fast API or Flask) [Shared (integration team)]/
│
├── Dashboard-Web (React frontend) [Anush]/
│
├── Data (Datasets or links)/
│
├── Docs (for documentation)/
│
├── Edge-Module (Edge deployment (Lite model))/
│
├── Mobile-App (Android app)/
│   └── Marine/
│       ├── app/
│       ├── gradle/
│       ├── build.gradle.kts
│       ├── gradle.properties
│       ├── gradlew
│       ├── gradlew.bat
│       └── settings.gradle.kts
│
├── Scripts (Utility scripts)/
│
├── ml_model/
│   ├── data/
│   ├── evaluation/
│   ├── models/
│   ├── src/
│   ├── API_GUIDE.md
│   ├── compress_model.py
│   ├── main.py
│   └── new_maritime_dataset.csv
│
├── .gitignore
└── README.md
```

---

## Security Considerations

Database credentials and other sensitive configuration values should not be committed to source control.

Use environment variables:

```env
DB_SERVER=YOUR_SERVER
DB_NAME=MarineAI
DB_DRIVER=SQL Server
```

The Android application should communicate with the backend through authenticated and secured APIs rather than connecting directly to the database.

For production deployment, additional security measures should include:

- HTTPS
- Authentication
- Authorization
- Secure API tokens
- Input validation
- SQL injection prevention
- Secure credential management
- Proper server configuration
- Database access control

---

## Testing

The project can be tested at multiple levels.

### Android Testing

Test:

- Application startup
- Screen navigation
- API communication
- Data rendering
- UI interactions
- Error states

### Backend Testing

Test:

- API endpoints
- Request validation
- Database connectivity
- Response formats
- Error handling

### Database Testing

Test:

- SQL queries
- Data insertion
- Data retrieval
- Data relationships
- Constraints
- Data consistency

### ML Testing

Test:

- Dataset processing
- Model performance
- Evaluation metrics
- Model inference
- Model compression

---

## Future Improvements

Potential future improvements include:

- [ ] Real-time vessel telemetry
- [ ] Live sensor data integration
- [ ] Push notifications for abnormal conditions
- [ ] Push notifications for abnormal conditions
- [ ] Improved ML model accuracy
- [ ] Real-time anomaly detection
- [ ] Offline Android support
- [ ] Local database caching
- [ ] Improved authentication
- [ ] Role-based access control
- [ ] Advanced dashboard analytics
- [ ] Model optimization for edge devices
- [ ] Automated CI/CD
- [ ] Comprehensive unit testing
- [ ] Automated API testing
- [ ] Production deployment

---

## Learning Outcomes

This project provided practical experience in:

- Native Android development
- Kotlin programming
- Android UI development
- REST API integration
- Client-server architecture
- Database management
- SQL
- Relational database design
- Backend integration
- Machine-learning systems
- AI-assisted applications
- RAG architecture
- LangChain
- Git and GitHub
- Team-based software development
- Modular project architecture

---

## License

No explicit open-source license is currently specified for this repository.

---

<p align="center"> <b>Marine Smart Automation</b> </p> <p align="center"> AI • Android • Backend • Database • Machine Learning • RAG </p>
