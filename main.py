from qvd import qvd_reader

# reading qvd into pandas Dataformat
df = qvd_reader.read('products_source.qvd')

# export data format to csv
df.to_csv('products_source.csv')