import time
from datetime import datetime as dt

host_file_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'

block_list = ['https://www.amazon.com', 'www.amazon.com', 'https://www.ebay.com', 'www.ebay.com']
block_window = [8, 17]

host_header_text = '\n## custom host list for the website blocker\n'
host_content = '\n'.join(['{} {}'.format(redirect, host) for host in block_list])

last_status = 'UNK'
current_status = 'UNK'


def update_host_file():
    with open(host_file_path, 'r+') as file:
        content = file.read()
        if host_header_text in content:
            print('Content in the host file update, no need to add it again')
        else:
            file.write(host_header_text)
            file.write(host_content)
            print('Content in the host file updated')


def reset_host_file():
    with open(host_file_path, 'r') as file:
        content = file.read()

    if host_header_text in content:
        reset_content = content.replace(host_header_text, '')
        reset_content = reset_content.replace(host_content, '')

        with open(host_file_path, "w") as file:
            file.write(reset_content)

        print('Host file content is reset to default')
    else:
        print('Host file content is already reset to default, no need to do it again')


while True:
    current_date = dt.now()
    print('Current timestamp - {}'.format(current_date))

    if current_date.isoweekday() not in [6, 7] and block_window[0] < current_date.hour < block_window[1]:
        print('Process is inside - [block-window]')
        current_status = 'BLK'
    else:
        print("Process is inside - [non-block-window]")
        current_status = 'UNB'

    if current_status == 'BLK' and (last_status == 'UNB' or last_status == 'UNK'):
        print('State transition from-{} to-{}'.format(last_status, current_status))
        update_host_file()
    elif current_status == 'UNB' and (last_status == 'BLK' or last_status == 'UNK'):
        print('State transition from-{} to-{}'.format(last_status, current_status))
        reset_host_file()
    else:
        print('No state transition, no file operation required')

    last_status = current_status
    time.sleep(5)
