#!/usr/bin/env python3
"""
Setup script for CleanTech AI Waste Classification App.
This script sets up the environment, installs dependencies, and verifies required files.
"""

import sys
import os
import subprocess
import venv
import shutil

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    print("Checking Python version...")
    if sys.version_info < (3, 7):
        print(f"❌ Error: Python 3.7 or higher is required. You are using {sys.version.split()[0]}.")
        sys.exit(1)
    print(f"✅ Python version {sys.version.split()[0]} is compatible.")

def create_virtual_env(env_name="venv"):
    """Create a virtual environment."""
    if os.path.exists(env_name):
        print(f"Virtual environment '{env_name}' already exists.")
        return
    print(f"Creating virtual environment '{env_name}'...")
    venv.create(env_name, with_pip=True)
    print(f"✅ Virtual environment '{env_name}' created.")

def install_dependencies(env_name="venv"):
    """Install dependencies from requirements.txt."""
    requirements_file = "requirements.txt"
    if not os.path.exists(requirements_file):
        print(f"Error: {requirements_file} not found.")
        sys.exit(1)

    pip_path = os.path.join(env_name, "Scripts", "pip") if os.name == "nt" else os.path.join(env_name, "bin", "pip")
    print("Installing dependencies...")
    try:
        subprocess.check_call([pip_path, "install", "-r", requirements_file])
        print("✅ Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        print("Please check your network connection and try again.")
        sys.exit(1)

def verify_files():
    """Verify presence of required model and config files."""
    print("Verifying required files...")
    required_files = ["waste_classifier.h5", "class_indices.json"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    if missing_files:
        print(f"❌ Error: Missing required files: {', '.join(missing_files)}. Please ensure they are in the root directory.")
        sys.exit(1)
    print("✅ All required files are present.")

def main():
    print("Setting up CleanTech AI Waste Classification App...")
    check_python_version()
    create_virtual_env()
    install_dependencies()
    verify_files()
    print("\n🚀 Setup complete! 🚀")
    print("To activate the virtual environment:")
    if os.name == "nt":
        print(f"  > .\\{os.path.join('venv', 'Scripts', 'activate')}")
    else:
        print(f"  $ source {os.path.join('venv', 'bin', 'activate')}")
    print("Then run: python app.py")

if __name__ == "__main__":
    main()
