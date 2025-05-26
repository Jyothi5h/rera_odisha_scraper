# rera_odisha_scraper

This Python script scrapes the first 6 projects listed under the **"Projects Registered"** section on the [Odisha RERA website](https://rera.odisha.gov.in/projects/project-list).

It collects the following details from each project's "View Details" page:

- RERA Regd. No
- Project Name
- Promoter Name (Company Name under Promoter Details tab)
- Promoter Address (Registered Office Address under Promoter Details tab)
- GST No

---

## Files

- `odisha_rera_scraper.py` — The main script that performs the scraping.
- `requirements.txt` — Python dependencies needed to run the script.

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Jyothi5h/rera_odisha_scraper.git
cd rera-odisha-scraper
