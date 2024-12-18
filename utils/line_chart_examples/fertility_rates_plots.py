import plotly.graph_objects as go
import plotly.express as px

def fertility_rates_plotly_express_line_chart(df):
    fig = px.line(df,
                 x='Year',
                 y='Fertility_Rate',
                 color='Country Name',
                 title='Fertility rates (children per woman)')

    # Minor layout customization
    fig.update_layout(
        font=dict(family="Helvetica Neue"),
        height=600,
        width=1000,
    )

    return fig

def fertility_rates_line_plot(df, title, countries_to_highlight):
    fig = go.Figure()

    for country in df['Country Name'].unique():
        if country not in countries_to_highlight:
            fig.add_trace(
                go.Scatter(x=df[df['Country Name'] == country]['Year'],
                           y=df[df['Country Name'] == country]['Fertility_Rate'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='rgba(204, 209, 209, 0.5)', width=1)
                           )
            )

    for country in countries_to_highlight:
        if country in df['Country Name'].unique():
            fig.add_trace(
                go.Scatter(x=df[df['Country Name'] == country]['Year'],
                           y=df[df['Country Name'] == country]['Fertility_Rate'],
                           mode='lines',
                           name=country,
                           showlegend=False,
                           line=dict(color='purple', width=2)
                           )
            )

            if country == 'United Arab Emirates':
                text='UAE'
                textposition = 'middle right'
            elif country == 'Congo, Dem. Rep.':
                text='Congo'
                textposition = 'middle right'
            elif country == 'Somalia':
                text = 'Somalia'
                textposition = 'top right'
            else:
                text=country
                textposition='middle right'



            fig.add_trace(
                go.Scatter(x=df[(df['Country Name'] == country) & (df['Year'] == df['Year'].max())]['Year'],
                           y=df[(df['Country Name'] == country) & (df['Year'] == df['Year'].max())]['Fertility_Rate'],
                           mode='markers+text',
                           name=country,
                           showlegend=False,
                           marker=dict(color='purple', size=6),
                           text=text,
                           textposition=textposition,
                           textfont=dict(family="Helvetica Neue", color='purple', size=12),
                           )
            )

    # Update layout
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(family="Helvetica Neue", size=24),
        ),
        annotations=[
            # First paragraph annotation
            dict(
                text="Children per woman",
                xref="paper",
                yref="paper",
                x=-0.085, y=1.08,
                showarrow=False,
                font=dict(family="Helvetica Neue", size=14),
                align="left"
            ),
        ],
        xaxis=dict(
            showline=True,
            linecolor='lightgrey',
            linewidth=2,
            range=[df['Year'].min(), df['Year'].max()+9],
        ),
        yaxis=dict(
            title='',
            showline=True,
            showgrid=False,
            linecolor='lightgrey',
            linewidth=2,
            ticksuffix="  ",
        ),
        font=dict(family="Helvetica Neue", size=14),
        showlegend=False,
        margin=dict(t=150, r=100, pad=0),
        height=800,
        width=700,
    )

    return fig

