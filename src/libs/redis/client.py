from typing import Optional

from redis import Redis

from src.configs.config import RedisConfig

class RedisCluster:
    def __init__(self, config: RedisConfig):
        self.rd = Redis(host=config.hosts, port=config.port)


    def get(self, key: str) -> Optional[str]:
        value: Optional[bytes] = self.rd.get(key)
        if value is not None:
            return value.decode('utf-8')
        return None
    
    def set(self, key, value):
        return self.rd.set(key, value)

    

if __name__ == '__main__':
    config = RedisConfig()
    rc = RedisCluster(config)
    rc.set('foo', 123456789)
    print(rc.get('foo'))