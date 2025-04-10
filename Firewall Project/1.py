import random
from ipaddress import ip_address

def generate_random_ip():
    return f"192.168.1.{random.randint(1, 20)}"
#__name là một biến đặc biệt chứa tên mô đun hiện tại, khi chạy file py thì __name__ sẽ có gía trị là __main__
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"
def main():
    firewall_rules = {
        "192.168.1.1" : "block",
        "192.168.1.4" : "block",
        "192.168.1.9" : "block",
        "192.168.1.13" : "block",
        "192.168.1.16" : "block",
        "192.168.1.19" : "block",
    }
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999) #example when we take mutiple action against the same Source IP, to be able to distinguish between the different instances of those actions
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}") #print to the terminal the IP address and the packet that was analyzed the action taken against that IP address and the random unique identifying number
        #f"..." : đây là f-string, một cách format chuỗi trong Python giúp chèn thêm giá trị của biến trực tiếp vào chuỗi
if __name__ == "__main":
    main()