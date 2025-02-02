# PayStack PWN3R

A cyberpunk-themed Paystack balance monitoring and management tool for Termux.


FOR THOSE WHO KNOW!

![Cyberpunk Theme](https://img.shields.io/badge/theme-cyberpunk-ff69b4)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 🚀 Real-time balance monitoring with alerts
- 💰 Automated balance tracking and notifications
- 🔔 Maximum alert settings with sound and vibration
- 🎨 Cyberpunk-themed UI with ASCII art
- 🔒 Secure API key management
- 📊 Transaction history tracking
- 🌐 Network connectivity testing
- 🏦 Bank verification system
- 💸 Secure withdrawal system
- 🎮 Easter eggs and fun animations

## Requirements

- Termux app installed
- Termux:API app installed
- Python 3.6 or higher
- Active internet connection
- Paystack API key

## Installation

1. Install required Termux packages:
```bash
pkg update && pkg upgrade
pkg install python git termux-api
```

2. Clone the repository:
```bash
git clone https://github.com/bodachoco/paystack-pwner.git
cd paystack-pwner
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Paystack API key:
```bash
mkdir -p ~/.paystack_pwner
echo "PAYSTACK_SECRET_KEY=your_secret_key" > ~/.paystack_pwner/.env
```

## Usage

1. Start the script:
```bash
python paystack_pwner_termux.py
```

2. Available options:
- 1️⃣ Monitor - Real-time balance monitoring
- 2️⃣ Balance - Quick balance check
- 3️⃣ Banks - List supported banks
- 4️⃣ Recipient - Add transfer recipient
- 5️⃣ Verify - Verify recipient details
- 6️⃣ Withdraw - Initiate withdrawal
- 7️⃣ History - View transaction history
- 8️⃣ Network - Test connectivity
- 9️⃣ Keys - Manage API keys
- T️ Test - Test notifications
- R Reload - Reload script
- 0️⃣ Exit - Exit program

## Security Features

- Secure API key storage
- File permission hardening
- Network security checks
- Transaction verification
- Session monitoring
- Secure exit sequence

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

⚠️ **IMPORTANT LEGAL DISCLAIMER** ⚠️

This tool is provided for EDUCATIONAL and AUTHORIZED TESTING purposes ONLY. By using this software, you agree:

1. To use it only on systems you own or have explicit permission to test
2. Not to use it for any malicious or illegal activities
3. Not to hold the creator(s) liable for any misuse or damage
4. To comply with all applicable laws and Paystack's terms of service

The developer (B0D4CH0C0) assumes NO responsibility for any misuse or damage caused by this program.
Remember: With great power comes great responsibility! 🦹‍♂️

## Credits

```ascii
╔══════════════════════════════════════════════════════════╗
║             P4Y$T4CK PWN3R CR3D1T$                       ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  ██████╗ ██╗    ██╗███╗   ██╗██████╗ ██████╗           ║
║  ██╔══██╗██║    ██║████╗  ██║██╔══██╗██╔══██╗          ║
║  ██████╔╝██║ █╗ ██║██╔██╗ ██║██████╔╝██████╔╝          ║
║  ██╔═══╝ ██║███╗██║██║╚██╗██║██╔══██╗██╔══██╗          ║
║  ██║     ╚███╔███╔╝██║ ╚████║██║  ██║██║  ██║          ║
║  ╚═╝      ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝          ║
║                                                          ║
║  CR34T3D BY: B0D4CH0C0                                  ║
║  C0D3N4M3: N1GH7_$T4LK3R                                ║
║  V3R$10N: 2.0.0                                         ║
║                                                          ║
║  Copyright © 2024 B0D4CH0C0. All rights reserved.       ║
╚══════════════════════════════════════════════════════════╝
```

## Support

If you like this project, please give it a ⭐!
