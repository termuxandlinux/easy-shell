import os
import subprocess

def execute_shell_script(script_name):
    try:
        print("Executing script:", script_name)  # Print the script name before executing
        subprocess.Popen(["bash", script_name])
    except Exception as e:
        print(f"Error executing script {script_name}: {e}")

def print_ascii_art():
    print("\033[H\033[J")  # Clear screen and move cursor to top-left
    print("\033[92m")  # Green color
    print(r"""
        ,----,    ,--,
      ,/   .`| ,---.'|
    ,`   .'  : |   | :
  ;    ;     / :   : |
.'___,/    ,'  |   ' :
|    :     |   ;   ; '
;    |.';  ;   '   | |__
`----'  |  |   |   | :.'|
    '   :  ;   '   :    ;
    |   |  '   |   |  ./
    '   :  |   ;   : ;
    ;   |.'    |   ,/
    '---'      '---'
   [Available on (Ubuntu/Debian/Kali/Termux)] 
   [v.1.0]
   [© By Termux & Linux]
   """)
    print("\033[0m")  # Reset color

def print_menu(menu_items, start_index):
    print("Menu:")
    for index, (name, _) in enumerate(menu_items[start_index:start_index+10], start=start_index+1):
        print(f"[{index}] {name}")
    print("[0] Exit")
    print("[99] Make all scripts executable")
    print("[+] Scroll down")
    print("[-] Scroll up")

def main():
    # Get the full path of the .shell directory
    scripts_directory = os.path.join(os.getcwd(), ".shell")
    print("Scripts directory:", scripts_directory)
    
    menu_items = [("base", ".shell/base.sh"), ("discord", ".shell/discord.sh"), ("termux", ".shell/termux.sh"), ("proot", ".shell/proot.sh"), ("Browser", ".shell/browser.sh"), ("Phishing", "phishing.sh")]

    script_files = os.listdir(scripts_directory)
    for script_file in script_files:
        menu_items.append((script_file, os.path.join(scripts_directory, script_file)))
    
    start_index = 0  # Initialize start_index here

    while True:
        print_ascii_art()
        print_menu(menu_items, start_index)
        choice = input("Please choose an option: ")
        if choice == '0':
            print("Exiting program.")
            break
        elif choice == '99':
            for script_name in script_files:
                script_path = os.path.join(scripts_directory, script_name)
                os.system(f"chmod +x {script_path}")
            print("All scripts have been made executable.")
        elif choice == '+':
            start_index += 10
        elif choice == '-':
            start_index -= 10
            if start_index < 0:
                start_index = 0
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= len(menu_items):
                    script_name = menu_items[start_index + choice - 1][1]
                    print_ascii_art()  # Hide the menu before executing the script
                    execute_shell_script(script_name)
                    input("Press Enter to continue...")
                else:
                    print("Invalid option. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
