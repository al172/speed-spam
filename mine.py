print ("                                                                                  ")
print("░██████╗██████╗░███████╗███████╗██████╗░        ░██████╗██████╗░░█████╗░███╗░░░███╗")
print("██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗        ██╔════╝██╔══██╗██╔══██╗████╗░████║")
print("╚█████╗░██████╔╝█████╗░░█████╗░░██║░░██║        ╚█████╗░██████╔╝███████║██╔████╔██║")
print("░╚═══██╗██╔═══╝░██╔══╝░░██╔══╝░░██║░░██║        ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║")
print("██████╔╝██║░░░░░███████╗███████╗██████╔╝        ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║")
print("╚═════╝░╚═╝░░░░░╚══════╝╚══════╝╚═════╝░        ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝")
import pyautogui
from time import sleep
msg = input ("Enter your Msg ==> :")
num_msg = int(input("chose Your Number of Msg ==> :"))
time_msg = float(input("Chose Your Time of Msg ==> :"))

for num in range(num_msg + 1 ):
    pyautogui.typewrite(msg)
    sleep(time_msg)
    pyautogui.press('enter')
    sleep(time_msg)