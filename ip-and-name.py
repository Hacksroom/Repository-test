# We import the packages
import socket
# We define the instructions
# We bring the hostname with a method 
def run():
    print("Hey, How are you?, Welcome!!! this is our repository")
    answer = input("""
    Do you want to know your IP and hostname? 
    If your answer is yes, please write "y" 
    If your answer is not, please write "n"
    """)
    if answer == "y":
        # We bring the hostname with a method 
        hostname = socket.gethostname()
        # with the hostname, we bring the ip
        ip = socket.gethostbyname(hostname)
        # Show the information 
        print(f"""
        Your device's name is {hostname}
        And your IP is {ip} 
        Your welcome, have a nice day""")
        print("hey don´t forget it, we are your friends :3")
        # End of the script
    else:
         print("Ok don't worry, Anyway, i already know it")
         print("hey don´t forget it, we are your friends :3")
if __name__ == '__main__':
    run()
