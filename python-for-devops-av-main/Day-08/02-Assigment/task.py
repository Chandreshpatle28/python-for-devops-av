# DevOps script to manage user accounts
# Create an empty list to store user accounts
user_accounts = []

# Add user accounts
user_accounts.append('user1')
user_accounts.append('user2')
user_accounts.append('user3')

# Display the current user accounts
print("Current user accounts:", user_accounts)

# Remove a user account
user_to_remove = 'user2'
if user_to_remove in user_accounts:
    user_accounts.remove(user_to_remove)
    print("User account '{user_to_remove}' removed.")
else:
    print("User account '{user_to_remove}' not found.")

# Update a user account
user_to_update = 'user1'
new_username = 'new_user1'
if user_to_update in user_accounts:
    index = user_accounts.index(user_to_update)
    user_accounts[index] = new_username
    print(f"User account '{user_to_update}' updated to '{new_username}'.")
else:
    print(f"User account '{user_to_update}' not found.")

# Display the final user accounts
print("Final user accounts:", user_accounts)