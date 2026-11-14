import inotify_simple
from inotify_simple import INotify, flags

inotify = INotify()
watch_flags = (
    flags.CREATE # detect newly created files
    | flags.MODIFY # detect changed made to files
    | flags.DELETE # detect deleted files
    | flags.MOVED_FROM # detect files moved out of or renamed
    | flags.MOVED_TO # detect files moved in or renaemed
    | flags.CLOSE_WRITE # Detect when a writable file descriptor closes
)