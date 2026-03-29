import requests

def scan_channel():
    print("=== Fan Detector Client ===")
    channel = input("Enter YouTube channel link: ")

    if not channel.strip():
        print("No link provided.")
        return

    try:
        # Change this URL to your actual backend later
        url = "http://localhost:5000/scan"

        response = requests.post(url, json={"channel": channel})

        if response.status_code == 200:
            data = response.json()
            print("\n=== Scan Results ===")
            print(f"Fans Detected: {data.get('fans')}")
            print(f"Super Fans: {data.get('superfans')}")
        else:
            print("Error:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("Could not connect to server.")
        print("Make sure your backend (app.py) is running!")

if __name__ == "__main__":
    scan_channel()
