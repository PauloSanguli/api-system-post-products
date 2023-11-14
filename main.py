from src.server.api.app import app
from src.server.api.controllers.__login__ import app
from src.server.api.controllers.__admin__ import app
from src.server.api.controllers.__editAccount__ import app
from src.server.api.controllers.__posts__ import app
from src.server.api.controllers.__logout__ import app
from src.server.api.controllers.__recover_account__ import app




if __name__ == '__main__':

    app.run(
        port=1357,
        debug=True
    )