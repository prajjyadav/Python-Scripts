#Coded by Timothy Chua
#A script to generate mouse movements and clicks to prevent idle status from various applications.

import pyautogui as auto #The library that contains the automation


if __name__ == "__main__":

  width, height = auto.size() #Screen Size
  print(width, height)

  while(True):
    auto.moveTo(5, 5, duration = 2) #Move to upper left corner
    auto.click()
    auto.moveTo(width-5, 5, duration = 2) #Move to upper right corner
    auto.click()
    auto.moveTo(width-5, height-5, duration = 2) #Move to lower right corner
    auto.click()
    auto.moveTo(5, height-5, duration = 2) #Move to lower left corner
    auto.click()
