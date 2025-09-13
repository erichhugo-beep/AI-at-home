import time

def run():
    print("[dummy] workload started")
    try:
        while True:
            # Simulate CPU work
            _ = sum(i*i for i in range(10000))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[dummy] workload stopped")
