___
# Air Quality Management System🌍
___
Welcome to the Air Quality Management System (AQMS) project! This repository hosts the complete source code, documentation, and resources for building an advanced environmental monitoring system. The AQMS leverages the power of modern IoT devices, AI/ML algorithms, and 3D visualization to provide a comprehensive platform for monitoring and managing air quality in real-time. This project is designed for researchers, developers, and organizations passionate about sustainability and public health.
___
## Table of Contents
* Overview
* Features
* Architecture
* Technologies Used
___
## Overview
The AQMS is a cutting-edge solution designed to address the increasing need for effective air quality monitoring in urban and industrial environments. Inspired by the latest advancements in Industry 4.0, our system integrates:

1. Real-Time Monitoring: Collects live air quality data from IoT sensors.
2. Predictive Analytics: Uses machine learning to forecast trends and identify anomalies.
3. Interactive Visualization: Offers 3D views of air quality metrics for intuitive understanding.

This platform is open-source, scalable, and modular, making it adaptable to various use cases, including urban planning, industrial compliance, and public health monitoring.
___
## Features
### 🌟 Core Features:
* IoT-Driven Monitoring: Seamless integration with sensors using MQTT and AMQP protocols.
* AI-Powered Predictions: Accurate forecasting of air quality metrics like AQI, PM2.5, and PM10.
* Data Storage & Retrieval: Efficient time-series storage with InfluxDB.
* Interactive Dashboards: User-friendly interfaces built with Grafana.
* 3D Visualization: Immersive models built with Unity, integrated into Grafana dashboards.
* Scalability: Kubernetes-based deployment ensures high availability and fault tolerance.

### 🌐 Additional Capabilities:
* Support for multi-region monitoring.
* Configurable alerts and notifications.
* Historical data analysis and trend visualization.
* Modular architecture for easy extensibility.
* Ditto Integration: Advanced capabilities for managing and simulating IoT devices.
___
## Architecture
The AQMS is built on a microservices architecture, ensuring modularity, scalability, and maintainability. Below is a high-level overview of the system:

### Components:
#### 1. IoT Layer
* Sensors deployed in the field collect air quality data.
* Data is transmitted using MQTT and AMQP protocols to the system.
* Eclipse Ditto: Manages the digital twin representation of IoT devices, enabling seamless integration and monitoring.

#### 2. Processing Layer:
* Apache Kafka: Handles real-time data streaming.
* Kafka-ML: Integrates machine learning models for predictive analytics.

#### 3. Storage Layer
* InfluxDB: Stores time-series data from IoT sensors.

#### 4. Visualization Layer:
* Grafana: Displays real-time and historical data in customizable dashboards.
* Unity: Provides interactive 3D models for visual representation.

#### 5. Deployment Layer:
* Docker: Packages services into containers.
* Kubernetes: Orchestrates and manages containerized services.

## 🔧 Technologies Used

### Backend Technologies

* Eclipse Ditto: For digital twin creation and management.
* Apache Kafka: For real-time data streaming and processing.
* Node.js: For building high-performance APIs.

### Data Management

* InfluxDB: Time-series database for storing sensor data.
* Telegraf: Data collection agent for integrating with InfluxDB.

### Visualization

* Grafana: For creating custom dashboards and panels.
* Unity: For 3D visualization of air quality metrics.

### Machine Learning

* TensorFlow & PyTorch: For building and deploying predictive models.
* Kafka-ML: For seamless integration of ML models with data streams.

### Deployment

* Docker: For containerizing microservices.
* Kubernetes: For orchestrating containerized services.


## Links

- [Project Documentation](https://docs.google.com/document/d/1XviPpqcS2rh5lh2nsUYSRIaxFg3r1NHvLa8BCDi7I6w/edit?usp=sharing)
- [Project Repository](https://github.com/cepdnaclk/e19-co326-air-quality-management-system)
- [Project Page](https://cepdnaclk.github.io/e19-co326-air-quality-management-system/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)
