# test_Cowin.py
import pytest
from Task_20_Cowin import WindowsAutomation

def test_browserWindows():
    # Initialize the WindowsAutomation instance and assign the setup driver
    obj = WindowsAutomation()

    # Execute the browserWindows method and get the window handles
    windowsID = obj.browserWindows()

    # Assert that there are 3 windows (main window, FAQ, and Partners)
    assert len(windowsID) == 3, f"Expected 3 windows, but got {len(windowsID)} windows"