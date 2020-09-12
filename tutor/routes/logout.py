from .. import app
from ..controllers import logout

@app.route('/logout')
def logout_route():
    return logout.logout()