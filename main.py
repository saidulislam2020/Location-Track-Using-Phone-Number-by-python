from opencage.geocoder import OpencageGeocode
from phonenumbers import carrier
import phonenumbers
import opencage

from phonenumber import number

from phonenumbers import geocoder
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
# print(location)
srvice_pro = phonenumbers.parse(number)
print(carrier.name_for_number(srvice_pro, "en"))

key = '44546cd4278b4f5cbbb9eb5beef16067'

geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)
print(results)
