# CloudPulse - VM Monitoring Dashboard

A lightweight cloud monitoring system that tracks live CPU, memory, and disk 
metrics from a remote VM, displays them on a web dashboard, and sends email 
alerts when thresholds are breached.

## Architecture
[Target VM]                    [Monitor VM]
Node Exporter :9100  ------>  Prometheus :9090
Grafana :3000
Flask Dashboard :5000

## Tech Stack

- Python, Flask
- Prometheus, Grafana
- Node Exporter
- Docker
- Oracle Cloud (Ubuntu 22.04)
- smtplib (email alerting)

## Setup Instructions

### Prerequisites
- Two Ubuntu 22.04 VMs
- Docker installed on monitor VM
- Ports 9090, 3000, 5000, 9100 open

### 1. Clone the repo
```bash
git clone https://github.com/Jeffrie-04/cloudpulse.git
cd cloudpulse
```

### 2. Create config.py with your email credentials
```python
EMAIL_SENDER = "your-email@gmail.com"
EMAIL_RECEIVER = "your-email@gmail.com"
APP_PASSWORD = "your-app-password"
```

### 3. Build and run the Docker container
```bash
docker build -t cloudpulse .
docker run -d -p 5000:5000 --name cloudpulse-app cloudpulse
```

### 4. Access the dashboard
http://<monitor-vm-ip>:5000

## Screenshots

### Flask Dashboard
<img width="754" height="306" alt="Screenshot 2026-04-17 at 12 44 42 PM" src="https://github.com/user-attachments/assets/15f44829-a2f0-4596-9ff7-73d239bc9e8a" />


### Grafana Dashboard
<img width="1399" height="818" alt="Screenshot 2026-04-17 at 12 46 20 PM" src="https://github.com/user-attachments/assets/70f97973-e163-4431-9f0b-3e2dfe588fc3" />


## Alerts
Email alerts are triggered when:
- CPU usage exceeds 80%
- Memory usage exceeds 90%
