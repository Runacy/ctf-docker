FROM booyaabes/kali-linux-full

RUN mkdir -p /dev/net && \
  mknod /dev/net/tun c 10 200

WORKDIR /test