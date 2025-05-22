import ollama
import json
import click

def more_stacks(stack):
    with open("stacks.json", "r") as f:
        stacks = json.load(f)
    response = ollama.generate(
        model="mistral",
        prompt = f"Provide only the installation commands for {stack} for windows,linux and macos in the format as mentioned: {{'stack_name': {{'os_name': ['command1', 'command2', ...]}}}}. Do not include any other text or explanation."    )
    print(response['response'])
    try:
      nstack = json.loads(response['response'].lower())
      stacks.update(nstack)
      with open("stacks.json", "w") as f:
          json.dump(stacks, f, indent=2)
      click.echo("New stacks added successfully!")
    except json.JSONDecodeError:
      click.echo("Failed to decode JSON response. Please check the format of the response.")

    
