# import requests
# from bs4 import BeautifulSoup
# import threading

#url1 = "https://www.opensanctions.org/datasets/default/"
# url1 = "http://127.0.0.1:5000"

# response = requests.get(url1)
# response.raise_for_status()

# soup = BeautifulSoup(response.content, 'html.parser')

#link1 = soup.find("a", string="entities.ftm.json")
#link2 = soup.find("a", string="targets.nested.json")

#if link1:
#    file_url1 = link1["href"]
#    file_url2 = link2["href"]
#    print(f"The URL of entities.ftm.json is: {file_url1}")
#    print(f"The URL of targets.nested.json is: {file_url2}")
#else:
#    print("entities.ftm.json link not found on the page.")


#timestamp_element = soup.find("time", class_="util_formattedDate__i6BYn")
#if timestamp_element and timestamp_element.has_attr("datetime"):
#    last_changed = timestamp_element["datetime"].split("T")[0]
#    print(f"Last Changed: {last_changed}")
#else:
#    print("Last changed timestamp not found on the page.")

# links = soup.find_all("a", string="JSON Download")

# output = []
# result = []

# if links:
#     for link in links:
#         file_url = link["href"]
#         card_title = link.find_previous("h5", class_="card-title serif").text.strip()
#         name = card_title[:-12]
#         date = card_title[-11:-1]
#         output.append([name, date, file_url])
# else:
#     print("Json Zip links not found on the page.")

# result.append(output[0])
# result.append(output[1])
# result.append(output[-1])

# print(result)

#def printit():
#  threading.Timer(1.0, printit).start()
#  get_metadata()
#printit()

import requests
from bs4 import BeautifulSoup
import threading
import logging

logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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

def check_for_changes():
    global result
    new_result = scrape_and_process_data()

    if new_result != result:
        logging.info("Data changed: {}".format(new_result))
    else:
        logging.info("Data unchanged")

    result = new_result
    threading.Timer(60.0, check_for_changes).start() 

if __name__ == "__main__":
    result = scrape_and_process_data()
    check_for_changes()
