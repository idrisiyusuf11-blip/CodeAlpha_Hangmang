import os
import shutil
import time

# UI Colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def automate_files():
    print(f"{CYAN}====================================")
    print("   🚀 PYTHON FILE AUTOMATOR")
    print(f"===================================={RESET}")

    # Define paths (You can change these to actual paths on your PC)
    source_dir = "./my_downloads"
    target_dir = "./organized_images"

    # Create dummy folders for demonstration if they don't exist
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        # Create a dummy jpg to show it works
        open(f"{source_dir}/photo1.jpg", 'a').close()
        print(f"{YELLOW}Note: Created a dummy 'my_downloads' folder for demo.{RESET}")

    try:
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        files = os.listdir(source_dir)
        moved_count = 0

        print(f"Scanning {source_dir} for .jpg files...")
        time.sleep(1)

        for file in files:
            if file.lower().endswith(".jpg"):
                source_path = os.path.join(source_dir, file)
                target_path = os.path.join(target_dir, file)
                
                # Move the file
                shutil.move(source_path, target_path)
                print(f"{GREEN}✔ Moved:{RESET} {file}")
                moved_count += 1

        print(f"\n{CYAN}--- Automation Complete ---{RESET}")
        print(f"Total images moved: {moved_count}")
        print(f"Files are now in: {os.path.abspath(target_dir)}")

    except Exception as e:
        print(f"\n❌ {RED}Error occurred:{RESET} {e}")

if __name__ == "__main__":
    automate_files()