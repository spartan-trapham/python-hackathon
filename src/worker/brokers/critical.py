from celery import Celery

critical = Celery()

if __name__ == '__main__':
    critical.start()
