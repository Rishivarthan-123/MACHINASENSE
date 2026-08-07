# MACHINASENSE System Architecture

# Overview

MACHINASENSE follows a modular, scalable architecture that separates the frontend, backend, AI services, and database into independent layers.

This architecture allows the platform to grow from a simple predictive maintenance application into a complete Manufacturing Intelligence Platform.

---

# High-Level Architecture

```
                 User

                  │

                  ▼

        React + TypeScript Frontend

                  │

          REST API (HTTPS)

                  │

                  ▼

          FastAPI Backend Server

        ┌─────────┼──────────┐
        │         │          │
        ▼         ▼          ▼

 Authentication  Machine   Sensor Data
    Service      Service     Service

                  │

                  ▼

            AI Prediction Service

        ┌─────────┼──────────┐
        │         │          │

        ▼         ▼          ▼

 Anomaly Detection
 Failure Prediction
 Health Score

                  │

                  ▼

            PostgreSQL Database

                  │

                  ▼

          Dashboard & Reports
```

---

# Components

## Frontend

Responsibilities:

* User Interface
* Authentication
* Dashboard
* Machine Management
* Reports
* Alerts

Technology:

* React
* TypeScript
* Tailwind CSS
* React Query

---

## Backend

Responsibilities:

* REST APIs
* Authentication
* Business Logic
* File Upload
* AI Integration
* Database Management

Technology:

* FastAPI
* SQLAlchemy
* Pydantic
* JWT Authentication

---

## AI Engine

Responsibilities:

* Data preprocessing
* Feature engineering
* Anomaly detection
* Machine health calculation
* Failure prediction

Technology:

* Scikit-learn
* XGBoost
* SHAP

---

## Database

Responsibilities:

* User data
* Machine information
* Sensor data
* Prediction history
* Alerts

Technology:

* PostgreSQL

---

# Data Flow

1. User logs into MACHINASENSE.
2. User registers a machine.
3. User uploads machine sensor data (CSV).
4. Backend validates the uploaded data.
5. AI engine processes the sensor data.
6. Predictions are generated.
7. Results are stored in PostgreSQL.
8. Dashboard displays machine health and predictions.

---

# Design Principles

* Modular Architecture
* Separation of Concerns
* Scalable Services
* API-First Design
* AI as an independent service
* Easy future integration with IoT devices

---

# Future Architecture

Future versions will include:

* MQTT Broker
* ESP32 Sensor Devices
* Real-Time Streaming
* Redis Cache
* Celery Background Workers
* MLflow Model Registry
* Docker Deployment
* Kubernetes
* Monitoring with Prometheus and Grafana

The current architecture is designed so these components can be added without major changes to the existing codebase.
