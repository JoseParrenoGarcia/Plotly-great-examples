import plotly.graph_objects as go

def waterfall_bar_chart():
    fig = go.Figure(
        go.Waterfall(
            orientation="v",
            measure=["relative", "relative", "relative", "relative", "total"],
            x=["Sales", "Consulting", "Purchases", "Other expenses", "Profit before tax"],
            textposition="outside",
            text=["+60", "+80", "-40", "-20", "80"],
            y=[60, 80, -40, -20, 0],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        )
    )

    fig.update_layout(
        title=dict(text="Profit and loss statement 2018",
                   font=dict(family="Helvetica Neue", size=18),
                   ),
        showlegend=False,
        margin=dict(t=100, pad=0),
        height = 500,
        width=600,
        font=dict(family="Helvetica Neue"),
    )

    return fig