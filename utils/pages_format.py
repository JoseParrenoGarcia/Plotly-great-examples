from st_pages import Page, Section, show_pages

def pages_format():
    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠", in_section=False),
            Section(name="Rules for bar charts", icon="📊"),
            Page("pages/rule_17_alternative_to_bar_charts.py", "R17. Bar chart alternatives"),
            Page("pages/rule_18_bar_chart_colouring_and_grouping.py", "R18. Colouring and grouping"),
            Page("pages/rule_19_ordering_bar_charts.py", "R19. Order of bars"),
        ]
    )