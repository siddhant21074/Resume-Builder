from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
import os
import pickle
from PreprocessData import name, mob_no, email, acheive_list, skill_list, proj_disc, proj_title,job_disc, job_durn, job_title, summary, cert_list,col1_duration, col2_duration, col1_name, col2_name


# Define output path
output_path = os.path.join("Resume_Checker", "src", "ResumesGenerated", "Generated_Resume.pdf")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Create PDF document
doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=20)

# Defining styles
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Header", fontName="Helvetica", fontSize=16, leading=20, alignment=TA_CENTER, spaceAfter=10))
styles.add(ParagraphStyle(name="SubHeader", fontName="Helvetica", fontSize=14, leading=18, spaceBefore=12, underlineWidth=1))
styles.add(ParagraphStyle(name="NormalText", fontName="Helvetica", fontSize=12, leading=16))
styles.add(ParagraphStyle(name="MyBullet", fontName="Helvetica", fontSize=12, leading=16, leftIndent=20))

# Build content
content = []

# Header
content.append(Paragraph(name, styles["Header"]))
content.append(Paragraph(f"+91- {mob_no}    {email}", styles["NormalText"]))
content.append(Spacer(1, 10))

# Summary
content.append(Spacer(1, 12))
content.append(Paragraph("SUMMARY", styles["SubHeader"]))
content.append(Paragraph("• " + summary, styles["MyBullet"]))

# Projects
content.append(Paragraph("PROJECTS", styles["SubHeader"]))
content.append(Paragraph(proj_title, styles["MyBullet"]))
content.append(Spacer(1, 6))
content.append(Paragraph("• " + proj_disc, styles["MyBullet"]))

# Experience
content.append(Spacer(1, 12))
content.append(Paragraph("EXPERIENCE", styles["SubHeader"]))
content.append(Paragraph("• " + job_title, styles["MyBullet"]))
content.append(Paragraph("• " + job_disc, styles["MyBullet"]))
content.append(Paragraph("• " + job_durn, styles["MyBullet"]))

# Education
content.append(Paragraph("EDUCATION", styles["SubHeader"]))
content.append(Paragraph("• " + col1_name, styles["MyBullet"]))
content.append(Paragraph("• " + col2_name, styles["MyBullet"]))

# Skills
content.append(Spacer(1, 12))
content.append(Paragraph("SKILLS", styles["SubHeader"]))
for skill in skill_list:
    content.append(Paragraph("• " + skill.strip(), styles["MyBullet"]))

# Certifications
content.append(Spacer(1, 12))
content.append(Paragraph("CERTIFICATION", styles["SubHeader"]))
for cert in cert_list:
    content.append(Paragraph("• " + cert.strip(), styles["MyBullet"]))

# Build PDF
doc.build(content)
print(f"✅ Resume PDF generated at: {output_path}")
