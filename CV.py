import streamlit as st
from io import BytesIO

# Try to import reportlab, handle gracefully if not available
try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, ListFlowable, ListItem
    from reportlab.lib.enums import TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    st.warning("⚠️ PDF generation is not available. Please ensure reportlab is installed.")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Antony Best | Data Engineer", layout="wide")

# --- HEADER ---
st.title("👨🏾‍💻 Antony Best")
st.subheader("Data Engineer")
st.write("📧 antony.best@googlemail.com | 📱 07891 664159")
st.markdown("---")

# --- PROFESSIONAL SUMMARY ---
st.header("Professional Summary")
summary_text = """
I specialise in building complex data pipelines that transform raw educational data into actionable business intelligence, 
working extensively with **Snowflake** and **dbt** to create a multi-layered data architecture. 

My technical expertise includes designing sophisticated intermediate models that handle complex joins across student information systems, 
learning management platforms, and video analytics data, ensuring data quality and performance optimisation.

I implement advanced SQL techniques, including window functions and data aggregation strategies, and hold certifications in 
**Snowflake SnowPro** and **Azure AZ-900**, demonstrating a commitment to continuous learning. 

Additionally, I develop and maintain comprehensive data models that support real-time analytics dashboards and API endpoints, 
enabling stakeholders to access critical insights for student success and institutional decision-making.
"""
st.write(summary_text)
st.markdown("---")

# --- WORK EXPERIENCE ---
st.header("Work Experience")

experience = [
    {
        "role": "Lead Business Intelligence Learner Analytics Developer | University of Birmingham UK (04/2024 – Present)",
        "details": [
            "Designed, built, and optimised end-to-end data platforms using Snowflake, Azure Data Factory, and dbt.",
            "Delivered scalable ELT solutions integrating multiple data systems into a unified warehouse.",
            "Built Azure Functions integrating with APIM APIs for cloud-native automation.",
            "Proficient in Python, SQL, Terraform, CI/CD, and version control.",
            "Collaborated with architects, analysts, and stakeholders to deliver data strategies aligned with business goals.",
        ]
    },
    {
        "role": "Data Engineer | Capgemini UK (05/2023 – 04/2024)",
        "details": [
            "Processed XML data in AWS Glue, loading structured data into AWS and metadata into Snowflake.",
            "Developed Python scripts for file validation, batch IDs, and Snowflake integration.",
        ]
    },
    {
        "role": "Data Specialist | Capgemini UK (05/2023 – 08/2023)",
        "details": [
            "Used SQL (SSM) for DataLake extractions and report generation.",
            "Created SSRS and Power BI reports for reconciliation and analysis.",
        ]
    },
    {
        "role": "DataOps | Capgemini UK (02/2023 – 04/2023)",
        "details": [
            "Connected to ClickHouse via Docker OCS.",
            "Modelled data from unstructured sources and visualised API calls using Insomnia and DBeaver.",
        ]
    },
    {
        "role": "Data Engineering / Developer / Tester | Capgemini UK (02/2022 – 01/2023)",
        "details": [
            "Migrated SAS solutions to PySpark and BigQuery.",
            "Used Databricks, Airflow, and GCP for ETL orchestration.",
            "Implemented AI (GPT3) for code testing and reconciliation.",
        ]
    },
    {
        "role": "Data Analyst | Self Employed (09/2020 – 01/2022)",
        "details": [
            "Analysed CSV data using Python, Pandas, Seaborn, and Matplotlib to visualise insights.",
        ]
    },
]

for job in experience:
    with st.expander(f"💼 {job['role']}"):
        for line in job["details"]:
            st.markdown(f"- {line}")

st.markdown("---")

# --- SKILLS ---
skills = [
    "Snowflake", "dbt", "Azure Data Factory", "Python", "SQL",
    "Terraform", "Azure Functions", "APIM", "AWS Glue", "Power BI",
    "Airflow", "Databricks", "GCP", "BigQuery", "Git / CI-CD"
]
st.header("Skills")
cols = st.columns(4)
for i, skill in enumerate(skills):
    with cols[i % 4]:
        st.markdown(f"- {skill}")
st.markdown("---")

# --- EDUCATION & CERTIFICATIONS ---
education_text = """
🎓 **BSc (Hons) in Audio Systems Design**, University of Derby  

📜 **Certifications:**  
- Snowflake SnowPro Core Certified  
- Microsoft Certified Azure Fundamentals (AZ-900)  
- Python PCAP Certified  
- BigQuery Basics (Coursera)  
- SAS & PySpark Certificates (Coursera)
"""
st.header("Education & Certifications")
st.write(education_text)
st.markdown("---")

# --- HOBBIES ---
hobbies_text = """
🎶 Music  
🎾 Tennis  
🧠 Learning new skills and AI technologies  
💡 Exploring new data tools and innovations
"""
st.header("Hobbies & Interests")
st.write(hobbies_text)
st.markdown("---")

# --- PDF GENERATION (TWO-COLUMN LAYOUT) ---
if REPORTLAB_AVAILABLE:
    pdf_buffer = BytesIO()

    doc = BaseDocTemplate(pdf_buffer, pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    # Enhanced styling for better visual appeal
    styles.add(ParagraphStyle(name='CVTitle', fontSize=18, leading=22, spaceAfter=12, fontName='Helvetica-Bold', textColor='#2c3e50'))
    styles.add(ParagraphStyle(name='CVSectionHeader', fontSize=14, leading=18, spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold', textColor='#34495e'))
    styles.add(ParagraphStyle(name='CVBody', fontSize=10, leading=14, spaceAfter=6, fontName='Helvetica'))
    styles.add(ParagraphStyle(name='CVListItem', fontSize=10, leading=12, leftIndent=20, fontName='Helvetica'))
    styles.add(ParagraphStyle(name='CVContact', fontSize=10, leading=12, spaceAfter=8, fontName='Helvetica', textColor='#7f8c8d'))
    styles.add(ParagraphStyle(name='CVJobTitle', fontSize=11, leading=14, spaceAfter=4, fontName='Helvetica-Bold', textColor='#2c3e50'))
    styles.add(ParagraphStyle(name='CVCompany', fontSize=10, leading=12, spaceAfter=6, fontName='Helvetica', textColor='#7f8c8d'))

    # Define two-column layout
    frame_left = Frame(doc.leftMargin, doc.bottomMargin, (A4[0] - 100) / 2, A4[1] - 100, id='left')
    frame_right = Frame(doc.leftMargin + (A4[0] / 2), doc.bottomMargin, (A4[0] - 100) / 2, A4[1] - 100, id='right')
    doc.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame_left, frame_right])])

    story = []

    # LEFT COLUMN: Summary + Experience + Education
    story.append(Paragraph("Antony Best", styles['CVTitle']))
    story.append(Paragraph("Data Engineer", styles['CVSectionHeader']))
    story.append(Paragraph("📧 antony.best@googlemail.com", styles['CVContact']))
    story.append(Paragraph("📱 07891 664159", styles['CVContact']))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Professional Summary", styles['CVSectionHeader']))
    story.append(Paragraph(summary_text, styles['CVBody']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Work Experience", styles['CVSectionHeader']))
    for job in experience:
        # Split role and company/date
        role_parts = job['role'].split(' | ')
        if len(role_parts) == 2:
            role_title = role_parts[0]
            company_date = role_parts[1]
        else:
            role_title = job['role']
            company_date = ""
        
        story.append(Paragraph(role_title, styles['CVJobTitle']))
        if company_date:
            story.append(Paragraph(company_date, styles['CVCompany']))
        story.append(ListFlowable(
            [ListItem(Paragraph(item, styles['CVListItem'])) for item in job["details"]],
            bulletType='bullet'
        ))
        story.append(Spacer(1, 10))

    story.append(Paragraph("Education & Certifications", styles['CVSectionHeader']))
    
    # Education section with proper formatting
    story.append(Paragraph("<b>BSc (Hons) in Audio Systems Design</b>", styles['CVBody']))
    story.append(Paragraph("University of Derby", styles['CVBody']))
    story.append(Spacer(1, 8))
    
    story.append(Paragraph("<b>Certifications:</b>", styles['CVBody']))
    certifications = [
        "Snowflake SnowPro Core Certified",
        "Microsoft Certified Azure Fundamentals (AZ-900)",
        "Python PCAP Certified",
        "BigQuery Basics (Coursera)",
        "SAS & PySpark Certificates (Coursera)"
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(cert, styles['CVListItem'])) for cert in certifications],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 12))

    # RIGHT COLUMN: Skills + Hobbies
    story.append(Paragraph("Skills", styles['CVSectionHeader']))
    # Format skills in a more readable way
    skills_text = " • ".join(skills)
    story.append(Paragraph(skills_text, styles['CVBody']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Hobbies & Interests", styles['CVSectionHeader']))
    # Clean up hobbies text for better formatting
    hobbies_clean = hobbies_text.replace("🎶 ", "").replace("🎾 ", "").replace("🧠 ", "").replace("💡 ", "")
    story.append(Paragraph(hobbies_clean, styles['CVBody']))

    doc.build(story)
    pdf_buffer.seek(0)

    # --- DOWNLOAD BUTTON ---
    st.download_button(
        label="📥 Download My Two-Column CV (PDF)",
        data=pdf_buffer,
        file_name="Antony_Best_TwoColumn_CV.pdf",
        mime="application/pdf",
    )
else:
    st.info("💡 PDF download will be available once the app is deployed with the requirements.txt file.")