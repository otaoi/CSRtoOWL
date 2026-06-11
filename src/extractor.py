# Holds the pdfplumber and Regex logic
import pdfplumber
import re

def extract_client_data(pdf_path):
    extracted_data = {}
    
    print(f"extracting text from {pdf_path}...")
    full_text = ""
    
    # goes through with pdfplumber and grabs text appends to ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
    except Exception as e:
        print(f"couldnt read pdf: {e}")
        return None


    # we use [\s\S]*? to capture all text (even across multiple lines) 
    # logic regex 
    
    patterns = {
        "FirstName": r"First Name\s*([\s\S]*?)(?=Last Name)",
        "LastName": r"Last Name\s*([\s\S]*?)(?=Phone Number)",
        "Phone": r"Phone Number\s*([\s\S]*?)(?=E-Mail Address)",
        "Email": r"E-Mail Address\s*([\s\S]*?)(?=Street Address, City, Province)",
        "Address": r"Street Address, City, Province\s*([\s\S]*?)(?=Postal Code)",
        "PostalCode": r"Postal Code\s*([\s\S]*?)(?=Age)",
        "Age": r"Age\s*([\s\S]*?)(?=Date of Birth)",
        "DOB": r"Date of Birth\s*([\s\S]*?)(?=Identified Gender)",
        "Gender": r"Identified Gender\s*([\s\S]*?)(?=What is your preferred language\?)",
        
        # long form text box extraction
        "ReasonForSeeking": r"Why are you seeking counselling\?.*?\n([\s\S]*?)(?=Please provide the name \(if applicable\))",
        
        "SchedulePreference": r"Do you have preference for days/times for appointments\?.*?\n([\s\S]*?)(?=Image|Moving Forward Family Services|Informed Consent)"
    }

    # search the text for each pattern
    for key, pattern in patterns.items():
        match = re.search(pattern, full_text, re.IGNORECASE)
        if match:
            # .strip() removes any accidental line breaks or spaces around the answer
            extracted_data[key] = match.group(1).strip() 
        else:
            extracted_data[key] = "" # Field left blank on form

    # just in case formatting for checked boxes
    # TODO test these cases when the pdf example given
    for key, value in extracted_data.items():
        if "[X]" in value or "[x]" in value:
            extracted_data[key] = value.replace("[X]", "").replace("[x]", "").strip()

    return extracted_data