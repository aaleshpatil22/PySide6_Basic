# PySide6 QLabel Example

This project demonstrates the usage of the QLabel element in PySide6, a Python binding for the Qt framework. The `main.py` file creates a simple PySide6 application with a QWidget containing a QLabel, QLineEdit, QPushButton, and another QLabel to showcase QLabel-related functionalities.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases the implementation of a PySide6 application utilizing the QLabel element to display a static label, capture text input using a QLineEdit, and update another QLabel dynamically based on user interaction.

## Project Structure

- **main.py**: The main Python script that creates the PySide6 application using QLabel.
- **README.md**: Documentation file providing information about the project.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/aaleshpatil22/PySide6_Basic.git
   cd PySide6_Basic/Label
   ```

2. Ensure you have Python and PySide6 installed:

   ```bash
   pip install PySide6
   ```

## Usage

Run the `main.py` script to launch the PySide6 application:

```bash
python main.py
```

Explore the PySide6 application with QLabel, QLineEdit, and QPushButton elements. Enter text in the QLineEdit, click the "Grab Data" button, and observe the dynamic update of the second QLabel.

## Features

- Use of QLabel to display static text.
- Connection of QPushButton to a slot method (`button_clicked`) for capturing text input.
- Demonstration of various signal connections to QLineEdit for real-time updates.

## Contributing

Feel free to contribute to this project by opening issues, suggesting enhancements, or submitting pull requests. Follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE.txt) file for details.

---
