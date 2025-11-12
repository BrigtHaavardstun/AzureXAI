import pydeck as pdk
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [500, 500] +
    [60.539386568981655, 5.240386546193804],
    columns=['lat', 'lon'])

st.map(map_data)


gps_data = map_data

st.subheader("Using st.map")
st.map(gps_data)

st.subheader("Using st.pydeck_chart")
radius = 4
st.pydeck_chart(
    pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=gps_data.iloc[0]['lat'], longitude=gps_data.iloc[0]['lon'], zoom=13.4
        ),
        layers=[
            pdk.Layer(
                "ScatterplotLayer",
                data=gps_data,
                get_position=["lon", "lat"],
                get_color=[0, 249, 0],
                get_radius=radius,
            ),
        ],
    )
)
