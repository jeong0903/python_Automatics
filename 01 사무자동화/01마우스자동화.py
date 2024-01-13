import pyautogui
import time

# 1.화면크기 출력
# print(pyautogui.size())

# 2.마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 3.마우스 이동
# pyautogui.moveTo(36, 327)
# pyautogui.moveTo(36, 327, .5)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1)   # (1초당 클릭) * 3번

# 5. 마우스 드래그 : 360, 610 -> 520, 610
pyautogui.moveTo(360, 610, .5)
pyautogui.dragTo(530, 610, .5)