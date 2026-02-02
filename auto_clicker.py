#!/usr/bin/env python3
"""
Simple Auto-Clicker for Multiple Points
Press Ctrl+C to stop the program
"""

import pyautogui
import time
from pynput import mouse

# Configure PyAutoGUI
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort

# Define the points to click (x, y coordinates)
CLICK_POINTS = []

# Configuration
DELAY_BETWEEN_CLICKS = 1  # seconds between each click
DELAY_BETWEEN_CYCLES = 1  # seconds between completing all points
CLICK_COUNT = 1  # number of clicks per point

def get_screen_size():
    """Display screen dimensions"""
    width, height = pyautogui.size()
    print(f"Screen size: {width}x{height}")
    return width, height

def select_points_by_clicking():
    """Click to select multiple points"""
    global CLICK_POINTS
    CLICK_POINTS = []
    
    print("\n=== Click to Select Points ===")
    print("Left-click to add a point")
    print("Right-click to finish selecting")
    print("\nWaiting for clicks...")
    
    def on_click(x, y, button, pressed):
        if pressed:
            if button == mouse.Button.left:
                CLICK_POINTS.append((x, y))
                print(f"Point {len(CLICK_POINTS)} added: ({x}, {y})")
            elif button == mouse.Button.right:
                print("\nSelection complete!")
                return False  # Stop listener
    
    # Start listening for mouse clicks
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    
    if CLICK_POINTS:
        print(f"\nTotal points selected: {len(CLICK_POINTS)}")
        for i, (x, y) in enumerate(CLICK_POINTS, 1):
            print(f"  Point {i}: ({x}, {y})")
    else:
        print("\nNo points selected!")

def display_mouse_position():
    """Show current mouse position (useful for finding coordinates)"""
    print("\nMove your mouse to the desired positions.")
    print("Press Ctrl+C when done.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Position: X={x:4d} Y={y:4d}", end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n")

def auto_click():
    """Perform auto-clicking at multiple points"""
    if not CLICK_POINTS:
        print("\nNo points selected! Please select points first (Option 2).")
        return
    
    print("\n=== Auto-Clicker Started ===")
    print(f"Clicking {len(CLICK_POINTS)} points")
    print(f"Delay between clicks: {DELAY_BETWEEN_CLICKS}s")
    print(f"Delay between cycles: {DELAY_BETWEEN_CYCLES}s")
    print("\nStarting in 3 seconds... (Move mouse to top-left corner to abort)")
    time.sleep(3)
    
    try:
        cycle = 1
        while True:
            print(f"\n--- Cycle {cycle} ---")
            
            for i, (x, y) in enumerate(CLICK_POINTS, 1):
                print(f"Clicking point {i}: ({x}, {y})")
                pyautogui.click(x, y, clicks=CLICK_COUNT)
                time.sleep(DELAY_BETWEEN_CLICKS)
            
            print(f"Cycle {cycle} completed. Waiting {DELAY_BETWEEN_CYCLES}s...")
            time.sleep(DELAY_BETWEEN_CYCLES)
            cycle += 1
            
    except KeyboardInterrupt:
        print("\n\n=== Auto-Clicker Stopped ===")
    except pyautogui.FailSafeException:
        print("\n\n=== Failsafe triggered! Mouse moved to corner. ===")

def main():
    """Main function"""
    print("=" * 50)
    print("Python Auto-Clicker for Multiple Points")
    while True:
        print("\nOptions:")
        print("1. Start auto-clicking")
        print("2. Select points by clicking (Left-click to add, Right-click to finish)")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == "1":
            auto_click()
        elif choice == "2":
            select_points_by_clicking()

if __name__ == "__main__":
    main()
