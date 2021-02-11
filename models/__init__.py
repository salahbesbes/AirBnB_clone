from models.engine.file_storage import FileStorage

storage = FileStorage()
print("before read from file __obj", len(storage.all()))
storage.reload()
print("after read from file __obj", len(storage.all()))

