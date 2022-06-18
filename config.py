from auxiliary import get_dolphin_token
# Don't touch the code above

INDIGO_TOKEN = '<indigo_token>'  # Replace <indigo_token> to token from Indigo settings
INDIGO_PORT = '<indigo_port>'  # Replace <indigo_port> to port from Indigo settings
DOLPHIN_LOGIN = '<dolphin_login>'  # Replace <dolphin_login> to login for Dolphin Anty
DOLPHIN_PASSWORD = '<dolphin_password>'  # Replace <dolphin_password> to password for Dolphin Anty

# Don't touch the code below
DOLPHIN_TOKEN = f'Bearer {get_dolphin_token(DOLPHIN_LOGIN, DOLPHIN_PASSWORD)}'
