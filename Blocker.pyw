import time
from datetime import datetime as dt

#host_temp= "hosts"
hosts_path= r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
websites_list= ["www.youtube.com", "youtube.com", "facebook.com", "www.facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("sorry, working hours.")
        with open(hosts_path, "r+") as file:
            content=file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website+ "\n")
    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print("NOT working hours, have fun")
    time.sleep(5)
