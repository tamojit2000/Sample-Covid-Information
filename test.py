from cowin_api import CoWinAPI
from pprint import pprint
cowin = CoWinAPI()

pin_code = "700054"

available_centers = cowin.get_availability_by_pincode(pin_code)
print("All Available Centers [ By Pincode ] : ")
pprint(available_centers)
