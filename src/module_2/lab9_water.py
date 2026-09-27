# Refer to this module's readme
from soil import sample

def main():
    moisture = sample()
    days = 0
    while moisture > 20:
        moisture = sample()
        print(f"Day {days}: Moisture is {moisture}%.")
        days += 1

    print("Time to water!")

main()