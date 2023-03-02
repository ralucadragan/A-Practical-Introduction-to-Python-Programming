'''
4. Write a class called Time whose only field is a time in seconds. It should have a method called
convert_to_minutes that returns a string of minutes and seconds formatted as in the following
example: if seconds is 230, the method should return '5:50'. It should also have
a method called convert_to_hours that returns a string of hours, minutes, and seconds
formatted analogously to the previous method.
'''

class Time:
# Write a class called Time whose only field is a time in seconds
    def __init__(self, seconds):
        self.seconds = seconds

    def convert_to_minutes(self):
        # that returns a string of minutes and seconds formatted as in the following example:
        # if seconds is 230, the method should return '3:50'.
        min = int(self.seconds / 60)
        sec = self.seconds - (60 * min)
        print(f'The times is: {min}:{sec}')

    def convert_to_hours(self):
        # returns a string of hours, minutes, and seconds
        # formatted analogously to the previous method.
        sec = int(self.seconds % 60)
        hour = int(self.seconds /60)
        min = int(hour % 60)
        hour = int(hour / 60)
        print(f'The time is: {hour}:{min}:{sec}')


s = Time(230)
print(s.convert_to_minutes())

s = Time(18951)
print(s.convert_to_hours())