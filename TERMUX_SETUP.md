# T3RMUX $3TUP GU1D3

## 1. C0PY1NG F1L3$ T0 T3RMUX
```bash
# First, grant storage permission to Termux
termux-setup-storage

# Wait for permission prompt on your Android device and grant it
# This creates ~/storage/downloads link to your Downloads folder

# Create project directory
mkdir -p ~/paystack_pwner

# Copy from Downloads to Termux (Method 1 - Direct Copy)
cp ~/storage/downloads/paystack_pwner.zip ~/paystack_pwner/

# OR use this if the above doesn't work (Method 2 - Manual Location)
cp /storage/emulated/0/Download/paystack_pwner.zip ~/paystack_pwner/

# Go to project directory
cd ~/paystack_pwner

# Extract the zip
unzip paystack_pwner.zip

# Set proper permissions
chmod 700 .
chmod 600 .env
```

## 2. TR0UBL3$H00T1NG F1L3 4CC3$$

### 1F P3RM1$$10N D3N13D:
```bash
# Check if storage is properly setup
ls -l ~/storage/
# Should show links to your storage locations

# If not visible, try:
termux-setup-storage
# Grant permission when prompted
```

### 1F F1L3 N0T F0UND:
```bash
# List available storage locations
ls ~/storage/

# Check Downloads folder content
ls ~/storage/downloads/

# Or check direct path
ls /storage/emulated/0/Download/
```

### 1F Z1P F41L$ T0 3XTR4CT:
```bash
# Install unzip if not available
pkg install unzip

# Check zip file permissions
ls -l paystack_pwner.zip

# Try with verbose output
unzip -v paystack_pwner.zip
```

## 3. 4LT3RN4T1V3 M3TH0D$ (1F 4B0V3 F41L$)

### M3TH0D 1: U$3 T3RMUX F1L3 P1CK3R
```bash
# Install termux-tools
pkg install termux-tools

# Use file picker
termux-storage-get paystack_pwner.zip
```

### M3TH0D 2: U$3 CP W1TH F1ND
```bash
# Find and copy zip file
find /storage/emulated/0 -name "paystack_pwner.zip" -exec cp {} ~/paystack_pwner/ \;
```

### M3TH0D 3: U$3 T3RMUX $H4R3
```bash
# Share the zip file to Termux from your file manager
# It will be saved in ~/downloads/
mv ~/downloads/paystack_pwner.zip ~/paystack_pwner/
```

## 4. V3R1FY1NG $UCC3$$FUL C0PY

```bash
# Check if files are copied correctly
cd ~/paystack_pwner
ls -la

# Verify zip contents
unzip -l paystack_pwner.zip

# Check file permissions
ls -l .env
ls -l paystack_pwner_termux.py
```

## 5. CL34NUP (0PT10N4L)

```bash
# Remove zip after extraction
rm paystack_pwner.zip

# Secure sensitive files
chmod 600 .env
chmod 700 ~/paystack_pwner
```

## 1. 1N$T4LL T3RMUX
1. Download Termux from F-Droid (recommended) or GitHub
   - F-Droid: https://f-droid.org/en/packages/com.termux/
   - DO NOT use Google Play version (outdated)

## 2. B4$1C $3TUP
```bash
# Update package list
pkg update -y && pkg upgrade -y

# Install required packages
pkg install python git nano python-pip tsu -y

# Install Termux:API (for notifications)
pkg install termux-api -y

# Setup storage access
termux-setup-storage
```

## 3. 1N$T4LL F0NT$ (0PT10N4L BUT R3C0MM3ND3D)
```bash
# Install required tools
pkg install wget -y

# Download and install Nerd Font
mkdir -p ~/.termux/font/
wget -O ~/.termux/font/font.ttf https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/FiraCode/Regular/FiraCodeNerdFontMono-Regular.ttf

# Reload Termux
termux-reload-settings
```

## 4. $3T C0L0R $CH3M3
```bash
# Install color scheme
curl -fsSL https://raw.githubusercontent.com/4679/oh-my-termux/master/install.sh | bash
```

## 5. CL0N3 & $3TUP P4Y$T4CK PWN3R
```bash
# Install requirements
pip install -r requirements.txt

# Set execute permissions
chmod +x paystack_pwner.py
```

## 6. C0NF1GUR3 .3NV
```bash
# Edit .env file with your Paystack key
nano .env
```

## 7. RUN TH3 $CR1PT
```bash
# Execute the script
python paystack_pwner.py
```

## TR0UBL3$H00T1NG

### N0T1F1C4T10N$ N0T W0RK1NG
1. Make sure Termux:API is installed
2. Grant notification permissions
3. Run: `termux-notification-list` to test

### D1$PL4Y 1$$U3$
1. Try different font:
```bash
# Install another Nerd Font
wget -O ~/.termux/font/font.ttf https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Regular/HackNerdFontMono-Regular.ttf
termux-reload-settings
```

### P3RM1$$10N$ 1$$U3$
```bash
# Fix permissions
chmod 755 ~/paystack_pwner
chmod 644 ~/paystack_pwner/.env
```

## R3C0MM3ND3D T3RMUX $3TT1NG$

1. Open Termux
2. Long press screen > Style
3. Set:
   - Terminal Margin: 1
   - Font Size: 14
   - Terminal Bell: OFF
   - Vibrate: ON
   - Dark Theme: ON

## $3CUR1TY N0T3$

1. Keep your .env file secure
2. Don't share your Termux session
3. Use termux-lock for added security
4. Regularly update packages
5. Backup your configuration

## 4DD1T10N4L T1P$

1. Use volume down + Q for extra keyboard keys
2. Swipe screen for quick access to sidebar
3. Use termux-wake-lock to keep script running
4. Install termux-services for background operation
5. Use tmux for better session management 