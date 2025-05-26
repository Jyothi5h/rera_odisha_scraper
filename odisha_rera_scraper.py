#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[10]:


options = Options()
# Comment out headless for debugging; uncomment later if needed
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://rera.odisha.gov.in/projects/project-list"
driver.get(url)


# In[11]:


# Wait until "View Details" buttons are loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//a[contains(text(),'View Details')]"))
)


# In[12]:


view_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'View Details')]")
print(f"Found {len(view_buttons)} 'View Details' buttons")

project_data = []

for idx in range(min(6, len(view_buttons))):
    try:
        button = view_buttons[idx]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, -200);")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)

        def get_text_by_label(label):
            try:
                container = driver.find_element(By.XPATH, f"//*[contains(text(),'{label}')]/ancestor::div[contains(@class, 'card-body')]")
                value = container.find_element(By.XPATH, f".//*[contains(text(),'{label}')]/following-sibling::*[1]").text.strip()
                return value
            except:
                return "N/A"

        rera_no = get_text_by_label("RERA Regd. No")
        project_name = get_text_by_label("Project Name")

        try:
            promoter_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Promoter Details')]")
            driver.execute_script("arguments[0].click();", promoter_tab)
            time.sleep(2)
        except:
            pass

        promoter_name = get_text_by_label("Company Name")
        promoter_address = get_text_by_label("Registered Office Address")
        gst_no = get_text_by_label("GST No")

        project_data.append({
            "RERA Regd. No": rera_no,
            "Project Name": project_name,
            "Promoter Name": promoter_name,
            "Promoter Address": promoter_address,
            "GST No": gst_no
        })

        driver.back()

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[contains(text(),'View Details')]"))
        )
        time.sleep(2)

        view_buttons = driver.find_elements(By.XPATH, "//a[contains(text(),'View Details')]")

    except Exception as e:
        print(f"Error scraping project {idx + 1}: {e}")
        continue

driver.quit()


# In[13]:


# Print the results
for i, proj in enumerate(project_data, start=1):
    print(f"Project {i}")
    for key, val in proj.items():
        print(f"{key}: {val}")
    print("-" * 40)


# In[ ]:




