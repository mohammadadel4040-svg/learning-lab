# Week 8 -- IoT Device Management System

from datetime import datetime, timedelta


class Device:

    def __init__(self, device_id, device_type, owner):
        self.__device_id = device_id
        self.__device_type = device_type
        self.__owner = owner
        self.__firmware_version = "1.0"
        self.__compliance_status = "unknown"
        self.__last_security_scan = None
        self.__is_active = True

    def run_security_scan(self):
        self.__last_security_scan = datetime.now()
        self.__compliance_status = "compliant"

    def check_compliance(self):

        if self.__last_security_scan is None:
            return False

        days = (
            datetime.now() - self.__last_security_scan
        ).days

        if days > 30:
            self.__compliance_status = "non-compliant"
            return False

        return True

    def authorise_access(self, user):

        if not self.__is_active:
            return False

        if not self.check_compliance():
            if not user.check_privileges("admin"):
                return False

        if self.__owner != user.get_safe_info()["username"] \
                and not user.check_privileges("admin"):
            return False

        return True

    def quarantine(self):
        self.__is_active = False

    def get_device_info(self):
        return {
            "device_id": self.__device_id,
            "type": self.__device_type,
            "status": self.__compliance_status,
            "active": self.__is_active
        }


class DeviceManager:

    def __init__(self):
        self.__devices = {}

    def add_device(self, device):
        info = device.get_device_info()
        self.__devices[info["device_id"]] = device

    def remove_device(self, device_id):
        if device_id in self.__devices:
            del self.__devices[device_id]

    def generate_security_report(self):

        report = []

        for device in self.__devices.values():
            device.check_compliance()
            report.append(device.get_device_info())

        return report
