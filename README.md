# StackTool

StackTool is a command-line interface (CLI) tool designed to automate the installation of tech stacks based on user prompts. It checks for prerequisites, installs stacks using predefined commands, and provides stack suggestions with explanations using a local language model (Mistral 7B via Ollama). Phase 1 focuses on core functionality, with plans for expansion in future phases.

## Features
- **Install Stacks**: Automatically install tech stacks (e.g., React Native, MERN, Django) using OS-specific commands from `stacks.json`.
- **Prerequisite Checks**: Verifies if Node.js, Python, or Chocolatey are installed, with clear error messages if missing.
- **Stack Suggestions**: Processes user prompts (e.g., "Python ML stack") and suggests stacks with explanations using Mistral 7B.
- **Use Case Recommendations**: Suggests stacks for specific use cases (e.g., "web development").
- **Cross-Platform**: Supports Windows, Linux, and macOS.

## Requirements
- Python 3.9+
- Ollama [](https://ollama.ai) with Mistral 7B model (`ollama pull mistral`)
- Node.js (for stacks like React Native, MERN, Vue)
- Python (for stacks like Django, Python-ML)
- Chocolatey (for Windows stacks like Flutter, LAMP)
- `stacks.json` file with installation commands
