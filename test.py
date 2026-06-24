from AIService import (
    qualify_lead,
    classify_support_ticket,
    draft_email,
    extract_data
)

print("\n=== Lead Qualification ===")
print(
    qualify_lead(
        "Company: ABC Ltd, 50 employees, interested in CRM software."
    )
)

print("\n=== Ticket Classification ===")
print(
    classify_support_ticket(
        "I was charged twice for my subscription."
    )
)

print("\n=== Email Draft ===")
print(
    draft_email(
        "Follow up after product demo and schedule next meeting."
    )
)

print("\n=== Data Extraction ===")
def extract_data(raw_text):
    return ask_llm(
        "You are a data extraction assistant. Return ONLY valid JSON.",
        f"""
Extract:

{{
  "name": "",
  "email": "",
  "phone": ""
}}

Text:
{raw_text}
"""
    )
print(
    extract_data(
        "Ahmad Tariq, ahmad@gmail.com, +92 300 1234567"
    )
)