a popular cryptographic hashing function used primarily for securing
storing passwords.
Here's what you need to know about it:

Purpose:

bcrypt is designed specifically for hashing passwords.
It's highly resistant to brute-force attacks.


Key Features:

Salt: bcrypt automatically generates and incorporates a salt, which is random data added to the input before hashing.
Adaptive: It can be made slower over time as computing power increases, maintaining security.


How it works:

bcrypt uses the Blowfish encryption algorithm to create a hash.
It applies multiple rounds of hashing (work factor), making it
computationally intensive.

it is installed using pip install bcrypt
