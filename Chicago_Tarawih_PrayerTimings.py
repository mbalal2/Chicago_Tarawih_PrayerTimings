import streamlit as st
import pandas as pd

# Updated Mosque Data
mosque_data = {
    "Mosque #": list(range(1, 24)),  # Mosque numbers starting from 1
    "Mosque Name": [
        "Jamia Masjid", "Darul Eman 1", "Darul Eman 2", "Darul Eman 3", "Suffah Masjid",
        "Rahmat-E-Alam Western", "Rahmat-E-Alam California", "Raheemiya Masjid", "Darul Hijjrah", "Unity Islamic Center",
        "R&R Learning Center", "Prayer Center of Orland Park", "MEC", "MCC", "Masjid DarusSalam", "NEIU MSA", "Masjid Noor",
        "UIC MSA", "ICC", "DIC", "Islamic Oasis Center & Mosque", "Islamic Foundation Villa Park", "ICNA Center Oak Brook"
    ],
    "Isha Iqamah/ Tarawih Starts Immediately After": [
        "8:00 PM", "7:45 PM", "8:45 PM", "1:00 AM", "7:45 PM",
        "7:30 PM", "7:30 PM", "7:30 PM", "8:00 PM", "7:45 PM",
        "8:00 PM", "7:00 PM (No Kids), 8:45 PM (Kids Programs)", "8:00 PM", "7:45 PM",
        "7:30 PM", "7:30 PM", "8:00 PM", "8:15 PM", "7:30 PM", "8:00 PM",
        "7:00 PM", "7:30 PM", "8:00 PM"
    ],
    "# Of Days Tarawih Completion": [
        "29 Day (Starting 1st)", "10 Day (Starting 1st)", "17 Day (Starting 11th)", "25 Day (Starting 1st)", "8 Day (Starting 1st)",
        "15 Day (Starting 1st) & 6 Day in Basement", "20 Day (Starting 1st) & 24 Day in Basement",
        "6 Day (Starting 1st)", "29 Day (Starting 1st)", "15 Day (Starting 1st)",
        "10 Day (Starting 1st)", "29 Day (Starting 1st)", "27 Day (Starting 1st)", "27 Day (Starting 1st)",
        "29 Day in Main Hall (Starting 1st), 7 Day in Gym (Starting 1st)", "29 Day Mon-Thurs",
        "10 Day Upstairs (Starting 1st), 27 Day in Basement (Starting 1st)", "29 Day (Starting 3rd)",
        "29 Day (Starting 1st)", "29 Day (Starting 1st)", "29 Day (Starting 1st)",
        "29 Day (Starting 1st)", "27 Day (Starting 1st)"
    ],
    "Address": [
        "6340 N Campbell Ave, Chicago, IL", "2315 W Devon Ave, Chicago, IL", "2315 W Devon Ave, Chicago, IL",
        "2315 W Devon Ave, Chicago, IL", "3929 Oakton St, Skokie, IL",
        "7045 N Western Ave, Chicago, IL", "6201 N California Ave, Chicago, IL", "2745 W Devon Ave, Chicago, IL",
        "3205 W Bryn Mawr Ave, Chicago, IL", "8944 Austin Ave, Morton Grove, IL",
        "6352 N Campbell Ave, Chicago, IL", "16530 104th Ave, Orland Park, IL", "8601 Menard Ave, Morton Grove, IL", "4380 N Elston Ave, Chicago, IL",
        "21W525 North Ave, Lombard, IL", "5500 N St Louis Ave, Chicago, IL (SU 219)", "6151 N Greenview Ave, Chicago, IL",
        "750 S Halsted St, Chicago, IL (SCE 713)", "5933 N Lincoln Ave, Chicago, IL", "231 S State St #4, Chicago, IL (5th Floor)",
        "4201 N Monticello Ave, Chicago, IL", "300 W Highridge Rd, Villa Park, IL", "1S270 Summit Ave, Oakbrook Terrace, IL"
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
        .author-text {
            text-align: right;
            font-size: 12px;
            color: black;
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

# Title & Subtitles
st.markdown("<p class='big-title'>🕌 Tarawih Prayer Timings in Chicagoland Area</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-style:italic; font-size:18px;'>بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:16px; font-weight:bold; color:red;'>**Please note, March 9th is Daylight Savings, hence timings may alter. Prayer timings are subject to change.**</p>", unsafe_allow_html=True)
st.markdown("<p class='author-text'>Author: Balal</p>", unsafe_allow_html=True)

# Display Table
st.write("### Mosque Timings Table")
st.markdown(df.to_html(classes="styled-table", index=False), unsafe_allow_html=True)

# Enhanced Search Feature
search_query = st.text_input("🔍 **Search Anything:**")

if search_query:
    # Convert all columns to string and search across the whole dataset
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]
    if not filtered_df.empty:
        st.markdown(filtered_df.to_html(classes="styled-table", index=False), unsafe_allow_html=True)
    else:
        st.write("❌ No results found. Try a different search term.")
