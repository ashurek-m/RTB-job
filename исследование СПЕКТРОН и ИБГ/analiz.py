import pandas as pd
import time, csv


def csv_writer(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


def search_by_client(address_file, client):
    file_csv = pd.read_csv(address_file, names=['path'])
    file_adrress_client = []
    order_number_client = []
    address_file_client = []
    file = file_csv.loc[:, 'path']
    for i in range(len(file)):
        registr = file[i].title()
        if client in registr:
            name_file = file[i].split("\\")
            try:
                num_order = int(name_file[-1][:5])
                file_adrress_client.append(file[i])
                order_number_client.append(num_order)
                address_file_client.append(file[i])
            except ValueError:
                continue
    path = client + '.csv'
    csv_writer(file_adrress_client, path)


start_time = time.time()
search_by_client('good_address_file.csv', 'Ibg')

print("--- %s seconds ---" % (time.time() - start_time))