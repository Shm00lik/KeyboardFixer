import win32clipboard
import pyautogui
import time


class Constants:
    ENGLISH_TO_HEBREW = {
        "q": "/",
        "w": "'",
        "e": "ק",
        "r": "ר",
        "t": "א",
        "y": "ט",
        "u": "ו",
        "i": "ן",
        "o": "ם",
        "p": "פ",
        "a": "ש",
        "s": "ד",
        "d": "ג",
        "f": "כ",
        "g": "ע",
        "h": "י",
        "j": "ח",
        "k": "ל",
        "l": "ך",
        ";": "ף",
        "z": "ז",
        "x": "ס",
        "c": "ב",
        "v": "ה",
        "b": "נ",
        "n": "מ",
        "m": "צ",
        ",": "ת",
        ".": "ץ",
        "/": ".",
        "'": ",",
    }

    HEBREW_TO_ENGLISH = {v: k for k, v in ENGLISH_TO_HEBREW.items()}

    class Modes:
        TO_HEBREW = "TO_HEBREW"
        TO_ENGLISH = "TO_ENGLISH"


def get_copied_text() -> str | None:
    win32clipboard.OpenClipboard()

    try:
        data = win32clipboard.GetClipboardData()
        time.sleep(0.1)
    except:
        data = None

    win32clipboard.CloseClipboard()

    return data


def copy_current_text() -> None:
    n = 0

    previousText = get_copied_text()

    print("Sending ctrl+c...")
    
    pyautogui.hotkey("ctrl", "c")

    print("Waiting for clipboard to update...")

    while n < 5 and previousText == get_copied_text():
        time.sleep(0.1)
        n += 1


def empty_clipboard() -> None:
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()


def set_copied_text(text: str) -> None:
    if not text:
        return

    print(text)
    empty_clipboard()
    win32clipboard.OpenClipboard()
    win32clipboard.SetClipboardText(text)
    win32clipboard.CloseClipboard()


def get_selected_text() -> str | None:
    currentCopy = get_copied_text()

    copy_current_text()
    text = get_copied_text()
    empty_clipboard()

    set_copied_text(currentCopy)

    return text


def main():
    print("Running in 3 seconds...")
    time.sleep(3)
    print("Running...")

    m = Constants.Modes.TO_ENGLISH

    selected_text = get_selected_text()

    print("Selected text: " + str(selected_text))
    if not selected_text:
        return

    fixed_text = ""

    for char in selected_text:
        if m == Constants.Modes.TO_HEBREW:
            fixed_text += Constants.ENGLISH_TO_HEBREW.get(char, char)
        else:
            fixed_text += Constants.HEBREW_TO_ENGLISH.get(char, char)

    print("Fixed text: " + fixed_text)


if __name__ == "__main__":
    main()
