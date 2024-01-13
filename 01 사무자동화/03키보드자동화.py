import pyautogui
import pyperclip

# 1. 키보드 입력(문자) : 한글지원 안됨
# pyautogui.write('# Hello world!', interval=.05) 
# Hello world!

# 2. 키보드 입력(키)
# pyautogui.press('enter')
# Hello world!

# 3. 키보드 입력(여러 키 동시에)
# pyautogui.hotkey('ctrl', 'c') 
# Hello world!

# 4. 붙여넣기 : 한글 입력 가능
pyperclip.copy('Hello Python')
pyautogui.hotkey('ctrl', 'v')
# Hello Python
