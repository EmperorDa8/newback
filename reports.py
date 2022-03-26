#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(save_name,title,info):
    styles=getSampleStyleSheet()
    report=SimpleDocTemplate(save_name)
    report_title=Paragraph(title, styles["h1"])
    report_info =Paragraph(info, styles["BodyText"])
    empty_line=Spacer(1,19)
    report.build([report_title, empty_line, report_info, empty_line])
    return report
