# 🏠 Real Estate Listings Monitor

A Python-based web scraping and monitoring tool that keeps track of property listings from websites. Easily fetch, display, and analyze real estate data in a user-friendly interface using Streamlit.

---

### 🔍 Features

- 🌐 Scrape real estate listings from custom URLs (HTML or live web)
- 🧾 Extract details: Title, Price, Location, and Listing Link
- 🧼 Clean UI using Streamlit
- 📤 Export to CSV for further analysis
- 🕒 Real-time monitoring capability (with periodic run)

---

### 📦 Tech Stack

- Python
- Streamlit
- BeautifulSoup (bs4)
- Requests

---

### 🚀 Installation

git clone https://github.com/parash-ax/real-estate-monitor.git cd real-estate-monitor 
pip install -r requirements.txt


---

### ▶️ Usage

streamlit run real_estate_monitor.py


---

### 🧪 Sample Output

| Title           | Price        | Location         | Link                            |
|----------------|--------------|------------------|---------------------------------|
| 3BHK Apartment | ₹18,00,000   | Bangalore, India | https://example.com/property/1 |

---

### 📁 Folder Structure

real-estate-monitor/
├── real_estate_monitor.py  
├── listings_sample.html  
└── README.md

---

### ✅ To-Do

- Add email notifications for new listings  
- Monitor multiple websites  
- Schedule automatic scraping (via cronjob)

---

