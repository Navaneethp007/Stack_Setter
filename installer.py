import json
import platform
import subprocess
import click

os_name = platform.system().lower()
def load_commands(stack_name):
    with open("stacks.json", "r") as f:
        stacks = json.load(f)
    return stacks.get(stack_name, {}).get(os_name, [])

def install_stack(stack_name):
    if stack_name in ["react-native", "mern", "vue"]:
        result = subprocess.run(["node", "-v"], capture_output=True, check=False)
        if result.returncode != 0:
            click.echo("Node.js is not installed yet. Please install Node.js and try again.")
            return
    if stack_name in ["python-ml", "django"]:
        result = subprocess.run(["python", "--version"], capture_output=True, check=False)
        if result.returncode != 0:
            click.echo("Python is not installed yet. Please install Python and try again.")
            return
    if os_name == "windows" and stack_name in ["flutter", "lamp", "spring-boot"]:
        result = subprocess.run(["choco", "-?"], capture_output=True, check=False)
        if result.returncode != 0:
            click.echo("Chocolatey is not installed yet. Please install Chocolatey and try again.")
            return
    commands = load_commands(stack_name)
    if not commands:
        click.echo(f"No installation commands found for {stack_name} on {os_name}.")
        return
    
    click.echo(f"Installing {stack_name}...")
    for cmd in commands:
        try:
            subprocess.run(cmd.split(), check=True)
        except subprocess.CalledProcessError as e:
            click.echo(f"Error installing {stack_name}: {e}", err=True)
            return
    click.echo(f"{stack_name} installed successfully!")
