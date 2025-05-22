# server.py
from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/html/<path:filename>')
def serve_html(filename):
    return send_from_directory(app.static_folder, filename)
st.markdown(
    '<a href="https://html-flask-server.onrender.com" target="_blank">Abrir HTML</a>',
    unsafe_allow_html=True)

#if __name__ == '__main__':
 #   app.run(port=5001)
