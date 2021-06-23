
import os
import requests
import shutil


def download_file(url, directory, fname=None):
    if fname == None:
        fname = os.path.basename(url)

    dl_path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        with open(dl_path, "wb") as f:
            shutil.copyfileobj(r.raw, f)
    return dl_path


def download_file_slower(url, directory=None):
    if directory == None:
        directory = os.path(os.path.dirname(
            os.path.abspath(__file__)), "downloads")

    os.makedirs(directory, exist_ok=True)

    local_filename = url.split('/')[-1]
    # NOTE the stream = True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(directory, local_filename), "web") as f:
            for chuk in r.iter_content(chunk_size=8192):
                if chuk:  # filter out keep-alive new chuks
                    f.write(chuk)

    return local_filename
