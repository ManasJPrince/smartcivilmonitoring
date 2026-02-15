<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Urban Sanitation Intelligence Platform 🎯

## Basic Details

### Team Name: Unified

### Team Members
- Member 1: Manas J Prince - Saintgits College Of Engineering
- Member 2: Sivani Nair - Saintgits College Of Engineering

### Hosted Project Link
[mention your project hosted link here]

### Project Description
The Urban Sanitation Intelligence Platform is a comprehensive smart city solution designed to modernize waste management. It integrates real-time incident reporting, sanitation worker task management, and data-driven analytics into a unified dashboard to ensure cleaner urban environments.

### The Problem statement
Rapid urbanization has led to inefficient waste collection, resulting in overflowing bins, delayed pickups, and environmental health hazards. Traditional methods lack real-time monitoring and accountability.

### The Solution
We provide a centralized platform that connects citizens, sanitation workers, and improved municipal administration. By leveraging IoT-enabled smart bins (simulated/planned) and a responsive web application, we enable real-time tracking of waste levels and efficient task allocation.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- **Languages used:** Python, JavaScript, HTML, CSS
- **Frameworks used:** FastAPI (Backend), React 19 + Vite (Frontend)
- **Libraries used:** 
  - Backend: SQLAlchemy, Pydantic, Python-multipart, Requests
  - Frontend: TailwindCSS v4, React Query, Recharts, Lucide-React, Axios
- **Tools used:** VS Code, Git, SQLite

**For Hardware:**
- **Main components:** [Arduino Uno / ESP32 - TBD by User]
- **Specifications:** [Sensors for waste level detection - TBD]
- **Tools required:** [Breadboard, Jumper wires, Soldering iron]

---

## Features

List the key features of your project:
- **Incident Reporting:** Real-time logging of sanitation issues with image evidence.
- **Task Management:** automated assignment and tracking of cleaning tasks for workers.
- **Analytics Dashboard:** Visual insights into waste monitoring, collection efficiency, and incident resolution.
- **Platform Configuration:** Flexible settings for system parameters and user management.

---

## Implementation

### For Software:

#### Installation

**Backend:**
```bash
cd urban-sanitation-platform/backend
# Create virtual environment
python -m venv venv
# Activate virtual environment (Windows)
.\venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
```

**Frontend:**
```bash
cd urban-sanitation-platform/frontend
# Install dependencies
npm install
```

#### Run

**Backend:**
```bash
cd urban-sanitation-platform/backend
# Run the FastAPI server
uvicorn app.main:app --reload
```
*Backend runs on http://127.0.0.1:8000*

**Frontend:**
```bash
cd urban-sanitation-platform/frontend
# Run the development server
npm run dev
```
*Frontend runs on http://localhost:5173*

### For Hardware:

#### Components Required
[List specific hardware components here, e.g., Ultrasonic Sensor HC-SR04, Servo Motors]

#### Circuit Setup
[Explain connections, e.g., Connect Trig pin to Arduino D9, Echo to D10]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Dashboard](docs/dashboard.png)
*Real-time analytics showing waste levels and incident reports*

![Task Board](docs/tasks.png)
*Task management interface for assigning jobs to workers*

![Incident Report](docs/incident.png)
*Detailed view of a reported sanitation incident*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*The system consists of a React frontend communicating with a FastAPI backend, which stores data in SQLite and manages static uploads.*

**Application Workflow:**

![Workflow](docs/workflow.png)
*User Report -> Backend Incident Log -> Task Assigned -> Worker Resolves -> Verified & Closed*

---

### For Hardware:

#### Schematic & Circuit

![Circuit](docs/circuit.png)
*Wiring diagram connecting sensors to the microcontroller*

![Schematic](docs/schematic.png)
*Electronic schematic of the smart bin module*

#### Build Photos

![Team](docs/team.jpg)

![Components](docs/components.jpg)
*Arduino, Sensors, and Communication Modules*

![Build](docs/build_process.jpg)
*Assembling the smart bin prototype*

![Final](docs/final_product.jpg)
*The fully assembled Smart Littering System*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `http://127.0.0.1:8000/api`

##### Endpoints

**GET /api/incidents**
- **Description:** Retrieve a list of all reported incidents.
- **Response:**
```json
[
  {
    "id": 1,
    "description": "Overflowing bin at Main St",
    "status": "open",
    "timestamp": "2023-10-27T10:00:00"
  }
]
