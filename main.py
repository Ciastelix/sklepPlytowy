from app import db, app
from views import *
from uzytkownik.uzytkownik import uzytkownik
from muzyka.muzyka import muzyka

app.register_blueprint(uzytkownik, url_prefix="/uzytkownik")
app.register_blueprint(muzyka, url_prefix="/muzyka")
app.register_blueprint(muzyka)


if __name__ == "__main__":
    app.run(debug=True)
