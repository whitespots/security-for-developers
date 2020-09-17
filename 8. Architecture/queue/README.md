# Run Redis

*Never use ALLOW_EMPTY_PASSWORD=yes* except your sandbox games

```bash
docker run --rm -p6379:6379 -d --name redis -e ALLOW_EMPTY_PASSWORD=yes bitnami/redis:latest
```

# Copy configs
`sudo cp *.service /etc/systemd/system/`

# Run a service with workers
sudo systemctl daemon-reload
sudo systemctl start whitespots
sudo systemctl start rqworker@1.service
sudo systemctl start rqworker@2.service
