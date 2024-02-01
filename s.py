import requests

file = "proxy.txt"
with open(file, "w", encoding="utf-8") as f:
    f.write(requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text)

with open(file, "r") as f:
    lines = f.read().splitlines()

print("Scraped",len(lines))