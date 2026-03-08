
# 🚀 Redundant Real-Time Telemetry Monitoring System

A fault‑tolerant telemetry visualization framework designed for mission‑critical environments such as propulsion testing and industrial monitoring systems.

This project implements a **dual‑server redundant telemetry architecture** capable of maintaining uninterrupted real‑time visualization even when one telemetry source becomes unavailable.

The system integrates **UDP-based telemetry streaming, heartbeat monitoring, automatic failover logic, multithreaded data acquisition, and real-time plotting**, ensuring stable monitoring under network failures or high data‑rate conditions.

---

# 📌 Project Overview

In telemetry monitoring systems, sensor data such as **pressure, temperature, flow rate, and vibration** must be continuously observed. Conventional monitoring architectures depend on a **single data acquisition source**, which introduces a **single point of failure**.

If the server stops transmitting data due to:

- network interruption
- packet loss
- hardware malfunction
- software crash

the visualization system immediately stops displaying telemetry data.

To address this limitation, this project introduces a **redundant dual‑server telemetry monitoring framework** capable of automatically switching to a standby source when the active server fails.

---

# 🏗 System Architecture

Telemetry Server 1 (Primary)
        │
        │ UDP Telemetry Stream
        ▼
Monitoring Application
 ┌─────────────────────────┐
 │ Receiver Thread (S1)    │
 │ Receiver Thread (S2)    │
 └─────────────────────────┘
        │
        ▼
 Queue Buffer System
        │
        ▼
Failover Monitoring Logic
        │
        ▼
Real-Time Plotting Engine

---

# ⚙ Key Features

### 🔁 Dual Server Redundancy
Two independent telemetry servers operate simultaneously to eliminate single points of failure.

### ⚡ Automatic Failover
If the active server stops transmitting telemetry packets, the system automatically switches to the standby server.

### 📡 UDP Telemetry Communication
Low-latency UDP protocol enables efficient real-time telemetry streaming.

### ❤️ Heartbeat Monitoring
Each received telemetry packet acts as a heartbeat signal indicating server availability.

### 🧵 Multithreaded Architecture
Separate receiver threads handle telemetry data reception without blocking the graphical interface.

### 📦 Queue-Based Buffering
Thread-safe queues ensure smooth communication between receiver threads and the plotting engine.

### ⏱ CDT Time Synchronization
Countdown timer data is mapped onto the X-axis to maintain accurate time representation.

### 🔄 Cooldown Switching Logic
Prevents unstable rapid switching during temporary network disturbances.

### 📉 Smooth Waveform Transition
Crossfade interpolation ensures smooth waveform continuity during server switching.

---

# 🧠 System Workflow

1. Telemetry servers transmit data packets over UDP.
2. Receiver threads listen to both telemetry streams.
3. Each packet updates the heartbeat timestamp of the server.
4. The monitoring engine checks the packet arrival interval.
5. If the active server fails to transmit packets within the timeout interval:
6. The system automatically switches to the standby server.
7. Cooldown logic prevents repeated switching during unstable network conditions.

---

# 🧪 System Validation

The system was evaluated under multiple operating conditions.

**Startup Failover Test**
The system automatically activates the redundant server when the primary server is unavailable during startup.

**Runtime Failure Test**
If the active server stops transmitting data during monitoring, the system detects the failure and switches automatically.

**Network Instability Test**
Cooldown logic prevents oscillation during intermittent packet loss.

**Queue Stress Test**
Queue buffering maintains smooth visualization under high data-rate conditions.

**Long Duration Stability Test**
The application runs continuously without:
- GUI freezing
- thread crashes
- memory leaks

---

# 🛠 Technology Stack

| Technology | Purpose |
|-----------|--------|
| Python | Core application development |
| Matplotlib | Real-time plotting |
| NumPy | Numerical processing |
| Threading | Parallel server communication |
| Queue | Thread-safe buffering |
| UDP Socket Programming | Telemetry data transmission |
| Dewesoft | Data acquisition platform |
| Spyder IDE | Development environment |

---

# 📂 Project Structure

telemetry-redundancy-system
│
├── main_app.py
├── DAS_Server_UDP_10_15_1.py
├── DAS_Redn_Sim.py
├── DAS_CDT_Reception10_9.py
├── csv_read_10_9.py
│
├── tg_7.csv
├── info_7.csv
│
├── README.md
├── LICENSE
└── .gitignore

---

# ▶ Installation

Install required dependencies:

pip install matplotlib numpy pandas

---

# ▶ Running the System

Start telemetry servers:

python DAS_Server_UDP_10_15_1.py
python DAS_Redn_Sim.py

Run monitoring application:

python main_app.py

---

# 📊 Example Visualization

Real-time telemetry waveform showing:

- continuous signal monitoring
- automatic server switching
- time-synchronized plotting

(Add a screenshot of your plotting window here.)

---

# 🔬 Future Improvements

Possible future enhancements:

- Multi-channel simultaneous visualization
- AI-based anomaly detection for telemetry signals
- Packet sequence integrity validation
- Secure telemetry communication
- GPU acceleration for high-frequency telemetry environments

---
📊 System Operation Screenshots
🔹 AUTO MODE – Before Switching

The monitoring system is operating in automatic mode while receiving telemetry data from the currently active server.
At this stage both servers are monitored, but no failover condition has occurred.

🔹 AUTO MODE – After Switching

When the active server stops transmitting telemetry packets, the system automatically detects the failure using the heartbeat timeout mechanism and switches to the redundant server.

🔹 MANUAL MODE – Before Switching

In manual mode, the operator has control over server selection.
The monitoring system continues plotting telemetry data from the currently selected server until a manual switch command is issued.

# ⚠ Security Note

Sensitive infrastructure details such as **network addresses, ports, and internal configurations have been removed or anonymized** from this repository.

---

# 👨‍💻 Author

**Govarthan S**

LinkedIn: www.linkedin.com/in/govarthan-s-7b7a623b5
 
GitHub: (https://github.com/gova-verse)

⭐ If you found this project useful, consider giving the repository a star.
