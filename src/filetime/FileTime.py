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
    for root, dirs, files in os.walk("/home/rommel/filetime-test"):
        inotify.add_watch(root, watch_flags)


# # Watch all existing directories
# for root, dirs, files in os.walk("/home/rommel/filetime-test"):
#     # print(root, dirs, files)
#     inotify.add_watch(root, watch_flags)
#     print("Watching:", root)
#
# # Listen for changes
# while True:
#     for event in inotify.read():
#         print(flags.from_mask(event.mask), event.name)