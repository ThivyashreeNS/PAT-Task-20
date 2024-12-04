# test_Labour.py
import pytest
from Task_20_Labour import WindowsAutomation

def test_downloadFiles():
    # Initialize the WindowsAutomation instance and assign the setup driver
    obj = WindowsAutomation()

    # Check if at least 10 images have been downloaded
    downloaded_photos = obj.downloadFiles()
    assert downloaded_photos == 10, f"Expected 10 photos, but found {downloaded_photos}."