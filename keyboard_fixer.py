import win32clipboard
import keyboard
import time


def getCopiedText() -> str | None:
    win32clipboard.OpenClipboard()
    
    try:
        data = win32clipboard.GetClipboardData()
    except:
        data = None

    win32clipboard.CloseClipboard()
    
    return data


def copyCurrentText() -> None:
    n = 0
    
    previousText = getCopiedText()
    keyboard.press_and_release('ctrl + c')

    while n < 5 and previousText == getCopiedText():
        time.sleep(0.1)
        n += 1


def emptyClipboard() -> None:
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()


def setCopiedText(text: str) -> None:
    emptyClipboard()
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardText(text if text else '')
    win32clipboard.CloseClipboard()


def getSelectedText() -> str | None:
    currentCopy = getCopiedText()

    copyCurrentText()
    text = getCopiedText()
    emptyClipboard()

    setCopiedText(currentCopy)

    return text


def main():
    print(getSelectedText())


if __name__ == '__main__':
    main()