#!python3
# -*- coding:utf-8 -*-
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto


def main():
    # auto.ShowDesktop()
    subprocess.Popen('notepad.exe', shell=True)
    time.sleep(1)
    note = auto.WindowControl(searchDepth=1, ClassName='Notepad')
    note.SetActive()
    note.SetTopmost()
    transformNote = note.GetTransformPattern()
    transformNote.Move(400, 0)
    transformNote.Resize(400, 300)
    edit = note.EditControl()
    edit.SendKeys('{Ctrl}{End}{Enter 2}I\'m a topmost window!!!\nI cover other windows.')
    subprocess.Popen('mmc.exe devmgmt.msc')
    mmcWindow = auto.WindowControl(searchDepth=1, ClassName='MMCMainFrame')
    mmcWindow.SetActive()
    transformMmc = mmcWindow.GetTransformPattern()
    transformMmc.Move(100, 100)
    transformMmc.Resize(400, 300)
    time.sleep(1)
    auto.DragDrop(240, 116, 900, 110, 0.2)
    auto.DragDrop(900, 110, 240, 116, 0.2)
    mmcWindow.SendKeys('{Alt}f', waitTime=1)
    mmcWindow.SendKeys('X', charMode=False)  # or mmcWindow.SendKey(auto.Keys.VK_X)
    edit.SendKeys('{Ctrl}{End}{Enter 2}You close me.')
    vp = edit.GetValuePattern()
    if vp:
        print('current text:', vp.Value)
    auto.GetConsoleWindow().SetActive()


if __name__ == '__main__':
    main()
    input('Press Enter to exit')

