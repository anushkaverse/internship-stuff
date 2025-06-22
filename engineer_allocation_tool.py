import pandas as pd
from datetime import datetime


# Load the engineer dataset
engineers_df = pd.read_csv('engineers.csv')
engineers_df.columns = engineers_df.columns.str.strip()



# Display all engineers
def view_all_engineers():
    print("\n--- Engineer List ---")
    print(engineers_df)


# Filter available engineers by optional criteria
def filter_engineers(skill_level=None, location=None, specialization=None):
    filtered = engineers_df.copy()

    if skill_level:
        filtered = filtered[filtered['Skill Level'].str.lower() == skill_level.lower()]
    if location:
        filtered = filtered[filtered['Location'].str.lower() == location.lower()]
    if specialization:
        filtered = filtered[filtered['Specialization'].str.lower() == specialization.lower()]


    # Only show available engineers
    filtered = filtered[filtered['Available'].str.lower() == 'yes']

    print("\n--- Available Engineers Matching Criteria ---\n")
    print(filtered)


# Allocate an engineer to a client and update records
def allocate_engineer(engineer_id, client_name):
    global engineers_df
    match = engineers_df[engineers_df['Engineer ID'] == engineer_id]


    if not match.empty and match.iloc[0]['Available'] == 'Yes':

        # Mark engineer as unavailable
        engineers_df.loc[match.index[0], 'Available'] = 'No'
        engineers_df.to_csv('engineers.csv', index=False)


        # Log the allocation
        allocation_log = {
            'Engineer ID': engineer_id,
            'Name': match.iloc[0]['Name'],
            'Client Name': client_name,
            'Date of Allocation': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        try:
            log_df = pd.read_csv('allocation_log.csv')
            log_df = pd.concat([log_df, pd.DataFrame([allocation_log])], ignore_index=True)
        except FileNotFoundError:
            log_df = pd.DataFrame([allocation_log])

        log_df.to_csv('allocation_log.csv', index=False)
        print(f"\n Engineer {engineer_id} allocated to {client_name}. Log updated.")
    else:
        print("\n⚠️ Engineer not found or not available.")


# Main CLI loop
while True:
    print("\n=== Engineer Allocation Tool ===")
    print("1. View All Engineers")
    print("2. Filter Engineers")
    print("3. Allocate Engineer to Client")
    print("4. Exit")

    user_choice = input("Enter your choice: ").strip()

    if user_choice == '1':
        view_all_engineers()
    elif user_choice == '2':
        level = input("Enter Skill Level (L1/L2/L3) or leave blank: ")
        city = input("Enter Location or leave blank: ")
        tech = input("Enter Specialization (e.g., Networking, Python) or leave blank: ")
        filter_engineers(skill_level=level or None, location=city or None, specialization=tech or None)
    elif user_choice == '3':
        eng_id = input("Enter Engineer ID to allocate: ").strip()
        client = input("Enter Client Name: ").strip()
        allocate_engineer(eng_id, client)
    elif user_choice == '4':
        print("\nExiting the tool. Goodbye!\n")
        break
    else:
        print("Invalid choice. Please try again.")
