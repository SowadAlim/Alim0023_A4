# Alim0023_A4
# Rock-Paper-Scissors Game

## Description
The **Rock-Paper-Scissors** application is a Python-based implementation of the classic hand game. Players can compete against the computer, making their choice of "Rock," "Paper," or "Scissors," and the program determines the winner based on the standard rules:
- Rock beats Scissors.
- Scissors beat Paper.
- Paper beats Rock.

This project also demonstrates how to package a Python application into a Docker container for easy deployment and consistent runtime environments.

---

## How to Run the Application

### Without Docker
1. **Pre-requisites**:
   - Python 3 installed on your system.

2. **Steps**:
   - Clone or download this repository.
   - Navigate to the project directory.
   - Run the application with:
     ```bash
     python Rock-Paper-Scissors.py
     ```

### With Docker
1. **Pre-requisites**:
   - [Docker](https://www.docker.com/get-started) installed and running.

2. **Steps to Build and Run**:
   1. **Navigate to the project directory**:
      ```bash
      cd /path/to/your/project
      ```
   2. **Build the Docker image**:
      ```bash
      docker build -t rock-paper-scissors .
      ```
   3. **Run the Docker container**:
      ```bash
      docker run --rm rock-paper-scissors
      ```

---

## Issues Encountered During Docker Image Creation

### Error 1: `zsh: command not found: docker`
   - **Cause**: Docker is not installed, or it is not added to the system's PATH.
   - **Troubleshooting**:
     - Ensure Docker is installed on your system.
     - Verify installation by running:
       ```bash
       docker --version
       ```
     - If this command fails, follow the installation instructions for your operating system [here](https://docs.docker.com/get-docker/).

### Error 2: `Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
   - **Cause**: Docker daemon is not running.
   - **Troubleshooting**:
     - Start the Docker daemon. On macOS, you can do this via the Docker Desktop app.
     - Run:
       ```bash
       docker info
       ```
       If this command fails, restart the Docker service.

### Error 3: `COPY failed: file not found in build context or excluded by .dockerignore: stat Rock-Paper-Scissors.py: file does not exist`
   - **Cause**: The `Rock-Paper-Scissors.py` file was not in the build context directory.
   - **Troubleshooting**:
     - Ensure your `Dockerfile` and `Rock-Paper-Scissors.py` file are in the same directory.
     - Use the correct build context when building the Docker image:
       ```bash
       docker build -t rock-paper-scissors /path/to/your/project
       ```

### Error 4: `The Dockerfile (or referenced files) were not found in the specified build context`
   - **Cause**: The `Dockerfile` is missing or not in the correct directory.
   - **Troubleshooting**:
     - Verify the `Dockerfile` is present in the same directory as your Python script.
     - Check the file is named exactly `Dockerfile` (case-sensitive, no extension).

---

## Assumptions
1. **Docker is Installed**: It is assumed that Docker is already installed on your system or you have access to install it.
2. **Python File Naming**: The Python script is named `Rock-Paper-Scissors.py` and resides in the same directory as the `Dockerfile`.
3. **Network Connectivity**: Network access may be required to download the base Docker image.
4. **Operating System**: Steps provided are primarily for macOS or Linux. Adjustments might be needed for Windows users.

---

## Troubleshooting Steps
1. **Verify Docker Installation**:
   - Run:
     ```bash
     docker --version
     ```
     If this fails, install Docker from [here](https://docs.docker.com/get-docker/).

2. **Check Directory Structure**:
   - Ensure both `Dockerfile` and `Rock-Paper-Scissors.py` are in the same directory.

3. **Build Context**:
   - Specify the correct path to the project when building the Docker image.

4. **Start Docker Daemon**:
   - If Docker commands fail, ensure the Docker daemon is running.

5. **Check for Typos**:
   - Ensure the `Dockerfile` and `Python` script names are correctly spelled and case-sensitive.

---


