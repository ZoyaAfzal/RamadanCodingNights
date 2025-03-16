'''import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Configure the Streamlit Page
st.set_page_config(page_title="Time Zone Converter", page_icon="🌍", layout="wide")

# Define Time Zones
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo",
    "Australia/Sydney", "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata"
]

# Apply Custom CSS for a Professional Look
st.markdown("""
    <style>
        .main {
            background-color: #F5F5F5;
        }
        .stApp {
            color: #333;
        }
        .big-font {
            font-size:18px !important;
            font-weight: 600;
            color: #1E88E5;
        }
        .time-card {
            background: white;
            padding: 10px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .stButton>button {
            width: 100%;
            background: #1E88E5;
            color: white;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background: #1565C0;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🌍 Time Zone Converter")
st.markdown("Convert time across different time zones easily with a professional and intuitive interface.")

# Sidebar for Selection
st.sidebar.header("📌 Select Timezones to Display")
selected_timezone = st.sidebar.multiselect(
    "Choose Timezones:", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

st.sidebar.markdown("---")

# Time Display Section
st.subheader("⏳ Live Time in Selected Timezones")
cols = st.columns(len(selected_timezone))

for i, tz in enumerate(selected_timezone):
    current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I:%M:%S %p')
    with cols[i]:
        st.markdown(f"<div class='time-card'><h4 class='big-font'>{tz}</h4><p>{current_time}</p></div>", unsafe_allow_html=True)

st.markdown("---")

# Time Conversion Section
st.subheader("🔄 Convert Time Between Timezones")

# Layout Optimization
col1, col2 = st.columns(2)

with col1:
    from_tz = st.selectbox("🌎 From Timezone", TIME_ZONES, index=0)
    to_tz = st.selectbox("🌍 To Timezone", TIME_ZONES, index=1)

with col2:
    current_time = st.time_input("🕒 Select Time", value=datetime.now().time())

# Convert Time Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔁 Convert Time"):
        try:
            dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
            converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I:%M:%S %p')
            st.success(f"✅ Converted Time in {to_tz}: {converted_time}")
        except Exception as e:
            st.warning("⚠️ Error converting time. Please check your input.")

# Footer
st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("📌 Built with ❤️ using Streamlit | Designed for professionals")
'''
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Configure the Streamlit Page
st.set_page_config(page_title="Time Zone Converter", page_icon="🌍", layout="wide")

# Define Time Zones
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Europe/London", "Asia/Tokyo",
    "Australia/Sydney", "America/Los_Angeles", "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata"
]

# Apply Dark Theme Using Markdown
st.markdown(
    """
    <style>
        /* Global dark background */
        body, .main, .stApp {
            background-color: #121212 !important;
            color: white !important;
        }
        .stText, .stMarkdown, .stRadio label, .stSelectbox label, .stCheckbox label {
            color: white !important;
        }
        .stSelectbox, .stMultiSelect div[data-baseweb="tag"] {
        color: white !important;
        }
        /* Fix placeholder text color */
        input::placeholder, textarea::placeholder, .stMultiSelect input {
        color: white !important;
        opacity: 1 !important;
        }

        /* Fix labels and text */
        .stTextInput label, .stSelectbox label, .stMultiSelect label {
        color: white !important;
        }

        /* Fix placeholder text color */
        input::placeholder, textarea::placeholder, .stMultiSelect input {
        color: white !important;
        opacity: 1 !important;
        }
        /* Sidebar dark theme */
        section[data-testid="stSidebar"] {
            background-color: #181818 !important;
            color: white !important;
        }
        /* Fix labels and text */
        .stTextInput label, 
        .stSelectbox label, 
        .stMultiSelect label, 
        .stTimeInput label {
        color: white !important;
        }

        /* Navbar (Top Bar) */
        header {
            background: #181818 !important;
        }

        /* Headers and Text */
        .stTitle, .stHeader, .stSubheader, .stMarkdown, h1, h2, h3, h4 {
            color: white !important;
        }

        /* Cards */
        .time-card {
            background: #1E1E1E;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
            text-align: center;
            color: white;
        }

        /* Select Boxes & Buttons */
        .stSelectbox, .stTimeInput, .stButton>button {
            border-radius: 8px !important;
            background: #333 !important;
            color: white !important;
        }

        /* Sidebar widgets */
        .stMultiSelect, .stTextInput, .stNumberInput {
            background: #252525 !important;
            color: white !important;
            border-radius: 8px !important;
        }

        /* Button Styling */
        .stButton>button {
            width: 100%;
            background: #1E90FF !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
        }

        .stButton>button:hover {
            background: #3700B3 !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("🌍 Time Zone Converter")
st.markdown("Easily convert time across different time zones with a sleek dark mode UI.")

# Sidebar for Selection
st.sidebar.header("⏰ Select Timezones to Display")
selected_timezone = st.sidebar.multiselect(
    "Choose Timezones:", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

st.sidebar.markdown("---")

# Time Display Section
st.subheader("⌚ Live Time in Selected Timezones")
cols = st.columns(len(selected_timezone))

for i, tz in enumerate(selected_timezone):
    current_time = datetime.now(ZoneInfo(tz)).strftime('%Y-%m-%d %I:%M:%S %p')
    with cols[i]:
        st.markdown(f"<div class='time-card'><h4>{tz}</h4><p>{current_time}</p></div>", unsafe_allow_html=True)

st.markdown("---")

# Time Conversion Section
st.subheader("🔄 Convert Time Between Timezones")

# Layout Optimization - Aligning Inputs in One Row
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    from_tz = st.selectbox("🌎 From Timezone", TIME_ZONES, index=0)

with col2:
    current_time = st.time_input("🕒 Select Time", value=datetime.now().time())

with col3:
    to_tz = st.selectbox("🌍 To Timezone", TIME_ZONES, index=1)

# Convert Time Button - Centered
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🔁 Convert Time"):
        try:
            dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
            converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime('%Y-%m-%d %I:%M:%S %p')
            st.success(f"✅ Converted Time in {to_tz}: {converted_time}")
        except Exception as e:
            st.warning("⚠️ Error converting time. Please check your input.")

