import streamlit as st
import pandas as pd

# Mosque Data
mosque_data = {
    "Mosque Name": [
        "Jamia Masjid", "Darul Eman 1", "Darul Eman 2", "Darul Eman 3", "Suffah Masjid",
        "Rahmat-E-Alam Western", "Rahmat-E-Alam California", "Raheemiya Masjid", "Darul Hijjrah", "Unity Islamic Center",
        "R&R Learning Center", "Prayer Center of Orland Park"
    ],
    "Isha Iqamah": [
        "8:00 PM", "7:45 PM", "8:45 PM", "1:00 AM", "7:45 PM",
        "7:30 PM", "7:30 PM", "7:30 PM", "8:00 PM", "7:45 PM",
        "8:00 PM", "7:00 PM (No Kids), 8:45 PM (Kids Programs)"
    ],
    "Tarawih Start Time": ["Check Above"] * 12,
    "# Of Days Tarawih Completion": [
        "30 Day", "10 Day", "17 Day (Starting 11th)", "25 Day (Starting 1st)", "8 Day (Starting 1st)",
        "15 Day (Starting 1st) & 6 Day in Basement", "20 Day (Starting 1st) & 24 Day in Basement",
        "6 Day (Starting 1st)", "30 Day (Starting 1st)", "15 Day (Starting 1st)",
        "10 Day (Starting 1st)", ""
    ],
    "Address": [
        "6340 N Campbell Ave, Chicago, IL", "2315 W Devon Ave, Chicago, IL", "2315 W Devon Ave, Chicago, IL",
        "2315 W Devon Ave, Chicago, IL", "3929 Oakton St, Skokie, IL",
        "7045 N Western Ave, Chicago, IL", "6201 N California Ave, Chicago, IL", "2745 W Devon Ave, Chicago, IL",
        "3205 W Bryn Mawr Ave, Chicago, IL", "8944 Austin Ave, Morton Grove, IL",
        "6352 N Campbell Ave, Chicago, IL", "16530 104th Ave, Orland Park, IL"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(mosque_data)

# Streamlit UI
st.set_page_config(page_title="Tarawih Timings", layout="wide")

# Background Styling
st.markdown(
    """
    <style>
        body {
            background-color: #e3f2fd; /* Light Blue */
        }
        .big-title {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: #1a237e; /* Deep Blue */
        }
        .sub-text {
            text-align: center;
            font-size: 14px;
            color: gray;
        }
        .styled-table {
            border-collapse: collapse;
            width: 100%;
            border: 1px solid #ddd;
            font-size: 16px;
        }
        .styled-table th, .styled-table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        .styled-table th {
            background-color: #1a237e;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<p class='big-title'>🕌 Tarawih Prayer Timings in Chicagoland Area</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>After Each Mosque's Isha Salah, Tarawih will follow immediately.</p>", unsafe_allow_html=True)

# Display Table
st.write("### Mosque Timings Table")
st.markdown(df.to_html(classes="styled-table"), unsafe_allow_html=True)

# Search/filter feature
search_query = st.text_input("🔍 **Search Mosque Name:**")
if search_query:
    filtered_df = df[df["Mosque Name"].str.contains(search_query, case=False, na=False)]
    st.markdown(filtered_df.to_html(classes="styled-table"), unsafe_allow_html=True)
