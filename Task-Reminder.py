# Python Script for Task - Reminder 

import time

from plyer import notification  # plyer library to generate notification

if __name__ == "__main__":
    TimeInterval = 3600     # Will give reminder every hour i.e., 3600 seconds. Can be customized as per requirement. 
    while True:
        notification.notify(
            title = "Reminder Title",
            message =  "Reminder Message",
            timeout = 10  
            # app_icon = "icon-path" (Optional)
        )
        time.sleep(TimeInterval)


"""

For reminder, this file can be run in background using the in-built Task Scheduler
                            or 
Another way is to use pythonw. Run the following line on the terminal:
    pythonw <nameOfFile.py>

"""