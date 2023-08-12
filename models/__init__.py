"""This file contains the global variable storage which
is used to store and reload the saved objects to memory.
"""


from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
