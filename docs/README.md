---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e19-co326-air-quality-management-system
title: Air Quality Management System
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Air Quality Management System

---

<!-- 
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)

![Sample Image](./images/sample.png)
 -->

## Team
-  E/19/133, HARISHANTH A., [email](e19133@eng.pdn.ac.lk)
-  E/19/134, HARNAN M., [email](e19134@eng.pdn.ac.lk)
-  E/19/137, HAYANAN T., [email](e19137@eng.pdn.ac.lk)
-  E/19/142, ILLANGARATHNE Y.M.H.V., [email](e19142@eng.pdn.ac.lk)
-  E/19/155, JAYARATHNA B.R.U.K., [email](e19155@eng.pdn.ac.lk)
-  E/19/163, JAYASUNDARA J.M.E.G., [email](e19163@eng.pdn.ac.lk)
-  E/19/166, JAYATHUNGA W.W.K., [email](e19166@eng.pdn.ac.lk)
-  E/19/167, JAYAWARDENA H.D.N.S., [email](e19167@eng.pdn.ac.lk)
-  E/19/170, JAYAWARDHANA, [email](e19170@eng.pdn.ac.lk)
-  E/19/193, KAUSHALYA N.V.K., [email](e19193@eng.pdn.ac.lk)
-  E/19/205, KUMARA I.P.S.N.U., [email](e19205@eng.pdn.ac.lk)
-  E/19/210, KUMARASIRI R.P.J.R., [email](e19210@eng.pdn.ac.lk)
-  E/19/226, MADHUSHANKA K.G.M., [email](e19226@eng.pdn.ac.lk)
-  E/19/227, MADHUSHANKA M.P.J., [email](e19227@eng.pdn.ac.lk)
-  E/19/236, MANIKDIWELA W.L., [email](e19236@eng.pdn.ac.lk)

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Technologies Used](#technologies-used)
5. [Links](#links)

---

## Overview
The AQMS is a cutting-edge solution designed to address the increasing need for effective air quality monitoring in urban and industrial environments. Inspired by the latest advancements in Industry 4.0, our system integrates:

1. Real-Time Monitoring: Collects live air quality data from IoT sensors.
2. Predictive Analytics: Uses machine learning to forecast trends and identify anomalies.
3. Interactive Visualization: Offers 3D views of air quality metrics for intuitive understanding.

This platform is open-source, scalable, and modular, making it adaptable to various use cases, including urban planning, industrial compliance, and public health monitoring.

 description of the real world problem and solution, impact

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
.....

## Links

- [Project Repository](https://github.com/cepdnaclk/e19-co326-air-quality-management-system)
- [Project Page](https://cepdnaclk.github.io/e19-co326-air-quality-management-system/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)


[//]: # (Please refer this to learn more about Markdown syntax)
[//]: # (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
