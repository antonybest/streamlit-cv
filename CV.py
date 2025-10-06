import streamlit as st
from io import BytesIO
from datetime import datetime

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

    doc = BaseDocTemplate(pdf_buffer, pagesize=A4, leftMargin=30, rightMargin=30, topMargin=30, bottomMargin=30)
    styles = getSampleStyleSheet()
    
    # Enhanced professional styling
    styles.add(ParagraphStyle(name='CVTitle', fontSize=20, leading=24, spaceAfter=8, fontName='Helvetica-Bold', textColor='#1a365d', alignment=1))
    styles.add(ParagraphStyle(name='CVSubtitle', fontSize=14, leading=16, spaceAfter=12, fontName='Helvetica', textColor='#2d3748', alignment=1))
    styles.add(ParagraphStyle(name='CVSectionHeader', fontSize=13, leading=16, spaceAfter=6, spaceBefore=12, fontName='Helvetica-Bold', textColor='#2b6cb0', borderWidth=0, borderColor='#2b6cb0', borderPadding=2))
    styles.add(ParagraphStyle(name='CVBody', fontSize=10, leading=12, spaceAfter=4, fontName='Helvetica', textColor='#2d3748'))
    styles.add(ParagraphStyle(name='CVListItem', fontSize=9, leading=11, leftIndent=18, fontName='Helvetica', textColor='#4a5568'))
    styles.add(ParagraphStyle(name='CVContact', fontSize=10, leading=12, spaceAfter=6, fontName='Helvetica', textColor='#718096', alignment=1))
    styles.add(ParagraphStyle(name='CVJobTitle', fontSize=11, leading=13, spaceAfter=2, fontName='Helvetica-Bold', textColor='#1a365d'))
    styles.add(ParagraphStyle(name='CVCompany', fontSize=9, leading=11, spaceAfter=4, fontName='Helvetica', textColor='#718096', fontStyle='italic'))
    styles.add(ParagraphStyle(name='CVSummary', fontSize=9, leading=11, spaceAfter=6, fontName='Helvetica', textColor='#2d3748'))
    styles.add(ParagraphStyle(name='CVSkills', fontSize=9, leading=11, spaceAfter=4, fontName='Helvetica', textColor='#4a5568'))
    styles.add(ParagraphStyle(name='CVCert', fontSize=9, leading=11, spaceAfter=2, fontName='Helvetica', textColor='#2d3748'))

    # Define two-column layout with more space
    frame_left = Frame(doc.leftMargin, doc.bottomMargin, (A4[0] - 60) / 2, A4[1] - 60, id='left')
    frame_right = Frame(doc.leftMargin + (A4[0] - 60) / 2 + 10, doc.bottomMargin, (A4[0] - 60) / 2, A4[1] - 60, id='right')
    doc.addPageTemplates([PageTemplate(id='TwoCol', frames=[frame_left, frame_right])])

    story = []

    # LEFT COLUMN: Summary + Experience + Education
    story.append(Paragraph("ANTONY BEST", styles['CVTitle']))
    story.append(Paragraph("Data Engineer", styles['CVSubtitle']))
    story.append(Paragraph("📧 antony.best@googlemail.com  |  📱 07891 664159", styles['CVContact']))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Professional Summary", styles['CVSectionHeader']))
    story.append(Paragraph(summary_text, styles['CVSummary']))
    story.append(Spacer(1, 8))

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
        story.append(Spacer(1, 8))

    story.append(Paragraph("Education & Certifications", styles['CVSectionHeader']))
    
    # Education section with proper formatting
    story.append(Paragraph("<b>BSc (Hons) in Audio Systems Design</b>", styles['CVBody']))
    story.append(Paragraph("University of Derby", styles['CVCompany']))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("<b>Professional Certifications:</b>", styles['CVBody']))
    certifications = [
        "Snowflake SnowPro Core Certified",
        "Microsoft Certified Azure Fundamentals (AZ-900)",
        "Python PCAP Certified",
        "BigQuery Basics (Coursera)",
        "SAS & PySpark Certificates (Coursera)"
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(cert, styles['CVCert'])) for cert in certifications],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 8))

    # RIGHT COLUMN: Skills + Additional Experience + Hobbies
    story.append(Paragraph("Technical Skills", styles['CVSectionHeader']))
    # Format skills in categories for better readability
    core_skills = "Snowflake • dbt • Azure Data Factory • Python • SQL"
    cloud_skills = "Terraform • Azure Functions • APIM • AWS Glue • Power BI"
    tools_skills = "Airflow • Databricks • GCP • BigQuery • Git / CI-CD"
    
    story.append(Paragraph("<b>Core Technologies:</b>", styles['CVSkills']))
    story.append(Paragraph(core_skills, styles['CVSkills']))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Cloud & Tools:</b>", styles['CVSkills']))
    story.append(Paragraph(cloud_skills, styles['CVSkills']))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Data Platforms:</b>", styles['CVSkills']))
    story.append(Paragraph(tools_skills, styles['CVSkills']))
    story.append(Spacer(1, 8))

    # Additional Experience section
    story.append(Paragraph("Additional Experience", styles['CVSectionHeader']))
    story.append(Paragraph("Data Engineering / Developer / Tester", styles['CVJobTitle']))
    story.append(Paragraph("Capgemini UK (02/2022 – 01/2023)", styles['CVCompany']))
    additional_experience_details = [
        "Migrated SAS solutions to PySpark and BigQuery.",
        "Used Databricks, Airflow, and GCP for ETL orchestration.",
        "Implemented AI (GPT3) for code testing and reconciliation.",
    ]
    story.append(ListFlowable(
        [ListItem(Paragraph(item, styles['CVListItem'])) for item in additional_experience_details],
        bulletType='bullet'
    ))
    story.append(Spacer(1, 8))

    story.append(Paragraph("Interests", styles['CVSectionHeader']))
    # Clean up hobbies text for better formatting
    hobbies_clean = hobbies_text.replace("🎶 ", "").replace("🎾 ", "").replace("🧠 ", "").replace("💡 ", "")
    story.append(Paragraph(hobbies_clean, styles['CVSkills']))

    doc.build(story)
    pdf_buffer.seek(0)

    # --- DOWNLOAD BUTTON ---
    st.download_button(
        label="📥 Download Antony Best's CV (PDF)",
        data=pdf_buffer,
        file_name=f"Antony_Best_Data_Engineer_CV_{datetime.now().strftime('%Y%m%d')}.pdf",
        mime="application/pdf",
    )
else:
    st.info("💡 PDF download will be available once the app is deployed with the requirements.txt file.")