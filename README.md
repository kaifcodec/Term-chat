# Term-chat
World's First ever chat repository which let you chat over internet from any where with your friends or family members. By just using termux and ngrok.
Features:
1. Light weight.
2. No connection issue.
3. One can use it for localhost chats over wifi or using hotspot
4. Chatting over the internet requires an account in ngrok and it's authtoken that's and it's super easy to get.
5. To get ngrok authtoken login to official ngrok and they will provide it immediately.
6. Uses socket for issue less connection
7. Only python language
8. No errors for using in termux
9. One can use it on other environments
10. Regular updates and bug fixes
11. 24×7 issue resolve service

# Usage commands for Termux
cd $HOME
apt update -y && apt upgrade-y
pkg install git
pkg install openssl
pkg install python
git clone https://github.com/kaifcodec/Term-chat.git
cd Term-chat 
pip install -r requirements.txt
python server.py

# Next steps
1. After the above all commands your server is started successfully.
2. Now the next step is to start a new session from the left side bar.
3. Start hotspot on your phone.
4. Get you ngrok authtoken from there official site after logging in.
5. 







