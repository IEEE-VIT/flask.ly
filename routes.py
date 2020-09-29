from flask import Blueprint

router = Blueprint("router", __name__)

@router.route('/status')
def status():
    return "Up and Running ! :)"

@router.route('/shorten')
def shorten():
    # Take the input URL from a user
    # Check if it's already in the database
    # If it already exists: return the shortened URL
    # Else: Shorten it using any encoding or algorithm
    # Store the input URL and the shortened URL
    # mapped together in the url database
    # Return the shortened URL back

@router.route('/register')
def register():
    # Register a User by taking their credentials basically
    # email id and password and storing them in the user database
    # After registration, redirect them to the /shorten/custom

@router.route('/login')
def login():
    # Validate a user by taking their email id and password
    # Check if they match in the user database
    # If they match: redirect them to the /shorten/custom
    # Else send them appropriate message accordingly

@router.route('/logout')
def logout():
    # Check if a User is logged in
    # If user is logged in, log them out

@router.route('/shorten/custom')
def customShorten():
    # Check whether the user is logged in or not
    # If the user is not logged in, redirect them to the /login page
    # else take the input URL to be shortened & the shortened URL they want
    # Check if the shortened URL is already present in the database
    # If its not, store the user's input and return their custom URL
    # Else ask the user to enter any other custom URL and repeat the process
