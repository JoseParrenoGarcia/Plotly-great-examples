from st_pages import Page, Section, add_indentation, show_pages

def pages_format():
    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠", in_section=False),
            Section(name="Rules for bar charts", icon="📊"),
            Page("pages/rule_17_when_not_to_use_bar_charts.py", "Rule 17 - When not to use them"),
            # Section(name="Rules for ", icon="⭐"),
        ]
    )