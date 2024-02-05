# UTF-8 Encoder and Decoder in Python
This repository is dedicated to providing a comprehensive learning tool for understanding and implementing UTF-8 encoding and decoding mechanisms using Python. The UTF-8 standard is a cornerstone of modern text processing and data exchange, enabling the representation of character sets from around the globe in a uniform manner.

# Overview
UTF-8 (8-bit Unicode Transformation Format) is a variable width character encoding capable of encoding all 1,112,064 valid character code points in Unicode using one to four 8-bit bytes. This encoding is designed for backward compatibility with ASCII and to avoid the complications of byte order marks (BOMs). Our project contains Python implementations for both encoding Unicode code points into UTF-8 bytes and decoding UTF-8 bytes back to Unicode code points.

# Features
**UTF-8 Decoder**: Converts UTF-8 encoded bytes into their corresponding Unicode code points, supporting characters from 1 to 4 bytes in length.
**UTF-8 Encoder**: Transforms Unicode code points into UTF-8 encoded bytes, ensuring compatibility with the wide range of characters represented in Unicode.
**Educational Comments**: Both the encoder and decoder are heavily commented to facilitate understanding of the UTF-8 encoding and decoding processes.
**Unit Tests**: Includes comprehensive tests to ensure accuracy and reliability of the encoding and decoding functions.


# Getting Started
To get started with this project, clone the repository and install the required dependencies:

```bash
Copy code
git clone git@github.com:zokis/utf8-encode-decode.git
cd utf8-encode-decode
pip install -r requirements.txt
```

Run the tests to ensure everything is set up correctly:
```
pytest
```

# How to Use
This repository is intended for educational purposes and can be a valuable resource for students and developers looking to deepen their understanding of text encoding, Unicode, and how characters are represented digitally. The source code can be used as a reference or incorporated into larger projects that require custom handling of UTF-8 data.

# Contributing
Contributions to this project are welcome, especially those that enhance educational value or extend functionality. Whether you're fixing bugs, improving the documentation, or adding new features, your input is appreciated.

# License
This project is open-source and available under the GPL-3.0 license. Feel free to use, modify, and distribute the code as you see fit.
