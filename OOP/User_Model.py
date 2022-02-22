class User:
    def __init__(self, username, password, email, admin=False):
        """Upon initiation, declare the attributes using the given variables."""
        self.username = username
        self.password = password
        self.email = email
        # self.hint = hint
        self.admin = admin

    def get_username(self):
        """Returns the username"""
        return self.username

    def get_password(self):
        """Returns the password"""
        return self.password

    def get_email(self):
        """Returns the email"""
        return self.email

    def is_admin(self):
        """Returns the admin status"""
        return self.admin

    def set_username(self, new_username):
        """Edits the username"""
        # check if valid user, verify if user knows password, check if existing user, check if hits requirements
        self.username = new_username

    def set_password(self, new_password):
        """Edits the password"""
        # check if valid pass
        self.password = new_password

    def set_email(self, new_email):
        """Edits the email"""
        # check if valid email, check if taken
        self.email = new_email

    def set_admin(self):
        """Edits the admin status"""
        # make sure is being used by an admin user
        self.admin = True
