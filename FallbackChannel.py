import random

class FallbackChannel:
    def __init__(self):
        self.channels = ["SMS", "Email", "Push Notification", "Radio Broadcast"]

    def choose_fallback(self):
        # Randomly choose a fallback channel in case of primary communication failure
        fallback = random.choice(self.channels)
        print(f"Fallback communication channel selected: {fallback}")
        return fallback

    def send_message(self, message, primary_channel="Internet"):
        if self.check_channel_status(primary_channel):
            print(f"Sending message via {primary_channel}: {message}")
        else:
            print(f"Primary channel {primary_channel} unavailable.")
            fallback = self.choose_fallback()
            print(f"Sending message via fallback channel {fallback}: {message}")

    def check_channel_status(self, channel):
        # Simulate channel status check (80% chance of being available)
        return random.random() > 0.2

# Example usage
fallback_system = FallbackChannel()
fallback_system.send_message("This is an emergency broadcast.")
