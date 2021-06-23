import os
import requests
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

urls = ["https://images.unsplash.com/photo-1610085927744-7217728267a6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=329&q=80",
        "https://images.unsplash.com/photo-1613226505855-999302e0c08d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80"]
index = 2
for url in urls:
    download_file(url, DOWNLOAD_DIR, f"{index}.jpg")
    index = index+1

# r = requests.get(urls[0], stream=True)
# r.raise_for_status()  # 200
# with open(os.path.join(DOWNLOAD_DIR, "1.jpg"), "wb") as f:
#     f.write(r.content)
