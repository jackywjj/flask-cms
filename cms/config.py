# Debug enviroment
DEBUG = True
# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print BASE_DIR
# Define the database
SQLALCHEMY_DATABASE_URI = 'mysql://root:admin123@127.0.0.1/cmsdb'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "mkoiujnbhyt"

# Secret key for signing cookies
SECRET_KEY = "0372ikxmjs7123746"

BACKEND_URI = "/backend"

POSTS_PER_PAGE = 24

UPLOAD_PATH_CATEOGRY = "/workdisk/workspace-python/jdsheep/jdsheep/app/static/uploads/c/"
UPLOAD_PATH_PRODUCT = "/workdisk/workspace-python/jdsheep/jdsheep/app/static/uploads/p/"

UPLOAD_URL_CATEOGRY = "/static/uploads/c/"
UPLOAD_URL_PRODUCT = "/static/uploads/p/"
