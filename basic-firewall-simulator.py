import random
#small scale basic firewall simulator
#generate random ip addresses, check if blocked

def gen_ip():
    return f"192.168.1.{random.randint(0,255)}"


def main():
    #ip addresses blocked
    block_list = []

    #generate the block list
    for i in range(100):
        block_list.append(gen_ip())

    def check_block_list(ip, list):
        if ip in list:
            return "block"
        
        return "allow"

    #simulate traffic from random ip addresses
    for i in range(30):
        ip_add = gen_ip()
        action = check_block_list(ip_add, block_list)
        rand_num = random.randint(0,9999)
        print(f"IP: {ip_add}, Action: {action}, ID: {rand_num}")

if __name__ == "__main__":
    main()

