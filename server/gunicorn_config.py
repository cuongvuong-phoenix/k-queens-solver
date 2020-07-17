import multiprocessing

bind = '127.0.0.1:8000'
backlog = 2048

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 60 * 3.5
keepalive = 2
