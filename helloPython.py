from pyaare.pyaare import PyAare

aare = PyAare(city="Bern")
print(aare.tempC)
print(aare.tempText)
print(aare.flow)
print(aare.flowText)

aare.refresh()        # get the newest data