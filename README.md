# TCP Socket Communication Experiment

A simple Python project demonstrating **client-server communication using TCP sockets**.

This project was created to understand the basics of:

- Socket programming
- TCP communication
- Client-server architecture
- Sending and receiving data over sockets
- Basic command execution concepts

---

## 📌 Features

- TCP connection between client and server
- Client can send messages to the server
- Server receives and processes incoming messages
- Server sends responses back to the client
- Basic subprocess usage for command execution experiments

---

## 🛠️ Technologies Used

- Python 3
- `socket` module
- `subprocess` module

---

## 🚀 Usage

### 1. Start the Server

Run:

```bash
python server.py
```

### 2. Start the Client

Open another terminal and run:

```bash
python client.py
```

### Example

Client:

```
>> hello
```

Server response:

```
Response from server: Mesaj Alindi
```

To close the client:

```
>> quit
```

---

## 🔐 Security Note

This project was created for educational purposes to understand socket communication.

The server-side implementation uses:

```python
subprocess.run(..., shell=True)
```

to demonstrate command execution.

⚠️ This approach is **not safe for production environments** because executing untrusted user input may lead to **command injection vulnerabilities**.

A real-world implementation should include:

- Input validation
- Authentication
- Authorization
- Secure communication using TLS
- Safer command handling

---

## ⚠️ Disclaimer

This project should only be used in a controlled local environment.

Do not expose this server directly to the internet.

---

## 📚 Learning Goals

Through this project, I practiced:

- Understanding TCP sockets
- Creating basic client-server communication
- Working with network connections
- Handling byte encoding/decoding
- Exploring security risks related to command execution
