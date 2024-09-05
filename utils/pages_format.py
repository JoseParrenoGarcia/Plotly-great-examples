from st_pages import Page, Section, show_pages

def pages_format():
    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠", in_section=False),
            Section(name="Rules for bar charts", icon="📊"),
            Page("pages/rule_17_alternative_to_bar_charts.py", "Rule 17 - Alternatives to bar charts"),
            # Section(name="Rules for ", icon="⭐"),
        ]
    )