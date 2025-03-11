
# from __init__ import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)
  




# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# from src import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Utilise le port de Render (ou 5000 en local)
    app.run(host="0.0.0.0", port=port, debug=True)  # Le host doit être "0.0.0.0"