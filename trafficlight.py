import time

def traffic_light_cycle():
    # Time duration for each light (in seconds)
    green_light_duration = 10
    yellow_light_duration = 3
    red_light_duration = 5

    while True:
        # North-South green light
        print("North-South: GREEN")
        time.sleep(green_light_duration)
        
        print("North-South: YELLOW")
        time.sleep(yellow_light_duration)
        
        print("North-South: RED")
        time.sleep(red_light_duration)
        
        # East-West green light
        print("East-West: GREEN")
        time.sleep(green_light_duration)
        
        print("East-West: YELLOW")
        time.sleep(yellow_light_duration)
        
        print("East-West: RED")
        time.sleep(red_light_duration)

# Run the traffic light cycle
traffic_light_cycle()
