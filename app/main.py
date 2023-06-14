from prometheus_client import start_http_server, Summary, Counter, Gauge
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
UPDATE_COUNT = Counter('update_count', 'Number of updates')
Gauge_COUNT = Gauge("instant_value", "Some test")


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    print('Time Fun')
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8080)
    print('Started...')
    # Generate some requests.
    while True:
        process_request(random.random())
        UPDATE_COUNT.inc(random.randint(1, 100))
        Gauge_COUNT.set(random.randint(1, 100))