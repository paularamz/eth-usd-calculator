def user_eth():
    eth = float(input("How much ETH do you own?"))
    return eth * 1948

def main():
    total_value = user_eth()
    print(f"You own {total_value:,.2f} USD")

main()