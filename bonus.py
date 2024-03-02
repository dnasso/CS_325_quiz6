class User():
    def __init__(self):
        self.steps = 0
        self.distance = 0
        self.calories = 0
class Activity:
    def __init__(self):
        pass
    def processActivity():
        print("Activity not properly implemented")
class Running(Activity):
    def __init__(self, monitor):
        self.monitor = monitor
    def processActivity(self, dataIn):
        print("Running detected")
        for i in dataIn:
            milesRan = i
            steps = 2000 * milesRan #aproximately
            calories = 100 * milesRan #aproximately
            dataOut = [milesRan, steps, calories]
        self.monitor.readActivity(dataOut)

class Swimming(Activity):
    def __init__(self, monitor):
        self.monitor = monitor
    def processActivity(self, dataIn):
        print("Running detected")
        for i in dataIn:
            milesRan = i
            calories = 500 * milesRan #aproximately
            dataOut = [milesRan, calories]
        self.monitor.readActivity(dataOut)
class ActivityMonitor():
    def __init__(self, display, storage):
        self.display = display
        self.storage = storage
    def readActivity(self, data):
        print("User activity read")
        self.display.updateDisplayData(data)
        self.storage.updateUser(data)
class DataStorage():
    def __init__(self, user):
        pass
    def updateUser(self, data):
        pass
class DataStorageRunning(DataStorage):
    def __init__(self, user):
        self.user = user
    def updateUser(self, data):
        print("Data stored successfully")
        self.user.distance = data[0]
        self.user.steps = data[1]
        self.user.calories = data[2]
class DataStorageSwimming(DataStorage):
    def __init__(self, user):
        self.user = user
    def updateUser(self, data):
        print("Data stored successfully")
        self.user.distance = data[0]
        self.user.calories = data[1]

class Display():
    def __init__(self):
        pass
    def updateDisplayData(self, data):
        pass
    def display(self):
        pass

    
class DisplayRunning(Display):    
    def __init__(self):
        self.distance = 0
        self.steps = 0
        self.calories = 0
        print("Display initialized")
    def updateDisplayData(self, data):
        #self.data = data
        self.distance = data[0]
        self.steps = data[1]
        self.calories = data[2]
        print("Activity Data set in Display")
        self.display()
    def display(self):
        print(f"Steps: {self.steps}")
        print(f"Distance: {self.distance} miles")
        print(f"Calories Burned: {self.calories}")

class DisplaySwimming(Display):    
    def __init__(self):
        self.distance = 0
        self.calories = 0
        print("Display initialized")
    def updateDisplayData(self, data):
        #self.data = data
        self.distance = data[0]
        self.calories = data[1]
        print("Activity Data set in Display")
        self.display()
    def display(self):
        print(f"Distance: {self.distance} miles")
        print(f"Calories Burned: {self.calories}")

def demo():
    user = User()
    dataStorage = DataStorageRunning(user)
    display = DisplayRunning()
    monitor = ActivityMonitor(display, dataStorage)
    activity = Running(monitor)

    data = [4.9] #dummy data
    activity.processActivity(data)

    dataStorage = DataStorageSwimming(user)
    display = DisplaySwimming()
    monitor = ActivityMonitor(display, dataStorage)
    activity = Swimming(monitor)

    data = [4.9] #dummy data
    activity.processActivity(data)

if __name__ == "__main__":
    demo()