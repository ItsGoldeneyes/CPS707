class Backend:
    def __init__(self) -> None:
        self.current_events = {}
        
    def import_events(self, current_events):
        # Import all lines from current events file except END code
        for event in current_events[:-1]:
            event_name = str(event[:15])
            event_tickets = int(event[15:])
            self.current_events[event_name] = event_tickets
        return True
    
    def export_events(self):
        # Export all events to current events file
        with open("current_events.txt", "w") as f:
            for key, value in self.current_events.items():
                f.write(f"{key}{value}\n")
            f.write("END____________ 0000")
        return True
    
    def delete_event(self, event):
        # Delete event from current events file
        del self.current_events[event]
        return True
    
    
    def edit_tickets(self, event, tickets):
        # Edit tickets for event
        self.current_events[event] += tickets
        return True