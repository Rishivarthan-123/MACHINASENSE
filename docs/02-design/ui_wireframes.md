# MACHINASENSE UI Wireframes

## 1. Purpose

This document defines the initial user interface structure for MACHINASENSE.

The UI will focus on simplicity because the primary users are factory owners, maintenance engineers, and technicians who may not have advanced technical or AI knowledge.

The interface should allow users to quickly answer:

1. How are my machines performing?
2. Which machines are at risk?
3. Why is a machine at risk?
4. What action should I take?

---

# 2. Application Structure

The application will contain the following major screens:

```text
Login
  │
  ▼
Dashboard
  │
  ├── Machines
  │     ├── Machine List
  │     ├── Machine Details
  │     └── Add Machine
  │
  ├── Sensor Data
  │     └── Upload CSV
  │
  ├── Predictions
  │     └── Prediction Details
  │
  ├── Alerts
  │
  └── Maintenance
        └── Maintenance History
```

---

# 3. Login Screen

## Purpose

Allow authorized users to securely access MACHINASENSE.

## Elements

```text
+------------------------------------------+
|              MACHINASENSE                |
|     Intelligent Manufacturing Platform   |
|                                          |
|  Email                                    |
|  [____________________________]           |
|                                          |
|  Password                                 |
|  [____________________________]           |
|                                          |
|             [ Login ]                     |
|                                          |
|  Don't have an account? Register          |
+------------------------------------------+
```

---

# 4. Dashboard

## Purpose

The dashboard provides an overview of the factory's machine health.

## Layout

```text
+------------------------------------------------------+
| MACHINASENSE                 User Profile   Logout   |
+------------------------------------------------------+
| Sidebar     |                                      |
|             |  Manufacturing Overview              |
| Dashboard   |                                      |
| Machines    |  +---------+ +---------+ +---------+ |
| Sensor Data |  | Machines| | Healthy | | Warning | |
| Predictions |  |   25    | |   18    | |    5    | |
| Alerts      |  +---------+ +---------+ +---------+ |
| Maintenance |                                      |
|             |  +-------------------------------+   |
|             |  | Machine Health Distribution   |   |
|             | |                               |   |
|             | |       [Chart]                 |   |
|             | +-------------------------------+   |
|             |                                      |
|             |  Critical Machines                   |
|             |  +-------------------------------+   |
|             |  | Machine | Health | Risk       |   |
|             |  |---------|--------|------------|   |
|             |  | CNC-01  |  42%   | HIGH       |   |
|             |  | Loom-04 |  51%   | MEDIUM     |   |
|             | +-------------------------------+   |
+------------------------------------------------------+
```

---

# 5. Machine List

## Purpose

Display all registered machines.

## Elements

```text
+------------------------------------------------------+
| Machines                              [ + Add ]      |
+------------------------------------------------------+
| Search machines...       Filter: [All ▼]             |
+------------------------------------------------------+
| Machine | Type | Status | Health | Last Update      |
|---------|------|--------|--------|------------------|
| CNC-01  | CNC  | Healthy|  92%   | 2 min ago        |
| CNC-02  | CNC  | Warning|  61%   | 3 min ago        |
| LOOM-01 | Loom | Critical| 38%   | 1 min ago        |
+------------------------------------------------------+
```

Users can select a machine to open its detailed health page.

---

# 6. Machine Details

## Purpose

Provide detailed information about a specific machine.

## Layout

```text
+------------------------------------------------------+
| ← Machines       CNC-01                              |
+------------------------------------------------------+
|                                                      |
| Machine Health                                       |
|                                                      |
|              92%                                     |
|          HEALTH SCORE                                |
|                                                      |
| Status: HEALTHY                                      |
|                                                      |
+------------------------------------------------------+
| Temperature | Vibration | Current | Pressure        |
|    68°C     |   2.1 mm/s|  12.4 A |  4.2 bar       |
+------------------------------------------------------+
|                                                      |
| Sensor Trends                                        |
|                                                      |
|        [ Temperature / Vibration Chart ]             |
|                                                      |
+------------------------------------------------------+
| AI Prediction                                        |
|                                                      |
| Failure Risk: LOW                                    |
| Confidence: 94%                                      |
|                                                      |
| Explanation:                                         |
| Current sensor readings remain within the expected   |
| operating range.                                     |
+------------------------------------------------------+
```

---

# 7. Sensor Data Upload

## Purpose

Allow users to upload historical sensor data during the MVP phase.

## Layout

```text
+------------------------------------------------------+
| Sensor Data Upload                                   |
+------------------------------------------------------+
|                                                      |
| Select Machine                                       |
| [ CNC-01                         ▼ ]                 |
|                                                      |
| Upload CSV File                                      |
|                                                      |
|       +--------------------------+                   |
|       |                          |                   |
|       |   Drag & Drop CSV Here   |                   |
|       |                          |                   |
|       |       [ Browse ]         |                   |
|       +--------------------------+                   |
|                                                      |
| Supported format: CSV                                |
|                                                      |
|              [ Upload Data ]                         |
+------------------------------------------------------+
```

The system should validate the uploaded file before processing it.

---

# 8. Predictions

## Purpose

Display AI-generated machine failure predictions.

## Layout

```text
+------------------------------------------------------+
| AI Predictions                                       |
+------------------------------------------------------+
|                                                      |
| Machine: CNC-01                                      |
|                                                      |
| Failure Risk                                         |
|                                                      |
|              18%                                     |
|              LOW                                     |
|                                                      |
| Confidence: 94%                                      |
|                                                      |
| Predicted Failure Window:                            |
| No significant failure risk detected                |
|                                                      |
| Key Factors                                          |
| ┌──────────────────────────────────────────────┐     |
| | Temperature          Normal                  |     |
| | Vibration            Slightly Elevated       |     |
| | Current              Normal                  |     |
| └──────────────────────────────────────────────┘     |
+------------------------------------------------------+
```

---

# 9. Alerts

## Purpose

Provide maintenance-related warnings.

## Layout

```text
+------------------------------------------------------+
| Alerts                                               |
+------------------------------------------------------+
|                                                      |
| 🔴 Critical                                          |
| LOOM-01 may require immediate inspection.            |
| Failure Risk: 87%                                    |
| [ View Machine ]                                     |
|                                                      |
| 🟠 Warning                                            |
| CNC-02 vibration level is increasing.               |
| [ View Machine ]                                     |
|                                                      |
| 🟢 Resolved                                           |
| CNC-04 temperature anomaly resolved.                |
+------------------------------------------------------+
```

Alerts should contain enough information for users to understand what happened and what action may be required.

---

# 10. Maintenance History

## Purpose

Track maintenance activities for each machine.

## Layout

```text
+------------------------------------------------------+
| Maintenance History                                  |
+------------------------------------------------------+
| Machine: CNC-01                                      |
+------------------------------------------------------+
| Date       | Type       | Description      | Status   |
|------------|------------|------------------|----------|
| 08-08-26   | Inspection | Bearing check    | Complete |
| 02-08-26   | Repair     | Motor repair     | Complete |
| 25-07-26   | Preventive | Lubrication      | Complete |
+------------------------------------------------------+
```

---

# 11. Navigation

The primary navigation will contain:

```text
Dashboard
Machines
Sensor Data
Predictions
Alerts
Maintenance
Settings
```

The navigation should remain consistent throughout the application.

---

# 12. UI Design Principles

## Simplicity

Users should understand machine health without requiring AI expertise.

## Information Hierarchy

Critical information should be visible immediately:

1. Critical machine failures
2. High-risk machines
3. Machine health
4. Sensor trends
5. AI explanations
6. Historical information

## Consistency

Buttons, tables, cards, forms, and navigation should use consistent layouts and interaction patterns.

## Responsiveness

The application should work on:

* Desktop
* Laptop
* Tablet

Mobile optimization will be considered in a future version.

## Accessibility

The UI should provide:

* Clear labels
* Readable typography
* Keyboard accessibility
* Meaningful error messages
* Accessible form controls

---

# 13. MVP Screens

The first release will implement:

* Login
* Dashboard
* Machine List
* Machine Details
* Sensor Data Upload
* Predictions
* Alerts
* Maintenance History

Future features such as real-time IoT monitoring and advanced AI assistance will be added incrementally.

---

# 14. Future UI

Future versions may include:

* Real-time sensor monitoring
* Live machine status
* Interactive factory map
* AI Maintenance Assistant
* Automated maintenance reports
* Energy analytics
* Computer vision inspection
* Multi-factory management

```
```
