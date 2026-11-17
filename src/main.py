from watchdog import events

for event in events.FileSystemEvent:
    print(event)