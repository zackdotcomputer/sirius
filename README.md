# sirius-printerfaker

A pared down version of Sirius to just create fake printer files

This project is designed to simplify the first setup steps of joining @ktamas's [TinyPrinterClub](tinyprinter.club).
While previously, you had to download and set up your own copy of the Sirius server to get a `.printer` file to then
use on your local client, this fork removes all the superfluous server code and weight from that server project and
just gives you an easy "one button press" website to get a faked `.printer`.

You can use it directly at [this heroku instance](https://printerfaker.herokuapp.com/) or you can download and run it
locally in python or docker using:

```sh
# For Python:
pip install requirements.txt
python ./printerfaker.py
```

```sh
# For Docker:
docker-compose up --build -d
```

In either case, you'll be able to get to the same website as is running on heroku by going to http://localhost:5000.
