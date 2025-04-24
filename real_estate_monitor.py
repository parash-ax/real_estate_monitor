import requests
import streamlit as st

# Function to fetch listings from a mock API
def fetch_listings(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise error for bad status codes
        data = response.json()
        
        listings = []
        for item in data:
            listings.append({
                "title": item.get("title", "N/A"),
                "price": f"${item.get('price', 'N/A')}",
                "location": "N/A",  # Mock API has no location
                "link": item.get("image", "#")  # Using image as a mock link
            })
        return listings
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return []

# Streamlit UI
def main():
    st.title("Real Estate Listings (Mock API)")

    # Replace this with a real estate API if you have one
    api_url = st.text_input("Enter API URL:", "https://apilink.com")

    if st.button("Fetch Listings"):
        listings = fetch_listings(api_url)

        if listings:
            for listing in listings:
                st.subheader(listing['title'])
                st.write(f"**Price**: {listing['price']}")
                st.write(f"**Location**: {listing['location']}")
                st.markdown(f"[View Details]({listing['link']})", unsafe_allow_html=True)
                st.markdown("---")
        else:
            st.warning("No listings found.")

if __name__ == "__main__":
    main()
