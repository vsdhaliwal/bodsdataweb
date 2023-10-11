import requests
from bs4 import BeautifulSoup
import threading
import logging
from datetime import datetime
import time
import os
from downloader import download_and_unzip_multiple_files, download_multiple_files
from data_inp_sanction import sanction_data_load
from data_inp_ownership import load_ownership_data

logger1 = logging.getLogger('Logger1')
logger1.setLevel(logging.INFO)
handler1 = logging.FileHandler('sanctioncrawl.log')
handler1.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler1.setFormatter(formatter)
logger1.addHandler(handler1)

logger2 = logging.getLogger('Logger2')
logger2.setLevel(logging.INFO)
handler2 = logging.FileHandler('ownershipcrawl.log')
handler2.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler2.setFormatter(formatter)
logger2.addHandler(handler2)

first_output = []
last_result = []

def opensanctions():
    url1 = "https://www.opensanctions.org/datasets/default/"
    response = requests.get(url1)
    response.raise_for_status()

    output_1 = []

    soup = BeautifulSoup(response.content, 'html.parser')

    link1 = soup.find("a", string="entities.ftm.json")

    if link1:
       file_url1 = link1["href"]
    else:
       print("links not found on the page.")


    timestamp_element = soup.find("time", class_="util_formattedDate__i6BYn")
    if timestamp_element and timestamp_element.has_attr("datetime"):
       last_changed = timestamp_element["datetime"].split("T")[0]
    else:
       print("Last changed timestamp not found on the page.")

    output_1.append([file_url1, last_changed])

    return output_1

def scrape_and_process_data():
    url1 = "http://127.0.0.1:5000"
    response = requests.get(url1)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all("a", string="JSON Download")

    output = []

    if links:
        for link in links:
            file_url = link["href"]
            card_title = link.find_previous("h5", class_="card-title serif").text.strip()
            name = card_title[:-12]
            date = card_title[-11:-1]
            output.append([name, date, file_url])

    return output

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created successfully.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def check_for_changes():
    global first_output
    global last_result

    while True:
        new_result = scrape_and_process_data()
        new_sanction = opensanctions()

        new_result = [item for item in new_result if item[2] in [
            'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/register/json.zip',
            'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/latvia/json.zip',
            'https://s3.eu-west-1.amazonaws.com/oo-bodsdata/data/gleif/json.zip'
        ]]

        if new_result != last_result:
            logger2.info("Ownership Data Changed: {}".format(new_result))
            links = []
            filenames = []
            for i in range(len(new_result)):
                filename = new_result[i][0].split()
                dater = new_result[i][1].replace("-", "_")
                #print(new_result[i][2]) 
                #print("./data/" + filename[0] + "_" + dater + ".json.zip")
                links.append(new_result[i][2])
                filenames.append("./ownership_data/" + filename[0] + "_" + dater + ".json.zip")
            print("Downloading...")
            download_and_unzip_multiple_files(links, filenames, "./ownership_data")
            print("Unzipped")
            print("Crawler Re-Started...")
            print("Data insertion Started...")
            all_files = os.listdir("./ownership_data")
            load_ownership_data(all_files)
            print("Data insertion Done")

        else:
            logger2.info("Ownership Data Unchanged at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        if new_sanction != first_output:
            logger1.info("Sanctions Data Changed: {}".format(new_sanction))
            links = []
            filenames = []
            links.append(new_sanction[0][0])
            filenames.append("./sanction_data/entities.ftm.json") 
            #print(links)
            #print(filenames)
            print("Downloading & Unziping ...")
            download_multiple_files(links, filenames)
            print("Unzipped")
            print("Crawler Re-Started...")
            print("Data insertion Started...")
            sanction_data_load()
            print("Data insertion Done")

        else:
            logger1.info("Sanctions Data Unchanged at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        last_result = new_result
        first_output = new_sanction
        time.sleep(43200)

if __name__ == "__main__":
    folder_path = './ownership_data'
    create_folder_if_not_exists(folder_path)
    folder_path = './sanction_data'
    create_folder_if_not_exists(folder_path)
    check_for_changes()

