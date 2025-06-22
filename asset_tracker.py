import pandas as pd

# Load CSV data
asset_data.csv = "https://1drv.ms/f/c/876ee016f06d9783/EvnFM1N9NGdAlXixhhknQnIBjqxMXofXKFCChEmGYUcErg?e=dmrtLM"
df = pd.read_csv('asset_data.csv')

def show_assets():
    print("\nAll Assets:\n")
    print(df)

def filter_by_status(status):
    print(f"\nAssets with status '{status}':\n")
    print(df[df['Status'].str.lower() == status.lower()])

def update_status(asset_id, new_status):
    global df
    df.loc[df['Asset ID'] == asset_id, 'Status'] = new_status
    df.to_csv('asset_data.csv', index=False)
    print(f"Updated {asset_id} to status '{new_status}'.")

while True:
    print("\n--- IT Asset Tracker ---")
    print("1. View All Assets")
    print("2. Filter by Status")
    print("3. Update Asset Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_assets()
    elif choice == '2':
        status = input("Enter status to filter (e.g., Available, Under Repair): ")
        filter_by_status(status)
    elif choice == '3':
        aid = input("Enter Asset ID: ")
        new_status = input("Enter New Status: ")
        update_status(aid, new_status)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Try again.")
