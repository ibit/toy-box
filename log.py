import time
import logging

# ロギングの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_logs():
    count = 0
    while True:
        logging.info(f'This is log message number {count}')
        count += 1
        time.sleep(0.1)  

if __name__ == "__main__":
    generate_logs()