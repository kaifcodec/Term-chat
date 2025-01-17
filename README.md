# Term-chat

*World's First ever chat repository which lets you chat over the internet from anywhere with your friends or family members using Termux and Ngrok. Why use WhatsApp when you don't have privacy? Use this command-line tool and be cool.*

---

## Key Features

1. **Lightweight**
2. **No connection issues**
3. **Localhost chat over Wi-Fi or hotspot**
4. **Supports all file formats**
5. **Send directories (zip them first)**
6. **Requires Ngrok account and authtoken**
7. **Easy Ngrok authtoken acquisition**
8. **Uses sockets for stable connections**
9. **Built with Python**
10. **Compatible with Termux**
11. **Runs on other environments**
12. **Regular updates and bug fixes**
13. **24×7 issue resolution service**

---

## Usage Commands for Termux

1. `cd $HOME`
2. `apt update -y && apt upgrade -y`
3. `pkg install git`
4. `pkg install openssl`
5. `pkg install python`
6. `pkg install wget unzip`
7. `git clone https://github.com/kaifcodec/Term-chat.git`
8. `wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip`
9. `unzip ngrok-stable-linux-arm.zip`
10. `mv ngrok /data/data/com.termux/files/usr/bin/`
11. `cd Term-chat`
12. `pip install -r requirements.txt`
13. `python server.py`

---

## Next Steps

1. **Server Start**
   - After completing the above commands, your server will start successfully.
   - It will display "Server started at 0.0.0.0:port".
   - Note the port number.

2. **Ngrok Setup**
   - Start a new session and enable the hotspot on your phone.
   - Get your Ngrok authtoken from the official site.
   - Run `ngrok config add-authtoken 'your_authtoken'`
   - Run `ngrok tcp 'port'` (use the server's listening port)
   - Ngrok will provide a link like `tcp://0.tcp.in.ngrok.io:port2`. Copy it.

3. **Client Connection**
   - In the Term-chat directory, run `python client.py`
   - Enter the copied Ngrok link IP (i.e. 0.tcp.in.ngrok.io) and port.
   - Choose your nickname and join the server.

---

## Steps for Others to Join the Chat

1. Clone the repository in their Termux.
2. Install the requirements.
3. Start `client.py` using `python client.py`.
4. Enter the same IP and port from the Ngrok link.
5. Choose a nickname and start chatting.

---

## Additional Features

- **File Transfers**
  1. Copy the path of the file you want to send.
  2. Type `#file` in the chat.
  3. Paste the copied path when prompted.
  4. Press enter to send the file.

---

## Troubleshooting

1. **Server IP Issues**
   - If starting the server one after another, change the server IP on which it is listening (use the nano tool for editing).
2. **Upcoming Automation**
   - Automation functions will be updated soon.
3. **Issue Reporting**
   - Open an issue if you encounter any errors and provide screenshots for quick resolution.

---

Feel free to reach out for any support or suggestions!

---
