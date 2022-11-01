# Simple_wss
An example of a simple secure websocket connection


# Credits:
https://github.com/dpallot/asyncws


# How to use

1) Clone this repository

2) Install the dependencies

```console
cd asyncws
py setup.py install
cd ..
```

3) Use your example.crt and example.key. If you want to test with self issued certificate and key run:

```console
openssl req -newkey rsa:2048 -nodes -keyout example.key -x509 -days 365 -out example.crt
```

The scripts won’t work without a certificate and a key.

4) Run server

```console
py server.py
```

5) Run client

```console
py client.py
```

In the client console you should see messages being sent and recived!