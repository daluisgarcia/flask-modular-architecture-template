# from flaskwebgui import FlaskUI
from core import create_app
from core import config

server_port: int = int(config.get('PORT', 8080))
ip_addr: str = '0.0.0.0'
debug_mode: bool = bool(config.get('DEBUG', False))

app = create_app()
# ui = FlaskUI(app, host=ip_addr, port=server_port, maximized=True, close_server_on_exit=True)

if __name__ == "__main__":
    app.run(host=ip_addr, port=server_port, debug=debug_mode, threaded=True)
