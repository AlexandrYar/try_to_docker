from redis import Redis
redis_cli = Redis(host='redis', port='6379', password='12345678', decode_responses= True)

def set_value(key, data):
    redis_cli.set(key, data)

def get_all_value(key):
    return redis_cli.get(key)