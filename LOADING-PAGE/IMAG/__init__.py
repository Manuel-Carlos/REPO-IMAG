from flask import Flask, render_template,redirect,request,flash

IMAG= Flask(__name__)
IMAG.config['SECRET_KEY']="IMAGSEGURA"
IMAG.secret_key='IMAGSEGURA'

from IMAG.controllers import default

