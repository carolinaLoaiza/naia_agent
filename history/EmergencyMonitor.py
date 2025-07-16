# emergency/emergency_monitor.py

class EmergencyMonitor:
    def __init__(self):
        self.emergency_triggered = False

    def check_and_handle(self, symptom_data):
        severity = symptom_data.get("severity", "").lower()
        requires_attention = symptom_data.get("requires_attention", False)

        if severity == "severe" or requires_attention:
            self.emergency_triggered = True
            self.alert_emergency(symptom_data)
            return True  # Emergency action taken
        return False  # No emergency

    def alert_emergency(self, symptom_data):
        # Simulated call to emergency services
        print("🚨 EMERGENCY TRIGGERED! 🚨")
        print(f"Symptom details: {symptom_data}")
        # Here you could later integrate with a real API or notification system
