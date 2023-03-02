'''
3. Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password.
There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not.
'''

class Password_manager:

    def __init__(self):
        # define an empty list for the old passwords
        self.old_pass = []

    def get_passord(self):
        # get the last password from list
        return self.old_pass[-1]

    def set_password(self, password):
        # does the password already exist?
        if password not in self.old_pass:
            # add new password to list of old passwords
            self.old_pass.append(password)
        return password # nu pot sa pun self.password pt ca in funct de initializare nu l-am definit

    def is_correct(self, password):
        # string is equal to the curent password or not
        return password == self.get_passord()

# create an instance of the password manager
a = Password_manager()
# prefill the list of old passwords
a.old_pass = ['ala', 'bala', 123, 'qwerty']
print(f'The user curent password is: {a.get_passord()}')
# set a new
a.set_password('asdfg')
print(f"The new passord is: {a.set_password('asdfg')}")
# check passord with a string
print(a.is_correct('mumu'))
print(a.is_correct('asdfg'))