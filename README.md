# StackTool

StackTool is a command-line interface (CLI) tool designed to automate the installation of tech stacks based on user prompts. It checks for prerequisites, installs stacks using predefined commands, and provides stack suggestions with explanations using a local language model (Mistral 7B via Ollama). 

## Features
- **Install Stacks**: Automatically install tech stacks (e.g., React Native, MERN, Django) using OS-specific commands from `stacks.json`.
- **Prerequisite Checks**: Verifies if Node.js, Python, or Chocolatey are installed, with clear error messages if missing.
- **Stack Suggestions**: Processes user prompts (e.g., "Python ML stack") and suggests stacks with explanations using Mistral 7B.
- **Use Case Recommendations**: Suggests stacks for specific use cases (e.g., "web development").
- **Cross-Platform**: Supports Windows, Linux, and macOS.

