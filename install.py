#!/usr/bin/env python3
"""
Portfolio Application Installation Script
This script helps set up the portfolio application
"""

import os
import sys
import subprocess
import json

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'static/uploads',
        'static/images',
        'logs'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Created directory: {directory}")

def check_portfolio_data():
    """Check if portfolio data file exists and is valid"""
    if not os.path.exists('portfolio_data.json'):
        print("❌ portfolio_data.json not found")
        return False
    
    try:
        with open('portfolio_data.json', 'r') as f:
            data = json.load(f)
        print("✅ Portfolio data file is valid")
        return True
    except json.JSONDecodeError:
        print("❌ portfolio_data.json is not valid JSON")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        env_content = """# Flask Configuration
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DEBUG=True

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
CONTACT_EMAIL=qurrath2809@gmail.com

# Portfolio Configuration
PORTFOLIO_DATA_FILE=portfolio_data.json
UPLOAD_FOLDER=static/uploads
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        print("📝 Created .env file with default configuration")
    else:
        print("✅ .env file already exists")

def main():
    """Main installation function"""
    print("🎯 Portfolio Application Setup")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Check portfolio data
    if not check_portfolio_data():
        print("⚠️  Please ensure portfolio_data.json exists and is valid")
        sys.exit(1)
    
    # Create .env file
    create_env_file()
    
    # Install requirements
    if not install_requirements():
        print("⚠️  Please install requirements manually: pip install -r requirements.txt")
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Update .env file with your email configuration")
    print("2. Update portfolio_data.json with your information")
    print("3. Run the application: python run.py")
    print("\n🚀 Happy coding!")

if __name__ == '__main__':
    main()
