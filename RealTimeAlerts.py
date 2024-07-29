import time
import threading

class AlertSystem:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert_message):
        self.alerts.append(alert_message)
        print(f"Alert added: {alert_message}")

    def monitor_system(self):
        print("Monitoring system for alerts...")
        while True:
            if self.alerts:
                alert_message = self.alerts.pop(0)
                self.send_alert(alert_message)
            time.sleep(1)

    def send_alert(self, alert_message):
        print(f"Sending alert: {alert_message}")

# Example usage
alert_system = AlertSystem()
monitor_thread = threading.Thread(target=alert_system.monitor_system)
monitor_thread.start()

alert_system.add_alert("Severe weather warning")
alert_system.add_alert("System overload detected")
