# settings.py

# Initial settings
GRAVITY = 1
VELOCITY = 50

# Function to update settings
def update_settings(new_gravity, new_velocity):
    global GRAVITY, VELOCITY
    GRAVITY = new_gravity
    VELOCITY = new_velocity
