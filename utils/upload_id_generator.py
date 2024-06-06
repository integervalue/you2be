import uuid

def genID():
    ID = str(uuid.uuid4())[:8]
    return ID