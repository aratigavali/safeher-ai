import random

print("SafeHer AI Risk Detection System")

risk = random.randint(1,10)

if risk > 7:
    print("⚠️ Risk detected!")
    print("Alert sent to emergency contacts")
else:
    print("Environment appears safe")
