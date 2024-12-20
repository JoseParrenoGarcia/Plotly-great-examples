from st_pages import Page, show_pages

def pages_format():
    show_pages(
        [
            Page("streamlit_app.py", "Home", "🏠", in_section=False),
            Page("pages/bar_chart_section.py", "Rules for bar charts", "📊"),
            Page("pages/rule_17_alternative_to_bar_charts.py", "R17. Bar chart alternatives"),
            Page("pages/rule_18_bar_chart_colouring_and_grouping.py", "R18. Colouring and grouping"),
            Page("pages/rule_19_ordering_bar_charts.py", "R19. Order of bars"),
            Page("pages/rule_24_labelling_axis_bar_charts.py", "R24. Axis labelling"),
            Page("pages/rule_25_broken_bars_and_non_zero_starts_bar_charts.py", "R25. Non zero starts and broken bars"),
            Page("pages/rule_28_clustered_columns.py", "R28. Careful with clustered columns"),
            Page("pages/line_chart_section.py", "Rules for line charts", "📈"),
            Page("pages/rule_30_lines_distance.py", "R30. Lines can represent distance"),
            Page("pages/rule_31_too_many_lines.py", "R31. Too many lines"),
            Page("pages/rule_32_colours_with_meaning.py", "R32. Colours with meaning"),
            Page("pages/rule_35_markers_on_lines.py", "R35. Markers on lines"),
            Page("pages/rule_36_line_width.py", "R36. Line width"),
            Page("pages/rule_41_area_charts.py", "R41. Area charts"),
        ]
    )