import csv
import time
import pandas as pd


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()


def search_by_client(address_file, client):
    file_csv = pd.read_csv(address_file, names=['path'])
    address_file_client = []
    file = file_csv.loc[:, 'path']
    for i in range(len(file)):
        file_adrress_client = []
        registr = file[i].title()
        if client in registr:
            name_file = file[i].split("\\")
            try:
                num_order = int(name_file[-1][:5])
                file_adrress_client.append(file[i])
                file_adrress_client.append(num_order)
                address_file_client.append(file_adrress_client)
            except ValueError:
                continue
    path = client + '.csv'
    csv_writer(address_file_client, path)


start_time = time.time()
search_by_client('good_address_file.csv', 'Спектрон')
print("--- %s seconds ---" % (time.time() - start_time))
