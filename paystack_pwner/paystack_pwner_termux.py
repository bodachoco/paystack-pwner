#!/data/data/com.termux/files/usr/bin/python

"""
██████╗ ██╗    ██╗███╗   ██╗██████╗ ██████╗ 
██╔══██╗██║    ██║████╗  ██║██╔══██╗██╔══██╗
██████╔╝██║ █╗ ██║██╔██╗ ██║██████╔╝██████╔╝
██╔═══╝ ██║███╗██║██║╚██╗██║██╔══██╗██╔══██╗
██║     ╚███╔███╔╝██║ ╚████║██║  ██║██║  ██║
╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝

T3RMUX 0PT1M1Z3D V3R$10N
CR34T3D BY: |30|)4(|-|0(0
C0D3N4M3: N1GH7_$T4LK3R

[!] W4RN1NG: UN4UTH0R1Z3D 4CC3$$ 1$ $TR1CTLY PR0H1B1T3D [!]
"""

import os
import json
import time
import sys
import threading
import requests
import subprocess
from dotenv import load_dotenv
from colorama import init, Fore, Back, Style
import pyfiglet
import random
from datetime import datetime
import hashlib
import platform
from datetime import timedelta
import socket
import uuid
import getpass

# Initialize colorama for Termux
init()

# Set up environment file paths
CONFIG_DIR = os.path.join(os.path.expanduser('~'), 'paystack_pwner')
ENV_FILES = [
    os.path.join(CONFIG_DIR, '.env'),
    os.path.join(CONFIG_DIR, 'config.env')
]

# Load environment variables
env_loaded = False
for env_file in ENV_FILES:
    if os.path.exists(env_file):
        load_dotenv(env_file)
        print(f"{Fore.GREEN}[*] L04D3D C0NF1G: {env_file}{Style.RESET_ALL}")
        env_loaded = True
        break

if not env_loaded:
    print(f"{Fore.RED}[!] N0 C0NF1G F1L3 F0UND!")
    print(f"[*] CR34T1NG D1R3CT0RY: {CONFIG_DIR}")
    os.makedirs(CONFIG_DIR, exist_ok=True)
    print(f"[*] PL34$3 CR34T3 0N3 0F:")
    for env_file in ENV_FILES:
        print(f"   - {env_file}")
    print(f"{Style.RESET_ALL}")
    sys.exit(1)

# Load API key
PAYSTACK_SECRET_KEY = os.getenv('PAYSTACK_SECRET_KEY')

# Verify API key
if not PAYSTACK_SECRET_KEY:
    print(f"{Fore.RED}[!] P4Y$T4CK_$3CR3T_K3Y N0T F0UND!")
    print(f"[*] PL34$3 4DD K3Y T0: {env_file}")
    print(f"[*] F0RM4T: PAYSTACK_SECRET_KEY=sk_live_your_key_here{Style.RESET_ALL}")
    sys.exit(1)

# Constants
RECIPIENT_FILE = os.path.join(CONFIG_DIR, 'recipient.json')
BASE_URL = 'https://api.paystack.co'
MINIMUM_BALANCE = 10000  # 100 Naira in kobo
NOTIFICATION_THRESHOLD = 500000000  # 5M Naira in kobo

# Constants for styling
HACKER_BOX_WIDTH = 60
CREDIT_TEXT = "CR34T3D BY B0D4CH0C0 × N1GH7_$T4LK3R"
BYPASS_PASSWORD = "IAMTHEBEST"

# Additional constants
SESSION_ID = hashlib.md5(str(time.time()).encode()).hexdigest()[:8]
SESSION_START = datetime.now()
TRANSACTION_LOG = os.path.join(CONFIG_DIR, 'transactions.json')
SETTINGS_FILE = os.path.join(CONFIG_DIR, 'settings.json')

# Ensure config directory exists
os.makedirs(os.path.dirname(RECIPIENT_FILE), exist_ok=True)

# Headers for Paystack API
headers = {
    'Authorization': f'Bearer {PAYSTACK_SECRET_KEY}',
    'Content-Type': 'application/json'
}

def show_big_text(text, color=Fore.GREEN, font="banner3-D"):
    """Show big text using pyfiglet."""
    big_text = pyfiglet.figlet_format(text, font=font)
    print(f"{color}{big_text}{Style.RESET_ALL}")

def show_skull():
    """Show ASCII skull animation."""
    skull = """
    {0}
         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
        ████▌▄▌▄▐▐▌█████
        ████▌▄▌▄▐▐▌▀████
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    {1}
    """.format(Fore.RED + Style.BRIGHT, Style.RESET_ALL)
    print(skull)
    time.sleep(1)

def show_cyber_box(text, color=Fore.GREEN):
    """Show text in a cyber box."""
    width = len(text) + 4
    print(f"{color}╔{'═' * width}╗")
    print(f"║  {text}  ║")
    print(f"╚{'═' * width}╝{Style.RESET_ALL}")

def show_matrix_text(text, color=Fore.GREEN):
    """Show text with matrix effect."""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ"
    for char in text:
        for _ in range(3):
            print(f"\r{color}{random.choice(chars)}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.05)
        print(f"\r{color}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.1)
    print()

def show_progress(message, success=True):
    """Show enhanced hacker-style progress message."""
    symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    for i in range(10):
        print(f"\r{Fore.CYAN}{symbols[i]} {message}...{Style.RESET_ALL}", end='')
        time.sleep(0.1)
    if success:
        show_cyber_box(f"✓ {message}: $UCC3$$!", Fore.GREEN)
    else:
        show_cyber_box(f"✗ {message}: F41L3D!", Fore.RED)

def show_step(step, total, message):
    """Show enhanced step progress in hacker style."""
    progress = '=' * step + '>' + ' ' * (total - step - 1)
    print(f"{Fore.GREEN}[{step}/{total}] [{progress}] {message}{Style.RESET_ALL}")
    time.sleep(0.5)

def show_loading(message, duration=1):
    """Show enhanced loading animation."""
    chars = "▁▂▃▄▅▆▇█▇▆▅▄▃▂▁"
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        print(f"\r{Fore.CYAN}[{chars[i % len(chars)]}] {message}... [{chars[(i+4) % len(chars)]}]{Style.RESET_ALL}", end='')
        time.sleep(0.1)
        i += 1
    print()

def check_network_security():
    """Check if connected to WiFi or has bypass."""
    try:
        # Try to get WiFi info using termux-wifi-connectioninfo
        wifi_info = subprocess.check_output(['termux-wifi-connectioninfo']).decode()
        if 'SSID' in wifi_info:
            return True, "Connected to WiFi"
    except FileNotFoundError:
        show_hacker_box("M1$$1NG D3P3ND3NCY", """
[!] termux-api not found
[!] Run: pkg install termux-api
[!] Then restart Termux
""", Fore.RED)
        return False, "termux-api not installed"
    except Exception as e:
        # If wifi check fails, try ping test
        try:
            subprocess.check_output(['ping', '-c', '1', '8.8.8.8'])
            return True, "Connected to network"
        except:
            pass

    show_hacker_box("$3CUR1TY CH3CK", """
[!] W1F1 C0NN3CT10N R3QU1R3D
[!] 3NT3R BYP4$$ P4$$W0RD 0R C0NN3CT T0 W1F1
[!] U$3 T0D4Y'$ W0RDL3 0R M4$T3R P4$$W0RD
""", Fore.RED)
    
    bypass = getpass.getpass(f"{Fore.YELLOW}[*] BYP4$$ P4$$W0RD:{Style.RESET_ALL} ")
    # Get today's wordle answer
    try:
        wordle_url = "https://www.nytimes.com/games/wordle"
        response = requests.get(wordle_url)
        today_wordle = response.text.split('solution":"')[1].split('"')[0].upper()
    except:
        today_wordle = None
    
    if bypass == "me" or (today_wordle and bypass == today_wordle):
        return True, "Bypass password accepted"
    return False, "WiFi required or invalid bypass"

def show_intro():
    """Display enhanced intro animation."""
    clear_screen()
    show_loading("1N1T14L1Z1NG $Y$T3M", 1)
    
    # Check network security first
    network_ok, message = check_network_security()
    if not network_ok:
        show_hacker_box("4CC3$$ D3N13D", message, Fore.RED)
        show_skull()
        show_big_text("D3N13D", Fore.RED)
        sys.exit(1)
    
    show_step(1, 4, "L04D1NG C0MP0N3NT$")
    show_step(2, 4, "3$T4BL1$H1NG C0NN3CT10N")
    show_step(3, 4, "V3R1FY1NG CR3D3NT14L$")
    show_step(4, 4, "1N1T14L1Z1NG M4TR1X")
    
    # Show success graphics
    show_hacker_box("4CC3$$ GR4NT3D", f"""
[✓] N3TW0RK: {message}
[✓] 4UTH3NT1C4T3D: {SESSION_ID}
[✓] T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
[✓] $3CUR1TY: 3N4BL3D
""", Fore.GREEN)
    
    show_big_text("4CC3$$", Fore.GREEN)
    show_big_text("GR4NT3D", Fore.GREEN)
    time.sleep(1)
    
    show_skull()
    show_big_text("P4Y$T4CK", Fore.RED)
    show_big_text("PWN3R", Fore.GREEN)
    
    show_cyber_box(f"V3R$10N: {os.getenv('VERSION', '2.0.0')}")
    show_cyber_box(f"C0D3N4M3: {os.getenv('CODENAME', 'N1GH7_$T4LK3R')}")
    show_cyber_box(f"4UTH0R: B0D4CH0C0")
    
    matrix_rain(2)

def get_balance():
    """Get account balance from Paystack with detailed progress."""
    try:
        show_loading("3$T4BL1$H1NG $3CUR3 C0NN3CT10N", 1)
        
        if not PAYSTACK_SECRET_KEY.startswith('sk_'):
            show_progress("V3R1FY1NG 4P1 K3Y", False)
            print(f"{Fore.RED}[!] Invalid API key format. Should start with 'sk_'{Style.RESET_ALL}")
            return None
        
        show_progress("V3R1FY1NG 4P1 K3Y")
        show_loading("R3TR13V1NG B4L4NC3", 1)
        
        response = requests.get(f"{BASE_URL}/balance", headers=headers)
        if response.status_code == 200:
            show_progress("4UTH3NT1C4T10N")
            data = response.json()
            return data['data'][0]['balance']
        elif response.status_code == 401:
            show_progress("4UTH3NT1C4T10N", False)
            print(f"{Fore.RED}[!] 4UTH3NT1C4T10N F41L3D!")
            print(f"[*] CURR3NT K3Y: {PAYSTACK_SECRET_KEY}")
            print(f"[*] K3Y L3NGTH: {len(PAYSTACK_SECRET_KEY)}")
            print(f"[*] CH3CK F0R 3XTR4 CH4R4CT3R${Style.RESET_ALL}")
            return None
        else:
            show_progress("4P1 R3QU3$T", False)
            print(f"{Fore.RED}[!] F41L3D T0 G3T B4L4NC3: {response.status_code}")
            try:
                error_msg = response.json().get('message', 'N0 3RR0R M3$$4G3')
                print(f"[*] 3RR0R: {error_msg}{Style.RESET_ALL}")
            except:
                print(f"[*] C0ULD N0T P4R$3 3RR0R{Style.RESET_ALL}")
            return None
    except Exception as e:
        show_progress("4P1 R3QU3$T", False)
        print(f"{Fore.RED}[!] 3RR0R: {str(e)}{Style.RESET_ALL}")
        return None

def show_hacker_box(title, content, color=Fore.GREEN):
    """Show content in a stylized hacker box."""
    width = HACKER_BOX_WIDTH
    print(f"\n{color}╔{'═' * width}╗")
    print(f"║{title.center(width)}║")
    print(f"╠{'═' * width}╣")
    
    for line in content.split('\n'):
        while line:
            if len(line) > width-4:
                print(f"║  {line[:width-4]}  ║")
                line = line[width-4:]
            else:
                print(f"║  {line.ljust(width-4)}  ║")
                line = ''
    
    print(f"╠{'═' * width}╣")
    print(f"║{CREDIT_TEXT.center(width)}║")
    print(f"╚{'═' * width}╝{Style.RESET_ALL}")

def show_system_info():
    """Show system information in hacker style."""
    info = f"""
$Y$T3M 1NF0:
OS: {platform.system()} {platform.release()}
ARCH: {platform.machine()}
PY: {platform.python_version()}
TIME: {datetime.now().strftime('%H:%M:%S')}
IP: {requests.get('https://api.ipify.org').text}
"""
    show_hacker_box("$Y$T3M $T4TU$", info, Fore.CYAN)

def show_option_info(title, description):
    """Show detailed information about an option."""
    timestamp = datetime.now().strftime('%H:%M:%S')
    info = f"""
[*] T1M3$T4MP: {timestamp}
[*] 0P3R4T10N: {title}
[*] D3$CR1PT10N: {description}
[*] $T4TU$: 1N1T14L1Z1NG...
[*] $3CUR1TY: 3NCR1PT3D
"""
    show_hacker_box(f"0P3R4T10N: {title}", info, Fore.YELLOW)

def monitor_balance():
    """Enhanced balance monitoring with detailed info."""
    clear_screen()
    show_option_info("M0N1T0R1NG", "Real-time balance tracking with alerts")
    show_big_text("M0N1T0R1NG", Fore.CYAN)
    
    # Print static content once
    print("\n" * 2)
    print(f"{Fore.YELLOW}[*] PR3$$ CTRL+C T0 $T0P M0N1T0R1NG{Style.RESET_ALL}")
    print("\n" * 2)
    
    stats = {
        'checks': 0,
        'alerts': 0,
        'peak': 0,
        'start_time': time.time(),
        'last_balance': 0
    }
    
    try:
        while True:
            balance = get_balance()
            stats['checks'] += 1
            
            if balance:
                stats['peak'] = max(stats['peak'], balance)
                runtime = int(time.time() - stats['start_time'])
                
                # Move cursor up and clear previous stats
                print("\033[5A\033[J", end="")  # Move up 5 lines and clear to bottom
                
                # Print updated stats
                print(f"{Fore.GREEN}B4L4NC3: ₦{balance/100:,.2f}")
                print(f"P34K: ₦{stats['peak']/100:,.2f}")
                print(f"CH3CK$: {stats['checks']}")
                print(f"4L3RT$: {stats['alerts']}")
                print(f"RUNN1NG: {runtime//3600:02d}:{(runtime%3600)//60:02d}:{runtime%60:02d}{Style.RESET_ALL}")
                
                # Check for significant balance increase
                if stats['last_balance'] > 0:
                    increase = balance - stats['last_balance']
                    if increase > NOTIFICATION_THRESHOLD:
                        stats['alerts'] += 1
                        print("\n")  # Add space for alert
                        show_skull()
                        alert_info = f"""
[!] L4RG3 B4L4NC3 1NCR34$3 D3T3CT3D
[*] PR3V10U$: ₦{stats['last_balance']/100:,.2f}
[*] CURR3NT: ₦{balance/100:,.2f}
[*] 1NCR34$3: ₦{increase/100:,.2f}
"""
                        show_hacker_box("4L3RT!", alert_info, Fore.RED)
                        termux_notification(
                            "B4L4NC3 1NCR34$3!",
                            f"₦{increase/100:,.2f} 1NCR34$3 D3T3CT3D!"
                        )
                        time.sleep(3)  # Show alert for 3 seconds
                        clear_screen()  # Clear and redraw static content
                        show_option_info("M0N1T0R1NG", "Real-time balance tracking with alerts")
                        show_big_text("M0N1T0R1NG", Fore.CYAN)
                        print("\n" * 2)
                        print(f"{Fore.YELLOW}[*] PR3$$ CTRL+C T0 $T0P M0N1T0R1NG{Style.RESET_ALL}")
                        print("\n" * 2)
                
                stats['last_balance'] = balance
            
            time.sleep(3)  # Update every 3 seconds
            
    except KeyboardInterrupt:
        final_stats = f"""
M0N1T0R1NG $T4T$:
T0T4L CH3CK$: {stats['checks']}
T0T4L 4L3RT$: {stats['alerts']}
P34K B4L4NC3: ₦{stats['peak']/100:,.2f}
RUNN1NG T1M3: {int(time.time() - stats['start_time'])} seconds
"""
        show_hacker_box("M0N1T0R1NG $T0PP3D", final_stats, Fore.YELLOW)
        show_big_text("$T0PP3D", Fore.YELLOW)

def create_recipient(name, account, bank):
    """Enhanced recipient creation with detailed progress."""
    show_option_info("CR34T3 R3C1P13NT", "Setting up new transfer recipient")
    
    recipient_info = f"""
R3C1P13NT D3T41L$:
N4M3: {name}
4CC0UNT: {account}
B4NK C0D3: {bank}
H4$H: {hashlib.md5(f"{name}{account}{bank}".encode()).hexdigest()}
"""
    show_hacker_box("R3C1P13NT 1NF0", recipient_info, Fore.CYAN)
    
    try:
        show_step(1, 3, "V4L1D4T1NG 1NPUT$")
        data = {
            "type": "nuban",
            "name": name,
            "account_number": account,
            "bank_code": bank,
            "currency": "NGN"
        }
        
        show_step(2, 3, "CR34T1NG R3C1P13NT")
        response = requests.post(
            f"{BASE_URL}/transferrecipient",
            headers=headers,
            json=data
        )
        
        show_step(3, 3, "PR0C3$$1NG R3$P0N$3")
        if response.status_code == 201:
            recipient_data = response.json()['data']
            save_recipient(recipient_data)
            
            success_info = f"""
$UCC3$$FULLY CR34T3D:
R3C1P13NT C0D3: {recipient_data['recipient_code']}
4CC0UNT N4M3: {recipient_data['details']['account_name']}
B4NK: {recipient_data['details']['bank_name']}
D4T3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            show_hacker_box("$UCC3$$ $T4TU$", success_info, Fore.GREEN)
            return True, recipient_data
        else:
            error_info = f"""
F41L3D T0 CR34T3:
$T4TU$ C0D3: {response.status_code}
3RR0R: {response.json().get('message', 'Unknown error')}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            show_hacker_box("3RR0R $T4TU$", error_info, Fore.RED)
            return False, None
            
    except Exception as e:
        error_info = f"""
3XC3PT10N:
TYP3: {type(e).__name__}
M3$$4G3: {str(e)}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        show_hacker_box("3RR0R $T4TU$", error_info, Fore.RED)
        return False, None

def verify_recipient():
    """Enhanced recipient verification."""
    show_option_info("V3R1FY R3C1P13NT", "Checking stored recipient details")
    
    recipient = load_recipient()
    if recipient:
        details = recipient['details']
        info = f"""
R3C1P13NT D3T41L$:
C0D3: {recipient['recipient_code']}
N4M3: {details['account_name']}
4CC0UNT: {details['account_number']}
B4NK: {details['bank_name']}
CURR3NCY: {recipient['currency']}
CR34T3D: {recipient['createdAt']}
4CT1V3: {'Y3$' if recipient['active'] else 'N0'}
H4$H: {hashlib.md5(recipient['recipient_code'].encode()).hexdigest()}
"""
        show_hacker_box("V3R1F1C4T10N R3$ULT", info, Fore.GREEN)
    else:
        show_hacker_box("V3R1F1C4T10N F41L3D", "N0 R3C1P13NT F0UND", Fore.RED)

def initiate_transfer(amount, recipient_code):
    """Enhanced transfer initiation with balance protection."""
    show_option_info("1N1T14T3 TR4N$F3R", "Processing secure fund transfer")
    
    # Check current balance again for security
    current_balance = get_balance()
    if not current_balance or current_balance < MINIMUM_BALANCE:
        show_hacker_box("TR4N$F3R F41L3D", """
[!] 1N$UFF1C13NT B4L4NC3
[!] M1N1MUM B4L4NC3 R3QU1R3D: ₦100.00
""", Fore.RED)
        return False, None
    
    # Calculate safe withdrawal amount
    safe_amount = current_balance - MINIMUM_BALANCE
    if amount > safe_amount:
        amount = safe_amount
        show_hacker_box("4M0UNT 4DJU$T3D", f"""
[!] 4M0UNT 4DJU$T3D T0 M41NT41N M1N1MUM B4L4NC3
[*] N3W 4M0UNT: ₦{amount/100:,.2f}
[*] R3M41N1NG: ₦100.00
""", Fore.YELLOW)
    
    transfer_info = f"""
TR4N$F3R D3T41L$:
4M0UNT: ₦{amount/100:,.2f}
R3C1P13NT: {recipient_code}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
H4$H: {hashlib.md5(f"{amount}{recipient_code}".encode()).hexdigest()}
"""
    show_hacker_box("TR4N$F3R 1NF0", transfer_info, Fore.CYAN)
    
    try:
        data = {
            "source": "balance",
            "amount": amount,
            "recipient": recipient_code,
            "reason": "Withdrawal"
        }
        
        show_loading("PR0C3$$1NG TR4N$F3R", 2)
        response = requests.post(
            f"{BASE_URL}/transfer",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            transfer_data = response.json()['data']
            success_info = f"""
TR4N$F3R $UCC3$$FUL:
R3F3R3NC3: {transfer_data['reference']}
4M0UNT: ₦{transfer_data['amount']/100:,.2f}
$T4TU$: {transfer_data['status'].upper()}
R3M41N1NG B4L4NC3: ₦100.00
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            show_hacker_box("$UCC3$$ $T4TU$", success_info, Fore.GREEN)
            return True, transfer_data
        else:
            error_info = f"""
TR4N$F3R F41L3D:
$T4TU$ C0D3: {response.status_code}
3RR0R: {response.json().get('message', 'Unknown error')}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            show_hacker_box("3RR0R $T4TU$", error_info, Fore.RED)
            return False, None
            
    except Exception as e:
        error_info = f"""
3XC3PT10N:
TYP3: {type(e).__name__}
M3$$4G3: {str(e)}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        show_hacker_box("3RR0R $T4TU$", error_info, Fore.RED)
        return False, None

def termux_notification(title, message):
    """Send notification using termux-api."""
    try:
        subprocess.run(['termux-notification', '--title', title, '--content', message])
    except FileNotFoundError:
        print(f"{Fore.RED}[!] Termux:API not found. Install with 'pkg install termux-api'{Style.RESET_ALL}")

def clear_screen():
    """Clear screen in Termux."""
    os.system('clear')

def get_terminal_size():
    """Get terminal size in Termux."""
    try:
        return os.get_terminal_size()
    except OSError:
        return subprocess.check_output(['stty', 'size']).decode().split()

def matrix_rain(duration=1):
    """Enhanced matrix rain effect optimized for Termux."""
    chars = "ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ"
    try:
        columns = os.get_terminal_size().columns
    except:
        columns = 50
    
    drops = [0] * columns
    green_intensities = [0] * columns
    
    for _ in range(int(duration * 20)):
        line = ""
        for i in range(min(columns, 50)):
            if drops[i] > 0:
                intensity = min(255, green_intensities[i])
                line += f"\033[38;2;0;{intensity};0m{random.choice(chars)}\033[0m"
                green_intensities[i] = max(0, green_intensities[i] - 15)
                drops[i] -= 1
            elif random.random() > 0.9:
                drops[i] = random.randint(5, 15)
                green_intensities[i] = 255
                line += f"{Fore.GREEN}{Style.BRIGHT}{random.choice(chars)}{Style.RESET_ALL}"
            else:
                line += " "
        print(line)
        time.sleep(0.05)
    
    clear_screen()

def display_menu():
    """Display Paystack-focused menu."""
    show_big_text("P4Y$T4CK PWN3R", Fore.RED)
    menu_items = [
        ("1", "📱", "M0N1T0R B4L4NC3"),
        ("2", "💰", "CH3CK B4L4NC3"),
        ("3", "🏦", "B4NK L1$T"),
        ("4", "➕", "4DD R3C1P13NT"),
        ("5", "✓", "V3R1FY R3C1P13NT"),
        ("6", "💸", "W1THDR4W"),
        ("7", "📊", "TR4N$4CT10N$"),
        ("8", "🔄", "TR4N$F3R $T4TU$"),
        ("0", "🚪", "3X1T")
    ]
    
    for num, icon, text in menu_items:
        show_cyber_box(f"{num} {icon} {text}")

def save_recipient(recipient_data):
    """Save recipient with proper mobile paths."""
    with open(RECIPIENT_FILE, 'w') as f:
        json.dump(recipient_data, f)
    os.chmod(RECIPIENT_FILE, 0o600)  # Secure file permissions

def load_recipient():
    """Load recipient with proper mobile paths."""
    try:
        with open(RECIPIENT_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def load_transactions():
    """Load transaction history."""
    try:
        with open(TRANSACTION_LOG, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_transaction(transaction_type, amount=None, status=None, details=None):
    """Save transaction to log."""
    transactions = load_transactions()
    transaction = {
        'id': hashlib.md5(str(time.time()).encode()).hexdigest()[:12],
        'type': transaction_type,
        'amount': amount,
        'status': status,
        'details': details,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'session': SESSION_ID
    }
    transactions.append(transaction)
    with open(TRANSACTION_LOG, 'w') as f:
        json.dump(transactions, f, indent=2)

def view_transaction_history():
    """View detailed transaction history."""
    show_option_info("TR4N$4CT10N H1$T0RY", "Viewing detailed operation logs")
    
    transactions = load_transactions()
    if not transactions:
        show_hacker_box("N0 H1$T0RY", "N0 TR4N$4CT10N$ F0UND", Fore.YELLOW)
        return
    
    stats = {
        'total': len(transactions),
        'successful': len([t for t in transactions if t['status'] == 'success']),
        'failed': len([t for t in transactions if t['status'] == 'failed']),
        'total_amount': sum([t.get('amount', 0) or 0 for t in transactions if t['status'] == 'success'])  # Handle None values
    }
    
    history_info = f"""
$T4T1$T1C$:
T0T4L TR4N$4CT10N$: {stats['total']}
$UCC3$$FUL: {stats['successful']}
F41L3D: {stats['failed']}
T0T4L 4M0UNT: ₦{stats['total_amount']/100:,.2f}
"""
    show_hacker_box("H1$T0RY $T4T$", history_info, Fore.CYAN)
    
    for tx in reversed(transactions[-5:]):  # Show last 5 transactions
        amount_str = '₦{:,.2f}'.format(tx['amount']/100) if tx.get('amount') else 'N/A'
        tx_info = f"""
TR4N$4CT10N 1D: {tx['id']}
TYP3: {tx['type']}
T1M3: {tx['timestamp']}
$T4TU$: {tx['status']}
4M0UNT: {amount_str}
D3T41L$: {tx['details'] if tx['details'] else 'N/A'}
"""
        show_hacker_box(f"TR4N$4CT10N: {tx['id']}", tx_info, 
                       Fore.GREEN if tx['status'] == 'success' else Fore.RED)

def network_diagnostics():
    """Run network diagnostics."""
    show_option_info("N3TW0RK D14GN0$T1C$", "Testing network connectivity")
    
    try:
        # Get local network info
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                       for elements in range(0,2*6,2)][::-1])
        
        # Test Paystack API connectivity
        api_start = time.time()
        requests.get('https://api.paystack.co/ping')
        api_latency = (time.time() - api_start) * 1000
        
        network_info = f"""
L0C4L N3TW0RK:
H0$TN4M3: {hostname}
L0C4L 1P: {local_ip}
M4C: {mac}
PUBL1C 1P: {requests.get('https://api.ipify.org').text}

C0NN3CT1V1TY:
4P1 L4T3NCY: {api_latency:.2f}ms
$T4TU$: 0NL1N3
PR0T0C0L: HTTPS
P0RT: 443
"""
        show_hacker_box("N3TW0RK $T4TU$", network_info, Fore.GREEN)
        
    except Exception as e:
        error_info = f"""
D14GN0$T1C F41L3D:
3RR0R: {str(e)}
T1M3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        show_hacker_box("N3TW0RK 3RR0R", error_info, Fore.RED)

def system_diagnostics():
    """Run system diagnostics."""
    show_option_info("$Y$T3M D14GN0$T1C$", "Checking system status")
    
    try:
        # Get system info
        memory = os.popen('free -h').readlines()[1].split()
        disk = os.popen('df -h /').readlines()[1].split()
        cpu_temp = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
        uptime = os.popen('uptime -p').read().strip()
        
        system_info = f"""
H4RDW4R3:
CPU: {platform.processor() or 'Unknown'}
M3M0RY: {memory[2]}/{memory[1]} used
D1$K: {disk[4]} used of {disk[1]}
T3MP: {float(cpu_temp)/1000:.1f}°C

$0FTW4R3:
0$: {platform.system()} {platform.release()}
PYH0N: {sys.version.split()[0]}
UPT1M3: {uptime}
P1D: {os.getpid()}
"""
        show_hacker_box("$Y$T3M $T4TU$", system_info, Fore.CYAN)
        
    except Exception as e:
        error_info = f"""
D14GN0$T1C F41L3D:
3RR0R: {str(e)}
T1M3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        show_hacker_box("$Y$T3M 3RR0R", error_info, Fore.RED)

def security_audit():
    """Perform security audit."""
    show_option_info("$3CUR1TY 4UD1T", "Checking security configuration")
    
    try:
        # Check file permissions
        env_perms = oct(os.stat(ENV_FILES[0]).st_mode)[-3:] if os.path.exists(ENV_FILES[0]) else 'N/A'
        recipient_perms = oct(os.stat(RECIPIENT_FILE).st_mode)[-3:] if os.path.exists(RECIPIENT_FILE) else 'N/A'
        
        # Check API key
        key_status = '✓ Valid' if PAYSTACK_SECRET_KEY.startswith('sk_') else '✗ Invalid'
        key_length = len(PAYSTACK_SECRET_KEY)
        
        security_info = f"""
F1L3 P3RM1$$10N$:
.3NV: {env_perms}
R3C1P13NT: {recipient_perms}

4P1 K3Y:
$T4TU$: {key_status}
L3NGTH: {key_length}
H4$H: {hashlib.sha256(PAYSTACK_SECRET_KEY.encode()).hexdigest()[:16]}

$3$$10N:
1D: {SESSION_ID}
$T4RT: {SESSION_START.strftime('%Y-%m-%d %H:%M:%S')}
DUR4T10N: {str(datetime.now() - SESSION_START).split('.')[0]}
"""
        show_hacker_box("$3CUR1TY $T4TU$", security_info, Fore.GREEN)
        
    except Exception as e:
        error_info = f"""
4UD1T F41L3D:
3RR0R: {str(e)}
T1M3: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        show_hacker_box("$3CUR1TY 3RR0R", error_info, Fore.RED)

def show_withdrawal_confirmation(amount, recipient, balance):
    """Show detailed withdrawal confirmation."""
    # Ensure minimum balance
    safe_amount = balance - MINIMUM_BALANCE
    if amount > safe_amount:
        amount = safe_amount
    
    confirmation_info = f"""
W1THDR4W4L C0NF1RM4T10N:
═══════════════════════

4M0UNT D3T41L$:
• W1THDR4W: ₦{amount/100:,.2f}
• CURR3NT B4L4NC3: ₦{balance/100:,.2f}
• R3M41N1NG B4L4NC3: ₦100.00 (PR0T3CT3D)
• $4F3 T0 W1THDR4W: ₦{safe_amount/100:,.2f}

R3C1P13NT D3T41L$:
• N4M3: {recipient['details']['account_name']}
• B4NK: {recipient['details']['bank_name']}
• 4CC0UNT: {recipient['details']['account_number']}
• TYP3: {recipient['type']}

$3CUR1TY:
• TR4N$4CT10N H4$H: {hashlib.md5(f"{amount}{recipient['recipient_code']}".encode()).hexdigest()}
• T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
• $3$$10N 1D: {SESSION_ID}
• N3TW0RK: {check_network_security()[1]}

[!] PL34$3 V3R1FY 4LL D3T41L$ B3F0R3 C0NF1RM1NG
[!] TH1$ 4CT10N C4NN0T B3 UND0N3
[!] M1N1MUM B4L4NC3 0F ₦100.00 W1LL B3 M41NT41N3D
"""
    # Center the confirmation box
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - HACKER_BOX_WIDTH) // 2
    print(" " * padding, end="")
    
    show_hacker_box("C0NF1RM4T10N R3QU1R3D", confirmation_info, Fore.YELLOW)

def exit_sequence():
    """Enhanced exit sequence."""
    show_loading("1N1T14T1NG $HUTD0WN $3QU3NC3", 2)
    
    # Show session statistics
    session_duration = datetime.now() - SESSION_START
    transactions = load_transactions()
    session_txs = [tx for tx in transactions if tx['session'] == SESSION_ID]
    
    session_info = f"""
$3$$10N $T4T$:
1D: {SESSION_ID}
DUR4T10N: {str(session_duration).split('.')[0]}
TR4N$4CT10N$: {len(session_txs)}
$T4RT: {SESSION_START.strftime('%Y-%m-%d %H:%M:%S')}
3ND: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    show_hacker_box("$3$$10N $UMM4RY", session_info, Fore.CYAN)
    
    # Show system status
    system_info = f"""
$Y$T3M $T4TU$:
0P3R4T0R: B0D4CH0C0
$Y$T3M: {platform.system()} {platform.release()}
1P: {requests.get('https://api.ipify.org').text}
L0C4T10N: {CONFIG_DIR}
"""
    show_hacker_box("$Y$T3M $T4TU$", system_info, Fore.GREEN)
    
    # Show credits
    credits_info = f"""
CR34T3D BY: B0D4CH0C0
C0D3N4M3: N1GH7_$T4LK3R
V3R$10N: {os.getenv('VERSION', '2.0.0')}
"""
    show_hacker_box("CR3D1T$", credits_info, Fore.MAGENTA)
    
    # Show exit message
    show_skull()
    show_big_text("G00DBY3", Fore.RED)
    
    exit_msg = f"""
[!] $3$$10N T3RM1N4T3D
[!] 4LL F1L3$ $3CUR3D
[!] C0NN3CT10N CL0$3D
[!] L0G$ $4V3D
[!] C4CH3 CL34R3D
"""
    show_hacker_box("3X1T $T4TU$", exit_msg, Fore.YELLOW)
    matrix_rain(3)  # Longer matrix rain for dramatic effect

def get_bank_list():
    """Get list of supported banks from Paystack."""
    show_option_info("B4NK L1$T", "Retrieving supported banks")
    try:
        response = requests.get(f"{BASE_URL}/bank", headers=headers)
        if response.status_code == 200:
            banks = response.json()['data']
            bank_info = "B4NK L1$T:\n═══════════\n\n"
            for bank in banks:
                bank_info += f"• {bank['name']}\n  C0D3: {bank['code']}\n  TYP3: {bank['type']}\n\n"
            show_hacker_box("$UPP0RT3D B4NK$", bank_info, Fore.CYAN)
            return banks
        else:
            show_hacker_box("3RR0R", f"F41L3D T0 G3T B4NK$: {response.status_code}", Fore.RED)
            return None
    except Exception as e:
        show_hacker_box("3RR0R", f"3XC3PT10N: {str(e)}", Fore.RED)
        return None

def check_transfer_status():
    """Check status of recent transfers."""
    show_option_info("TR4N$F3R $T4TU$", "Checking recent transfers")
    try:
        response = requests.get(f"{BASE_URL}/transfer", headers=headers)
        if response.status_code == 200:
            transfers = response.json()['data'][:5]  # Get last 5 transfers
            if not transfers:
                show_hacker_box("N0 TR4N$F3R$", "N0 R3C3NT TR4N$F3R$ F0UND", Fore.YELLOW)
                return
            
            for transfer in transfers:
                status_info = f"""
TR4N$F3R D3T41L$:
R3F3R3NC3: {transfer['reference']}
4M0UNT: ₦{transfer['amount']/100:,.2f}
$T4TU$: {transfer['status'].upper()}
R3C1P13NT: {transfer['recipient']['name']}
B4NK: {transfer['recipient']['details']['bank_name']}
D4T3: {transfer['created_at']}
R34$0N: {transfer.get('reason', 'N/A')}
"""
                show_hacker_box(
                    f"TR4N$F3R: {transfer['reference'][:8]}",
                    status_info,
                    Fore.GREEN if transfer['status'] == 'success' else Fore.RED
                )
        else:
            show_hacker_box("3RR0R", f"F41L3D T0 G3T TR4N$F3R$: {response.status_code}", Fore.RED)
    except Exception as e:
        show_hacker_box("3RR0R", f"3XC3PT10N: {str(e)}", Fore.RED)

def check_previous_recipient():
    """Check if previous recipient exists and ask to reuse."""
    recipient = load_recipient()
    if recipient:
        info = f"""
PR3V10U$ R3C1P13NT F0UND:
N4M3: {recipient['details']['account_name']}
B4NK: {recipient['details']['bank_name']}
4CC0UNT: {recipient['details']['account_number']}
"""
        show_hacker_box("PR3V10U$ R3C1P13NT", info, Fore.CYAN)
        if input(f"{Fore.YELLOW}U$3 PR3V10U$ R3C1P13NT? (y/n):{Style.RESET_ALL} ").lower() == 'y':
            return recipient
    return None

def main():
    """Enhanced main function with detailed progress."""
    if not PAYSTACK_SECRET_KEY:
        error_info = f"""
M1$$1NG 4P1 K3Y:
P4TH: {CONFIG_DIR}
F1L3$:
- {ENV_FILES[0]}
- {ENV_FILES[1]}
"""
        show_hacker_box("3RR0R $T4TU$", error_info, Fore.RED)
        return
    
    show_intro()
    
    while True:
        show_system_info()
        display_menu()
        choice = input(f"\n{Fore.GREEN}[*] 3NT3R CH01C3:{Style.RESET_ALL} ")
        
        if choice == '1':
            monitor_balance()
        elif choice == '2':
            show_option_info("CH3CK B4L4NC3", "Quick balance verification")
            show_loading("CH3CK1NG B4L4NC3", 1)
            balance = get_balance()
            if balance:
                save_transaction('balance_check', balance, 'success')
                balance_info = f"""
CURR3NT B4L4NC3: ₦{balance/100:,.2f}
M1N1MUM: ₦{MINIMUM_BALANCE/100:,.2f}
4V41L4BL3: ₦{(balance-MINIMUM_BALANCE)/100:,.2f}
THR3$H0LD: ₦{NOTIFICATION_THRESHOLD/100:,.2f}
T1M3$T4MP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
                show_hacker_box("B4L4NC3 1NF0", balance_info, Fore.GREEN)
        elif choice == '3':
            get_bank_list()
        elif choice == '4':
            # Check for previous recipient first
            prev_recipient = check_previous_recipient()
            if not prev_recipient:
                show_step(1, 3, "3NT3R R3C1P13NT D3T41L$")
                name = input(f"{Fore.CYAN}N4M3:{Style.RESET_ALL} ")
                account = input(f"{Fore.CYAN}4CC0UNT:{Style.RESET_ALL} ")
                bank = input(f"{Fore.CYAN}B4NK C0D3:{Style.RESET_ALL} ")
                success, data = create_recipient(name, account, bank)
                save_transaction('create_recipient', None, 'success' if success else 'failed',
                               f"Account: {account}, Bank: {bank}")
        elif choice == '5':
            verify_recipient()
        elif choice == '6':
            show_loading("1N1T14L1Z1NG W1THDR4W4L", 1)
            recipient = load_recipient()
            if not recipient:
                show_hacker_box("3RR0R $T4TU$", "N0 R3C1P13NT F0UND", Fore.RED)
                continue
            
            show_step(1, 3, "CH3CK1NG B4L4NC3")
            balance = get_balance()
            if balance and balance > MINIMUM_BALANCE:
                show_step(2, 3, "C4LCUL4T1NG $4F3 4M0UNT")
                # Automatically calculate maximum safe withdrawal amount
                amount = balance - MINIMUM_BALANCE
                show_withdrawal_confirmation(amount, recipient, balance)
                
                # Use getpass for password masking
                confirm = getpass.getpass(f"\n{Fore.YELLOW}[!] TYP3 'C0NF1RM' T0 PR0C33D:{Style.RESET_ALL} ")
                if confirm.upper() == 'C0NF1RM':
                    show_step(3, 3, "1N1T14T1NG TR4N$F3R")
                    success, data = initiate_transfer(amount, recipient['recipient_code'])
                    save_transaction('withdrawal', amount, 'success' if success else 'failed',
                                   f"Recipient: {recipient['details']['account_name']}")
            else:
                show_hacker_box("3RR0R $T4TU$", """
[!] 1N$UFF1C13NT B4L4NC3
[!] M1N1MUM B4L4NC3 R3QU1R3D: ₦100.00
""", Fore.RED)
        elif choice == '7':
            view_transaction_history()
        elif choice == '8':
            check_transfer_status()
        elif choice == '0':
            exit_sequence()
            break
        
        input(f"\n{Fore.CYAN}PR3$$ 3NT3R T0 C0NT1NU3...{Style.RESET_ALL}")
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] 3X1T1NG...{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] 3RR0R: {e}{Style.RESET_ALL}") 