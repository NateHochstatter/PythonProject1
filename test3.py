import json

def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    print(data[0]["ID"])
    data[0]["ID"] = "700000"
    print(data[0]["ID"])
    with open('data.json', 'w') as file:
        json.dump(data, file)
main()