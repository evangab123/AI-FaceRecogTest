from sqlalchemy import text
from session import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connsuccessful:", result.scalar())
except Exception as e:
    print("Connfailed:", str(e))
