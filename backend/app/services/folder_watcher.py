from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.services.auto_importer import import_file

import time


class MemoryHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        print(
            "NEW FILE:",
            event.src_path
        )

        # Wait for file copy to finish
        time.sleep(5)

        try:

            result = import_file(
                event.src_path
            )

            print(
                "IMPORTED:",
                result
            )

        except Exception as e:

            print(
                "WATCHER ERROR:",
                e
            )


def start_watcher(folder_path):

    event_handler = MemoryHandler()

    observer = Observer()

    observer.schedule(
        event_handler,
        folder_path,
        recursive=True
    )

    observer.start()

    print(
        f"Watching: {folder_path}"
    )

    return observer