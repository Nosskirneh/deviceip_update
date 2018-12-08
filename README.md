# deviceip_update
Update `THEOS_DEVICE_IP` and `_PORT` easily on macOS.

## Installation
Install Python 3 and pip.

`sudo -H pip3 install nmap pyobjc`

Configure `config.json`.

Add this to your `~/.zshrc` or bash profile:
```
deviceip_update() {
    ~/Dropbox/bin/deviceip_update/deviceip_update.py $@
    source ~/Dropbox/bin/theos.sh
}
```

## Example usage
`deviceip_update` and it will set the correct IP and port of the default device depending on the current network.
`deviceip_update A-iP6` will set the correct IP and port of the specified device depending on the current network.
