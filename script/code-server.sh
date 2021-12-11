docker run -itd \
--name code-server \
-p 8086:8080 \
-u root \
-e PASSWORD=123456 \
-v /home/pi/vscoder/.config:/home/coder/.config \
-v /home/pi/vscoder:/home/coder/project \
codercom/code-server:latest \
--auth password