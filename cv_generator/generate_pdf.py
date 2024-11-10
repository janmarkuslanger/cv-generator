from fpdf import FPDF
from data import DataSource
from output import Output


WORDS = {
    "en": {
        "cv": "Curriculum Vitae",
        "personal_info": "Personal Information",
        "name": "Name",
        "birthdate": "Birthdate",
        "birthplace": "Birthplace",
        "title": "Title",
        "address": "Address",
        "street": "Street",
        "city": "City",
        "zip_code": "Zip Code",
        "country": "Country",
        "work_experience": "Work Experience",
        "education": "Education",
        "skills": "Skills",
    },
    "de": {
        "cv": "Lebenslauf",
        "personal_info": "Persönliche Informationen",
        "name": "Name",
        "birthdate": "Geburtsdatum",
        "birthplace": "Geburtsort",
        "title": "Titel",
        "address": "Adresse",
        "street": "Straße",
        "city": "Stadt",
        "zip_code": "Postleitzahl",
        "country": "Land",
        "work_experience": "Berufserfahrung",
        "education": "Ausbildung",
        "skills": "Fähigkeiten",
    },
}



def generate_pdf(data_source: DataSource, output: Output):
    translations = WORDS.get(output.language)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Lebenslauf", 0, 1, "C")
    pdf.ln(10)

    left_x, left_y = 10, 40
    pdf.set_xy(left_x, left_y)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, translations.get("personal_info"), 0, 1)
    pdf.set_font("Arial", "", 10)

    # Persönliche Informationen
    personal_info = data_source.get_personal_info()
    pdf.set_x(left_x)
    pdf.cell(80, 10, f"{translations.get("name")}: {personal_info.firstname} {personal_info.lastname}", 0, 1)
    pdf.set_x(left_x)
    pdf.cell(80, 10, f"{translations.get('birthdate')}: {personal_info.birthdate}", 0, 1)
    if personal_info.birthplace:
        pdf.set_x(left_x)
        pdf.cell(80, 10, f"{translations.get('birthplace')}: {personal_info.birthplace}", 0, 1)
    if personal_info.title:
        pdf.set_x(left_x)
        pdf.cell(80, 10, f"{translations.get('title')}: {personal_info.title}", 0, 1)
    pdf.ln(5)

    # Adresse
    pdf.set_x(left_x)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, translations.get('address'), 0, 1)
    pdf.set_font("Arial", "", 10)
    address = data_source.get_address()
    pdf.set_x(left_x)
    pdf.multi_cell(80, 10, f"{address.street}\n{address.city}, {address.zip_code}\n{address.country}")
    pdf.ln(10)

    # Rechte Spalte: Berufserfahrung und Ausbildung
    right_x, right_y = 110, 40
    pdf.set_xy(right_x, right_y)
    
    # Berufserfahrung
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, translations.get('work_experience'), 0, 1)
    pdf.set_font("Arial", "", 10)
    work_experience = data_source.get_work_experience()
    for job in work_experience:
        end_date = job.end if job.end else "Aktuell"
        pdf.set_x(right_x)
        pdf.multi_cell(80, 10, f"{job.title} \n{job.company}\n({job.start} - {end_date})")
        pdf.ln(3)

    pdf.ln(5)
    pdf.set_x(right_x)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, translations.get('education'), 0, 1)
    pdf.set_font("Arial", "", 10)
    education = data_source.get_education()
    for edu in education:
        graduation_date = edu.graduation_date if edu.graduation_date else ""
        pdf.set_x(right_x)
        pdf.multi_cell(80, 10, f"{edu.degree} von {edu.institution}\n({graduation_date})")
        pdf.ln(3)

    pdf.set_y(240)  # Position weiter unten
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, translations.get('skills'), 0, 1)
    pdf.set_font("Arial", "", 10)
    skills = data_source.get_skills()
    for skill in skills:
        pdf.cell(0, 10, f"- {skill.name}", 0, 1)

    pdf.output(f"{translations.get('cv').lower()}.pdf")
