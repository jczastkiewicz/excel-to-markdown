import subprocess
import os
import sys

def main_app():
    """Runs the streamlit app."""
    # The path to the streamlit app file (src/app.py)
    app_file = os.path.join(os.path.dirname(__file__), "src", "app.py")

    # The command to run the streamlit app
    command = [sys.executable, "-m", "streamlit", "run", app_file]

    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    main_app()
