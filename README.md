# Mega-IO Web Interface
A simple, local web dashboard to be used with the Raspberry Pi Mega-IO Expansion Card

(Toggle the relays by clicking the text of the relay(s) you'd like to toggle)
## Getting started:
1. Make sure you have both the [Mega-IO Commands](https://github.com/alexburcea2877/megaio-rpi) and [Wiring Pi](http://wiringpi.com/download-and-install/) installed
2. `git clone https://github.com/tbaumer22/megaio-web-interface.git`
3. `cd` into the repository root and type: `pip install Flask`
4. Then type: `sudo python app/index.py`

You should be able to go to the url:`0.0.0.0:80` on your system and see a dashboard.

If you do not see a dashboard, you've done something wrong. In most cases, you haven't completed Step 1 properly.

![Picture of the dashboard](https://tate.ate-a-ta.co/dba59ec4.png)