import streamlit as st
import pandas as pd

# Mosque Data (Fill in the rest)
mosque_data = {
    "Mosque Name": [
        "Jamia Masjid", "Darul Eman", "Mosque 3", "Mosque 4", "Mosque 5",  # Fill in other names
        "Mosque 6", "Mosque 7", "Mosque 8", "Mosque 9", "Mosque 10",
        "Mosque 11", "Mosque 12", "Mosque 13", "Mosque 14", "Mosque 15",
        "Mosque 16", "Mosque 17", "Mosque 18", "Mosque 19", "Mosque 20",
        "Mosque 21", "Mosque 22", "Mosque 23", "Mosque 24", "Mosque 25",
        "Mosque 26", "Mosque 27", "Mosque 28", "Mosque 29", "Mosque 30",
        "Mosque 31", "Mosque 32", "Mosque 33", "Mosque 34", "Mosque 35"
    ],
    "Isha Iqamah": [
        "8:00 PM", "7:45 PM", "", "", "",  # Fill in other times
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", ""
    ],
    "Tarawih Start Time": [
        "Tarawih followed immediately after Isha salah" for _ in range(35)
    ],
    "# Of Days Tarawih Completion": [
        "30 Day", "10 Day", "", "", "",  # Fill in other values
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", ""
    ],
    "Address": [
        "6340 N Campbell Ave, Chicago, IL",
        "2315 W Devon Ave, Chicago, IL",
        "", "", "",  # Fill in other addresses
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", "",
        "", "", "", "", ""
    ]
}

# Convert to DataFrame
df = pd.DataFrame(mosque_data)

# Streamlit UI
st.set_page_config(page_title="Tarawih Timings", layout="wide")  # Better layout
st.title("🕌 Tarawih Prayer Timings in Chicagoland Area")
st.write("Scroll through the table to find your mosque's Tarawih timing.")

# Display interactive table
st.dataframe(df, height=600)

# Search/filter feature
search_query = st.text_input("🔍 Search Mosque Name:")
if search_query:
    filtered_df = df[df["Mosque Name"].str.contains(search_query, case=False, na=False)]
    st.dataframe(filtered_df, height=400)
