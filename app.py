import dotenv
import pkg.bootstrapper.bootstrapper as bootstrapper
import pkg.server.server as server
import os

app = server.initialize_flask_app()
dotenv.load_dotenv()

bootstrapper.initialize_routes(app)


server_address = os.getenv('SERVER_ADDRESS')

if __name__ == "__main__":
    from waitress import serve
    app.config['JSON_SORT_KEYS'] = False
    serve(app=app, host='0.0.0.0', port=server_address)
    # app.run(port=server_address)


