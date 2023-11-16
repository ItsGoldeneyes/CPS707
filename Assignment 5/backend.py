class Backend:
    def __init__(self) -> None:
        self.current_events = {}
        
    def import_events(self, current_events):
        # Import all lines from current events file except END code
        for event in current_events[:-1]:
            event_name = str(event[:15])
            event_tickets = int(event[15:20])
            event_name = event_name.replace("_"," ").strip()
            self.current_events[event_name] = event_tickets
        #    print(self.current_events)
        return True
    
    def export_events(self):
        # Export all events to current events file
        with open("current_events.txt", "w") as f:
            for key, value in self.current_events.items():
                f.write(f"{key}{value}\n")
        return True
    
    def delete_event(self, event):
        # Delete event from current events file
        event = event.replace("_", " ").strip()
        del self.current_events[event]
        return True
    
    
    def edit_tickets(self, event, tickets):
        # Edit tickets for event
        event = event.replace("_", " ").strip()
        self.current_events[event] += tickets
        return True