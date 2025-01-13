# Term-chat
World's First ever chat repository which let you chat over internet from any where with your friends or family members. By just using termux and ngrok.
Why use WhatsApp when you don't have privacy use this command line and be cool.

# Key Features:
1. Light weight.
2. No connection issue.
3. One can use it for localhost chats over wifi or using hotspot
4. It's not just a message sending tool you can send anything with it (file formats).
5. To send any directory first zip the directory and then use the additional commands below for using. (Automated function will be introduced soon in the new releases.
6. Chatting over the internet requires an account in ngrok and it's authtoken that's and it's super easy to get.
7. To get ngrok authtoken login to official ngrok and they will provide it immediately.
8. Uses socket for issue less connection
9. Only python language
10. No errors for using in termux
11. One can use it on other environments
12. Regular updates and bug fixes
13. 24×7 issue resolve service

# Usage commands for Termux
1. cd $HOME
2. apt update -y && apt upgrade-y
3. pkg install git
4. pkg install openssl
5. pkg install python
6. pkg install wget unzip
7. git clone https://github.com/kaifcodec/Term-chat.git
8. wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
9. unzip ngrok-stable-linux-arm.zip
10. mv ngrok /data/data/com.termux/files/usr/bin/
11. cd Term-chat 
12. pip install -r requirements.txt
13. python server.py

# Next steps
1. After the above all commands your server is started successfully.
2. It will show you started server at 0.0.0.0:<port>
3. Keep in mind that port.
4. Now the next step is to start a new session from the left side bar.
5. Start hotspot on your phone.
6. Get you ngrok authtoken from there official site after logging in.
7. Now run the following commands;
ngrok config add-authtoken <your_authtoken>
ngrok tcp <port>
8. Here the port is equals the port in which the server is listening.
9. ngrok tunneling is started successfully.
10. You will now see on the display it will connect to the server and forward datas from the clients over internet so it will provide you a link eg. tcp://0.tcp.in.ngrok.io:<port2> just copy the '0.tcp.in.ngrok.io' part of the link and go to next session.
11. In this session the Term-chat directory run
python client.py
12. Now it will ask for server IP paste that copied '0.tcp.in.ngrok.io'
13. Then it will ask for port, input the port2 of that ngrok link and enter, then Choose your nick name that's it you joined the server.
14. You are all set, Remember you are the host as you running the server.

# Next steps for the others to chat
It's easy for the clients;
1. First they need to clone my repository in there termux
2. install the requirements
3. Then start client.py , using 'python client.py' command.
4. Now enter same ip and port as you entered from the ngrok link>choose nickname and that's it.
5. You will get a message that the client joined now start chatting.

# Additional features
 It just don't sends messages
1. You can send any file to each other.
2. First copy the path of the file that you want to send.
3. type '#file' on the chatting display
4. It will ask you for the path just paste the copied.
5. Press enter and it will be sent.


# Troubleshoot
1. One trouble you will get i.e. sever ip. if you start the server ip one after another you need to change the server ip on which it is listening. (use nano tool for that)
2. Automation function will be updated soon. no worries.





