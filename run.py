from app import app, db
from app.models import Guest

app = create_app()
# flask shell context
@app.shell_context_processor
def shell_context():
    return {'app': app, 'db': db, 'Guest': Guest}