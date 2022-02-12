''' Pre-release 
February 10th, 2022 '''


import time
import mouse
time.sleep(2)
me = mouse.get_position()
print(me)
mouse.move(550, 330, absolute=True, duration=0)
time.sleep(0.3)
mouse.click('left')
time.sleep(0.3)
mouse.move(820, 625, absolute=True, duration=0)
time.sleep(0.3)
iterations = 20
while iterations > 0:
    mouse.click('left')
    iterations -= 1
    time.sleep(95)

