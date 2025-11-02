import math
import csv
import os
import time
import pandas as pd

from ctypes import *
from sys import platform
from time import sleep
from sys import platform, exit, getsizeof
from datetime import datetime

# Local modules
from helpers import *
from button_pressed import *
from constants import *
from struct_defs import *

def clear_terminal():
	os.system('cls' if os.name == 'nt else' else 'clear')
def center_text(text, width):
	return text.center(width)

def big_banner(width):
    lines = [
        "████████ ███████ ██    ██ ████████  ████ ██      ███████    █████  ██████  ██████  ███████ ███████ ███████ ███████  ",
        "   ██    ██       ██  ██     ██      ██  ██      ██         ███    ██     ██    ██ ██   ██ ██   ██ ██      ██     ██",
        "   ██    █████      ██       ██      ██  ██      ██████       ███  ██     ████████ ██   ██ ██   ██ ███████ ███████   ",
        "   ██    ██        ██ ██     ██      ██  ██      ██            ███ ██     ██    ██ ██   ██ ██   ██ ██      ██    ██  ",
        "   ██    ███████ ██     ██   ██     ████ ███████ ███████    █████  ██████ ██    ██ ██   ██ ██   ██ ███████ ██     ██ "
    ]
    return [center_text(line, width) for line in lines]

def terminal_gui():
    width = 120 
    clear_terminal()
    border_top = "╔" + "═" * (width - 2) + "╗"
    border_empty = "║" + " " * (width - 2) + "║"
    border_bottom = "╚" + "═" * (width - 2) + "╝"

    while True:
        clear_terminal()
        print(border_top)
        # Empty lines for padding
        for _ in range(2): print(border_empty)
        # Print the big banner, centered
        for line in big_banner(width - 2):
            print("║" + line + "║")
        for _ in range(2): print(border_empty)
        print(border_bottom)

        # Instructions, centered under the box
        print("\n" + center_text(">> Press the button to initiate scan <<", width))
        
        # Simulate button press (replace with your actual function)
        user_input = input(center_text(">", width)).strip().lower()
        if user_input == '':
           print(print(center_text("Now Scanning", width)))
           break
        
        
if __name__ == "__main__":
	terminal_gui()
	if platform == "linux":
		bin_lib_path = "./nir-final-main/lib/libmetascan-RPI.so"
	elif platform == "win32":
		bin_lib_path = "./lib/libmetascan.dll"
	nir_lib = cdll.LoadLibrary(bin_lib_path)
	
	# Get Library Version
	major = c_uint32()
	minor = c_uint32()
	version = c_uint32()
	get_lib_res = nir_lib._Z17GetLibraryVersionPiS_S_(byref(major), byref(minor), byref(version))
	if (get_lib_res != 0):
		raise Exception("Unable to fetch the library version")
	print(f"LIBRARY VERSION: {major.value}.{minor.value}.{version.value}", )
		# Open Device
	open_res = nir_lib._Z10OpenIscDevv()
	if (open_res != 0):
		raise Exception("Opening NIR Device unsuccessful.")	
	print("Scanner ready. Press button to initiate scan.")
		# Wait for button press to scan
		# Perform Scan
	print("Scanning...")
	perform_scan_read_res = nir_lib._Z19PerformScanReadDatav()
	if (perform_scan_read_res != 0):
		raise Exception("Scanning unsuccessful")
	print("Scan completed")
		
		
	print("Getting scan result")
	# c_wavelength_array = ctypes.c_double * 864
	scan_result = ScanResult()
	get_scan_result_res = nir_lib._Z13GetScanResultP10ScanResult(byref(scan_result))
	if (get_scan_result_res != 0):
		raise Exception("Unable to get scan result.")
		
	print("SCAN RESULT:")
	print(f"\tWavelength: {scan_result.wavelength}")
	print(f"\tIntensity: {scan_result.intensity}")
	print(f"\tLength: {scan_result.length}")
		
	for i in range(864):
		wavelength_val = scan_result.wavelength[i]
		intensity_val = scan_result.intensity[i]
		print(i, wavelength_val, intensity_val)
		if i == 54 and intensity_val in range (16276, 22503):
			print("████████ ███████ ██   ██ ████████ ██ ██      ███████      ██████  ██████  ███    ██ ████████  █████  ██ ███    ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ████   ██    ██    ██   ██ ██ ████   ██ ██      ")
			print("   ██    █████     ███      ██    ██ ██      █████       ██      ██    ██ ██ ██  ██    ██    ███████ ██ ██ ██  ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ██  ██ ██    ██    ██   ██ ██ ██  ██ ██      ██ ")
			print("   ██    ███████ ██   ██    ██    ██ ███████ ███████      ██████  ██████  ██   ████    ██    ██   ██ ██ ██   ████ ███████ ")
			print("                                                                                            ")
			print("███████ ██ ██      ██   ██    ")
			print("██      ██ ██      ██  ██     ")
			print("███████ ██ ██      █████      ")
			print("     ██ ██ ██      ██  ██     ")
			print("███████ ██ ███████ ██   ██    ")
			break
		elif i == 54 and intensity_val in range (25567, 29999):
			print("████████ ███████ ██   ██ ████████ ██ ██      ███████      ██████  ██████  ███    ██ ████████  █████  ██ ███    ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ████   ██    ██    ██   ██ ██ ████   ██ ██      ")
			print("   ██    █████     ███      ██    ██ ██      █████       ██      ██    ██ ██ ██  ██    ██    ███████ ██ ██ ██  ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ██  ██ ██    ██    ██   ██ ██ ██  ██ ██      ██ ")
			print("   ██    ███████ ██   ██    ██    ██ ███████ ███████      ██████  ██████  ██   ████    ██    ██   ██ ██ ██   ████ ███████ ")
			print("                                                                                            ")
			print("██████   ██████  ██      ██    ██ ███████ ███████ ████████ ███████ ██████      ")
			print("██   ██ ██    ██ ██       ██  ██  ██      ██         ██    ██      ██   ██     ")
			print("██████  ██    ██ ██        ████   █████   ███████    ██    █████   ██████      ")
			print("██      ██    ██ ██         ██    ██           ██    ██    ██      ██   ██     ")
			print("██       ██████  ███████    ██    ███████ ███████    ██    ███████ ██   ██     ")
			break
		elif i == 54 and intensity_val in range (30000, 36399):
			print("████████ ███████ ██   ██ ████████ ██ ██      ███████      ██████  ██████  ███    ██ ████████  █████  ██ ███    ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ████   ██    ██    ██   ██ ██ ████   ██ ██      ")
			print("   ██    █████     ███      ██    ██ ██      █████       ██      ██    ██ ██ ██  ██    ██    ███████ ██ ██ ██  ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ██  ██ ██    ██    ██   ██ ██ ██  ██ ██      ██ ")
			print("   ██    ███████ ██   ██    ██    ██ ███████ ███████      ██████  ██████  ██   ████    ██    ██   ██ ██ ██   ████ ███████ ")
			print("                                                                                            ")
			print("██      ██ ███    ██ ███████ ███    ██ ")
			print("██      ██ ████   ██ ██      ████   ██ ")
			print("██      ██ ██ ██  ██ █████   ██ ██  ██ ")
			print("██      ██ ██  ██ ██ ██      ██  ██ ██ ")
			print("███████ ██ ██   ████ ███████ ██   ████ ")
			break
		elif i == 54 and intensity_val in range (45000, 51219):
			print("████████ ███████ ██   ██ ████████ ██ ██      ███████      ██████  ██████  ███    ██ ████████  █████  ██ ███    ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ████   ██    ██    ██   ██ ██ ████   ██ ██      ")
			print("   ██    █████     ███      ██    ██ ██      █████       ██      ██    ██ ██ ██  ██    ██    ███████ ██ ██ ██  ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ██  ██ ██    ██    ██   ██ ██ ██  ██ ██      ██ ")
			print("   ██    ███████ ██   ██    ██    ██ ███████ ███████      ██████  ██████  ██   ████    ██    ██   ██ ██ ██   ████ ███████ ")
			print("                                                                                            ")
			print("██     ██  ██████   ██████  ██      ")
			print("██     ██ ██    ██ ██    ██ ██      ")
			print("██  █  ██ ██    ██ ██    ██ ██      ")
			print("██ ███ ██ ██    ██ ██    ██ ██      ")
			print(" ███ ███   ██████   ██████  ███████ ")
			break
		elif i == 54 and intensity_val in range (57617, 70000):
			print("████████ ███████ ██   ██ ████████ ██ ██      ███████      ██████  ██████  ███    ██ ████████  █████  ██ ███    ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ████   ██    ██    ██   ██ ██ ████   ██ ██      ")
			print("   ██    █████     ███      ██    ██ ██      █████       ██      ██    ██ ██ ██  ██    ██    ███████ ██ ██ ██  ██ ███████ ")
			print("   ██    ██       ██ ██     ██    ██ ██      ██          ██      ██    ██ ██  ██ ██    ██    ██   ██ ██ ██  ██ ██      ██ ")
			print("   ██    ███████ ██   ██    ██    ██ ███████ ███████      ██████  ██████  ██   ████    ██    ██   ██ ██ ██   ████ ███████ ")
			print("                                                                                            ")
			print(" ██████  ██████  ████████ ████████  ██████  ███    ██ ")
			print("██      ██    ██    ██       ██    ██    ██ ████   ██ ")
			print("██      ██    ██    ██       ██    ██    ██ ██ ██  ██ ")
			print("██      ██    ██    ██       ██    ██    ██ ██  ██ ██ ")
			print(" ██████  ██████     ██       ██     ██████  ██   ████ ")
			break
		elif i == 54 and intensity_val <3799:
			print("███    ██  ██████      ████████ ███████ ██   ██ ████████ ██ ██      ███████   ")
			print("████   ██ ██    ██        ██    ██       ██ ██     ██    ██ ██      ██        ")
			print("██ ██  ██ ██    ██        ██    █████     ███      ██    ██ ██      █████     ")
			print("██  ██ ██ ██    ██        ██    ██       ██ ██     ██    ██ ██      ██        ")
			print("██   ████  ██████         ██    ███████ ██   ██    ██    ██ ███████ ███████   ")
			break
		elif i == 54 and intensity_val >71000:
			print("███    ██  ██████      ████████ ███████ ██   ██ ████████ ██ ██      ███████  ")
			print("████   ██ ██    ██        ██    ██       ██ ██     ██    ██ ██      ██       ")
			print("██ ██  ██ ██    ██        ██    █████     ███      ██    ██ ██      █████    ")
			print("██  ██ ██ ██    ██        ██    ██       ██ ██     ██    ██ ██      ██       ")
			print("██   ████  ██████         ██    ███████ ██   ██    ██    ██ ███████ ███████  ")	
			break
	close_res=nir_lib._Z11CloseIscDevv()
	if (close_res!=0):
		raise Exception("NIR Device not successfully closed.")




