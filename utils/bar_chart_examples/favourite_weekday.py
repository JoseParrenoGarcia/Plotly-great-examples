import plotly.graph_objects as go

# def favourite_weekday_bar_chart_plot(df):
#     # Define the categorical order
#     categories = [animal for animal in df['Animal'] if animal != 'Other'] + ['Other']
#     df['SortOrder'] = df['Animal'].apply(lambda x: 1 if x == 'Other' else 0)
#     df = df.sort_values(by=['SortOrder', 'Percentage'], ascending=[True, False]).reset_index(drop=True)
#
#     fig = go.Figure(
#         data=[
#             go.Bar(
#                 x=df['Animal'],
#                 y=df['Percentage'],
#                 marker_color=[
#                     'lightgrey' if animal == 'Other' else 'darkblue' for animal in df['Animal']
#                 ],
#                 text=df['Percentage'].round(1),
#                 textposition='outside'
#             )
#         ]
#     )
#
#     # Customize the layout
#     fig.update_layout(
#         title=dict(
#             text='Tiger king',
#             y=0.9,
#             x=0,
#             xanchor='left',
#             yanchor='top',
#             font=dict(family="Helvetica Neue", size=24),
#         ),
#         annotations=[
#             # First paragraph annotation
#             dict(
#                 text="According to <i>Animal Planet</i> viewers, the tiger is the best beast.",
#                 xref="paper",
#                 yref="paper",
#                 x=0, y=1.25,
#                 showarrow=False,
#                 font=dict(family="Helvetica Neue", size=18),
#                 align="left"
#             ),
#             # Second paragraph annotation
#             dict(
#                 text="% who say this is their favourite animal",
#                 xref="paper", yref="paper",
#                 x=0, y=1.10,
#                 showarrow=False,
#                 font=dict(family="Helvetica Neue", size=14),
#                 align="left"
#             ),
#             # Footer annotation
#             dict(
#                 text="Source: Animal Planet, <a href='https://www.manchestereveningnews.co.uk/news/greater-manchester-news/tiger-is-worlds-favourite-animal-1131562'>Published in the Manchester news</a>",
#                 xref="paper", yref="paper",
#                 x=0, y=-0.18,
#                 showarrow=False,
#                 font=dict(family="Helvetica Neue", size=12),
#                 align="left"
#             )
#         ],
#         font=dict(family="Helvetica Neue"),
#         yaxis=dict(title="", visible=False),
#         xaxis=dict(title="",
#                    showline=True,
#                    linecolor='lightgrey',
#                    linewidth=3,
#                    type='category'
#                    ),
#         margin=dict(t=180, pad=0),
#         height=600,
#         width=700,
#     )
#
#     # Show the plot
#     return fig