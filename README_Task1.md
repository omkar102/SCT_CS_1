# Caesar Cipher - Encryption & Decryption Tool

## SkillCraft Technology - Cybersecurity Internship
**Task 01:** Caesar Cipher Implementation

## Project Description
A user-friendly GUI application that implements the **Caesar Cipher algorithm** for text encryption and decryption. The Caesar Cipher is one of the oldest and simplest encryption techniques, where each letter in the plaintext is shifted by a fixed number of positions down the alphabet.

## Features
- **Encryption:** Convert plain text into encrypted cipher text
- **Decryption:** Convert cipher text back to plain text
- **Adjustable Shift Value:** Choose any shift value from 1 to 25
- **Modern GUI:** Clean and intuitive graphical interface
- **Text Area Support:** Handle multiple lines of text
- **Clear Function:** Quick reset of all fields
- **Real-time Processing:** Instant encryption/decryption results

## How It Works
The Caesar Cipher algorithm shifts each letter in the text by a specified number of positions:
- **Encryption:** Each letter moves forward by the shift value
  - Example: With shift 3, 'A' becomes 'D', 'B' becomes 'E'
- **Decryption:** Each letter moves backward by the shift value
  - Example: With shift 3, 'D' becomes 'A', 'E' becomes 'B'
- **Special Characters:** Numbers, spaces, and punctuation remain unchanged

## Installation & Usage
### Prerequisites
- Python 3.x installed
- tkinter library (usually comes pre-installed with Python)

### Running the Application
1. **Clone or download this repository**
   ```bash
   git clone https://github.com/omkar102/SCT_CS_1.git
   cd SCT_CS_1
   ```

2. **Run the program**
   ```bash
   python caesar_cipher_gui.py
   ```

3. **Using the Application**
   - Enter your message in the input text area
   - Select a shift value (1-25) using the spinner
   - Click **ENCRYPT** to encrypt the message
   - Click **DECRYPT** to decrypt the message
   - Click **CLEAR** to reset all fields

## Example
**Original Text:** `Hello World`
**Shift Value:** `3`
**Encrypted Text:** `Khoor Zruog`
**Decrypted Text:** `Hello World`

## Technical Details
- **Language:** Python 3.12
- **GUI Framework:** Tkinter
- **Algorithm:** Caesar Cipher (Shift Cipher)
- **Complexity:** O(n) where n is the length of the input text

## Learning Outcomes
Through this project, I learned:
- Implementation of classical cryptography algorithms
- Building interactive GUI applications with Tkinter
- String manipulation and character encoding in Python
- Event-driven programming concepts
- User input validation and error handling


## Author
**Omkar Vivek Joshi**
- Cybersecurity Intern @ SkillCraft Technology
- www.linkedin.com/in/omkar-joshi-b000b3388 [LINKEDIN]
- https://github.com/omkar102/SCT_CS_1.git [GITHUB]

## License
This project is created as part of the SkillCraft Technology Cybersecurity Internship program.

## Acknowledgments
- SkillCraft Technology for the internship opportunity
- Caesar Cipher algorithm - one of the earliest encryption techniques
- Python Tkinter documentation and community

