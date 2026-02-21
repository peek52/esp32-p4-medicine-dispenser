Import("env")
import os

# Fix Windows encoding issue for PlatformIO upload
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["PYTHONUTF8"] = "1"
