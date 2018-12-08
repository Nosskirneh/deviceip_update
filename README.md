# deviceip_update
Update THEOS_DEVICE_IP and PORT easily on macOS

Configure `config.json`.

Add this to your ~/.zshrc or bash profile:
```
deviceip_update() {
    ~/Dropbox/bin/deviceip_update/deviceip_update.py $@
    source ~/Dropbox/bin/theos.sh
}
```

Example usage:
`deviceip_update A-iP6` and it will automatically set the correct IP and port depending on what network you're on.
