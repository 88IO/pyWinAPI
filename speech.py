# coding:utf-8

import win32com.client
import sys


def main():
    SF = True
    try:
        if sys.argv[2]:
            SF = False
    except:
        pass

    try:
        speech = win32com.client.Dispatch("SaPi.SpVoice")
        try:
            speech.Rate = float(sys.argv[1])
        except:
            pass
        if SF:
            speech.Speak("起動完了しました。")
        else:
            print("起動・・・")
    except:
        print("失敗・・・")
        return

    while True:
        text = input("Speech >> ")
        if text == "exit":
            if SF:
                speech.Speak("終了します。")
                return
            else:
                print("終了・・・")
                return
        speech.Speak(text)


if __name__ == "__main__":
    main()
