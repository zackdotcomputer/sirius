#!/usr/bin/env python3
import os, re

if os.path.exists('.env'):
    print('Importing environment from .env...')
    regex = re.compile(r"#.*$") # strip comments
    for line in open('.env'):
        kv = regex.sub("", line).strip()
        if '=' not in kv:
            continue
        name, value = kv.split('=', 1)
        os.environ[name] = value

import struct
from flask import Flask, Response

from sirius.coding import bitshuffle
from sirius.coding import claiming

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def homepage():
    return app.send_static_file('index.html')

@app.route("/fakeprinter")
def build_printer():
    device_address = os.urandom(8).hex()
    xor = bitshuffle.hardware_xor_from_device_address(device_address)
    secret = os.urandom(5).hex()

    cc = claiming.encode(xor, int(secret, 16))

    # Fake the printer ID, which in real-sirius is just the local Postgres ID long
    printerid = int(os.urandom(2).hex(), 16)

    filename = device_address + '.printer'

    fake_printer = (
        '     address: {}\n'.format(device_address) +
        '       DB id: {}\n'.format(printerid) +
        '      secret: {}\n'.format(secret) +
        '         xor: {}\n'.format(xor) +
        '  claim code: {}\n'.format(cc)
    )

    print('\nCreated and returned a fake printer file named {}'.format(filename))

    resp = Response(fake_printer)
    resp.headers['content-disposition'] = 'attachment; filename="' + filename + '"'
    return resp

if __name__ == '__main__':
    app.run()
