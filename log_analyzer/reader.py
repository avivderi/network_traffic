import csv

def load_csv(file_path):
    with open(file_path, "r") as f:
        list_network_traffic = [line for line in csv.reader(f)]
    return list_network_traffic
        
    
