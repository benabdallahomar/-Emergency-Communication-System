# Emergency Communication System

This repository contains the implementation of an Emergency Communication System designed to provide reliable and prioritized communication during critical situations. The system includes a priority messaging mechanism, real-time alerting, and fallback communication channels to ensure continuous communication even during network failures.

## Features

### Priority Messaging System
- Allows messages to be sent with different priority levels.
- Ensures that high-priority messages are delivered first.

### Real-Time Alerts System
- Monitors system status and triggers alerts based on predefined conditions.
- Notifies users in real-time about critical events.

### Fallback Communication Channel
- Automatically selects an alternative communication channel if the primary one fails.
- Supports SMS, Email, Push Notifications, and Radio Broadcasts as fallback options.

## Technologies Used
- Python
- threading for real-time monitoring
- heapq for priority queue management

## Getting Started

1. Clone the repository:
