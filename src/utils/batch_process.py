
def batch_generator(data, limit):
    i = 0
    while i < len(data):
        yield data[i:i + limit]
        i += limit