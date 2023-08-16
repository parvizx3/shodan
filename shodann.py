import shodan, os

# Initialize Shodan API client
api_keys = str(os.environ.get("TOKEN")).split(" ")


# Define the search query
query = os.environ.get("QUERY")

# Function to retrieve server addresses from search results
def get_server_addresses(results):
    server_addresses = []
    for result in results['matches']:
        server_addresses.append(result['ip_str'])
    return server_addresses
for api_key in api_keys:
    print(api_key)
    try:
        # Get the first 2 pages of search results
        api = shodan.Shodan(api_key)
        for page in range(1, 3):
                # Perform the search
            results = api.search(query, page=page)
        
                # Get server addresses from the current page
            server_addresses = get_server_addresses(results)
                
                # Print server addresses
            print(f"Page {page} - Server Addresses:")
            for address in server_addresses:
                print(address)
            print()
    
    except shodan.APIError as e:
        print('Error: {}'.format(e))
