class SmartDevice:
    def __init__(self,name,device_id):
        self.name=name
        self.__device_id=device_id
        self.__power="ON"
    @property
    def device_id(self):
        return self.__device_id
    @device_id.setter
    def device_id(self,new_id):
        if new_id !="":
            self.__device_id=new_id
        else:
            print("Device ID cannot be empty")
    @property
    def power(self):
        return self.__power
    def turn_on(self):
        self.__power="ON"
        print(f"{self.name} is ON")
    def turn_off(self):
        self.__power="OFF"
        print(f"{self.name} is OFF")
    def display_info(self):
        print("\nDevice Name:",self.name)
        print("Device ID:",self.device_id)
        print("Power:",self.power)
class SecurityCamera(SmartDevice):
    def __init__(self,name,device_id):
        super().__init__(name,device_id)
        self.recording="TRUE"
    def start_recording(self):
        self.recording="True"
        print("Recording has started")
    def stop_recording(self):
        self.recording="False"
        print("Recording has stopped")
class SmartLight(SmartDevice):
    def __int__(self,name,device_id):
        super().__init__(name,device_id)
        self.__brightness =30
    @property
    def brightness(self):
        return self.__brightness
    def increase_brightness(self):
        if self.__brightness <100:
            self.__brightness += 10
        print("Brightness:",self.__brightness)
    def decrease_brightness(self):
        if self.__brightness > 0:
            self.__brightness -= 10
        print("Brightness:",self.__brightness)
class TemperatureSensor(SmartDevice):
    def __int__(self,name,device_id):
        super().__init__(name,device_id)
        self.temperature = 20
    def read_temperature(self):
        print("Temperature:",self.temperature,"k")

camera = SecurityCamera("Front Camera","CAM106")
light = SmartLight("bedroom light","LGT200")
sensor= TemperatureSensor("Kitchen Sensor","TMP300")

while True:
    print("\n===SMART DEVICE MANAGEMENT===")
    print("1.Display information")
    print("2. Turn all devices ON")
    print("3. Turn all devices OFF")
    print("4. Read Temperature")
    print("5. Increase Brightness")
    print("6. Decrease Brightness")
    print("7. Start Recording")
    print("8. Stop Recording")
    print("Exit")

    choice = (input("Enter your choice:"))

    if choice =="1":
        camera.display_info()
        light.display_info()
        sensor.display_info()

    elif choice =="2":
        camera.turn_on()
        light.turn_on()
        sensor.turn_on()

    elif choice == "3":
        camera.turn_off()
        light.turn_off()
        sensor.turn_off()

    elif choice=="4":
        sensor.read_temperature()

    elif choice == "5":
        light.increase_brightness()

    elif choice == "6":
        light.decrease_brightness()

    elif choice == "7":
        camera.start_recording()

    elif choice =="8":
        camera.stop_recording()

    elif choice == "9":
        print("Thank you for using the Smart Device Management System.")
        break
    else:
        print("Invalid choice. Please try again")












