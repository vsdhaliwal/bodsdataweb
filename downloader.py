import requests
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def download_large_file(url, local_filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    total_size = int(response.headers.get('content-length', 0))

    with open(local_filename, 'wb') as file:
        with tqdm(total=total_size, unit='B', unit_scale=True, desc=local_filename) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))

def download_multiple_files(urls, local_filenames):
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_large_file, urls, local_filenames)

urls = [
    'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/slovakia/json.zip',
    'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/slovakia/json.zip',
    'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/slovakia/json.zip'
]

local_filenames = ['file1.zip', 'file2.zip', 'file3.zip']

download_multiple_files(urls, local_filenames)
print(f'Downloads complete: {local_filenames}') 