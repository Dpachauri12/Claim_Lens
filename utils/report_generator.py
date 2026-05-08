from fpdf import FPDF

def generate_report(results, output_path="reports/report.pdf"):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="GEO Truth Engine Verification Report", ln=True)

    for item in results:
        pdf.multi_cell(0, 10, txt=f"Claim: {item['claim']}")
        pdf.multi_cell(0, 10, txt=f"Status: {item['status']}")
        pdf.multi_cell(0, 10, txt=f"Correct Fact: {item['correct_fact']}")
        pdf.multi_cell(0, 10, txt=f"Source: {item['source']}")
        pdf.ln(5)

    pdf.output(output_path)

    return output_path