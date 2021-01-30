import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title='Break needed',
            message='Please, take a break',
            app_icon='img/tomato_1.ico',
            timeout=10
        )
        time.sleep(60 * 25)
