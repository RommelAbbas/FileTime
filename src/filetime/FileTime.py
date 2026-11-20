import os
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

wd = {}

def recursive_inotify(bas_path):
    for root, dirs, files in os.walk(bas_path):
        inotify.add_watch(root, watch_flags)


events = inotify.read()