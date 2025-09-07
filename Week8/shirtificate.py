from fpdf import FPDF

  
def generate_pdf(name):        
    pdf = FPDF(orientation="portrait",unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 28)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", ln=True)
    pdf.image("shirtificate.png", x=10, y=60, w=190)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(120)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

def main():
    name = input("Name: ")
    generate_pdf(name)

if __name__=="__main__":
    main()