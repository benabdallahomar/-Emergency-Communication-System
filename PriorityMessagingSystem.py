from datetime import datetime
import heapq

class Message:
    def __init__(self, sender, receiver, content, priority):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.priority = priority
        self.timestamp = datetime.now()

    def __lt__(self, other):
        # Messages are prioritized by priority value (lower is higher priority) and timestamp
        return (self.priority, self.timestamp) < (other.priority, other.timestamp)

class EmergencyCommunicationSystem:
    def __init__(self):
        self.message_queue = []

    def send_message(self, message):
        heapq.heappush(self.message_queue, message)
        print(f"Message sent from {message.sender} to {message.receiver} with priority {message.priority}")

    def process_messages(self):
        while self.message_queue:
            message = heapq.heappop(self.message_queue)
            self.deliver_message(message)

    def deliver_message(self, message):
        print(f"Delivering message to {message.receiver}: {message.content} (Priority: {message.priority})")

# Example usage
ecs = EmergencyCommunicationSystem()
ecs.send_message(Message("Admin", "Team A", "Emergency meeting at 5 PM", 1))
ecs.send_message(Message("Operator", "Team B", "Check system status", 3))
ecs.send_message(Message("Coordinator", "Team C", "Evacuate area immediately", 0))

ecs.process_messages()
