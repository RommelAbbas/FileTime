import os
from idlelib import history

from inotify_simple import INotify, flags

inotify = INotify()

watch_flags = (
    flags.CREATE
    | flags.MODIFY
    | flags.DELETE
    | flags.MOVED_FROM
    | flags.MOVED_TO
    | flags.CLOSE_WRITE
)

watches = {}
history = []

def recursive_inotify(bas_path):
    for root, dirs, files in os.walk(bas_path):
        wd = inotify.add_watch(root, watch_flags)
        watches[wd] = root

recursive_inotify("/home/rommel/PyCharmMiscProject/FileTime")
while True:
    events = inotify.read()
    for event in events:
        print(flags.from_mask(event.mask), event.name)
        entry = {
            "action" : flags.from_mask(event.mask),
            "file" : event.name
        }
        full_path = os.path.join(watches[event.wd], events.name)
        history.append(entry)
        print(entry)