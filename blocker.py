import time
from datetime import datetime as dt

host_path='C:\Windows\System32\drivers\etc\hosts'  #path of host file
redirect_ip= '127.0.0.1'  #loopbackaddress

website_list = ['facebook.com', 'www.facebook.com', 'www.instagram.com']

start_time = dt(2020,9,26) # start time for blocking the mentioned sites
end_time = dt(2020,9,27)   # end time for blocking the mentioned sites


while True:
    if start_time < dt.now() < end_time:
        with open(host_path, mode='r+') as file:
            content = file.read()
            for web in website_list:
                if web in content:
                    pass
                else:
                    file.write(redirect_ip + ' ' + web + '\n')
        print(f'The websites mentioned {website_list} are blocked now.')

    else:
        with open(host_path, mode='r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(web in line for web in website_list):
                    file.write(line)
            file.truncate()
        print('Websites unblocked.')
        time.sleep(4)    



