import dotenv
import pkg.bootstrapper.bootstrapper as bootstrapper
import pkg.server.server as server
import os

app = server.initialize_flask_app()
dotenv.load_dotenv()

bootstrapper.initialize_routes(app)

if __name__ == "__main__":
    app.config['JSON_SORT_KEYS'] = False
    app.run(port=os.getenv('SERVER_ADDRESS'))


