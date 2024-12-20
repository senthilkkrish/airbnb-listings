#-----------------------------------------------------------------------------------------------------#
# Run the below in the terminal 
#-----------------------------------------------------------------------------------------------------#
#pip install google-api-python-client 
#pip install isodate
#-----------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------#
# Importing required packages
#-----------------------------------------------------------------------------------------------------#
import streamlit as st
from pymongo import MongoClient
import pandas as pd
import os
import time
import plotly.express as px
import plotly.graph_objects as go
from tenacity import retry, stop_after_attempt, wait_fixed

#-----------------------------------------------------------------------------------------------------#
# Defining Mongo DB Database Connection 
#-----------------------------------------------------------------------------------------------------#
myclient = MongoClient(
    "mongodb+srv://dhodho20:Mongo2024@cluster0.xabkc5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

#-----------------------------------------------------------------------------------------------------#
## Code for Streamlit page      
#-----------------------------------------------------------------------------------------------------#

st.set_page_config(layout="wide")
st.header(
    "Air BnB Details",
    divider="orange",
    anchor="Airbnb_SK",
)

#-----------------------------------------------------------------------------------------------------#
## Define Dataframe Struture for processing Listing details      
#-----------------------------------------------------------------------------------------------------#
Mapdf_clms = {
    "List_id": [],
    "List_name": [],
    "List_price": [],
    "List_sum": [],  
   # 'List_add':[],
    'List_st':[],
    'List_sub':[],
    'List_Gov_Area':[],
    'List_Mar':[],
    "List_CC": [],  #'List_Coord':[],
    "List_Coord_X": [],
    "List_Coord_Y": [],  # "List_img" :[],
    "List_img_url": [],
    "List_acco": [],
    "List_amen": [],
    "List_beds": [],
    "List_bath": [],
    "List_rating": [],
}


mydb = myclient["sample_airbnb"]
mycollection = mydb["listingsAndReviews"]
# myquery = { "address": { "$regex": "^S" } }
myquery = {"_id": {"$regex": "^1"}}

#-----------------------------------------------------------------------------------------------------#
## Function to Plot Listings country level map 
#-----------------------------------------------------------------------------------------------------#

def Map_Plot(csv_name, MapList_CC,MapGeo_scope):
    CC = MapList_CC
    csv = pd.read_csv(csv_name)
    
    fig = go.Figure(
        data=go.Scattergeo(
            lon=csv["List_Coord_X"],
            lat=csv["List_Coord_Y"],
            text=csv["List_name"],
            mode="markers",
            marker_color="red",
            marker=dict(
            size=10,
            color=df["List_price"],  # Color by price
            colorscale="Viridis",  # Choose a color scale
            showscale=True,
            colorbar_title="Price ($)",
            ),
        )
    )
    fig.update_layout(
        geo=dict(
        projection_type="orthographic",  # Projection type
        showland=True,
        landcolor="rgb(217, 217, 217)",  # Background land color
        oceancolor="rgb(204, 229, 255)",  # Background ocean color
        showcountries=True,
        ),
        title={
        "text": "Map for Visualization"  # Title text
         },
        title_font=dict(size=20),
        width=800,
        height=400,
        #title= "Map for Visualization",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        #title="Airbnb Hotels",
        geo_scope=MapGeo_scope
    )
    fig.update_traces(marker_size=15, line=dict(color="teal"))  # Adjust marker size as needed
    st.plotly_chart(fig, use_container_width=False)

#-----------------------------------------------------------------------------------------------------#
## Function to get country level Listing details      
#-----------------------------------------------------------------------------------------------------#

def Map_Details(Country_code, Geo_scope):
    MapList_CC = "BR"
    Selected_CC = Country_code
    MapGeo_scope = Geo_scope
    mapquery = {"address.country_code": Selected_CC}
    count = mycollection.count_documents({})
    mydoc = mycollection.find(mapquery) #.limit(20)
    l_doc = mydoc.to_list()
    Selected_CC = Country_code
    
    for item in mydoc:
        print(item)
        break
    #print(f"{l_doc[0]['address'] = }")
    for x in l_doc:
        MapList_id = x["_id"]
        MapList_name = x["name"]
        MapList_price = x["price"]
        MapList_sum = x["summary"]
        MapList_add = x["address"]
        MapList_st = MapList_add.get("street")
        MapList_sub = MapList_add.get("suburb")
        MapList_Gov_Area = MapList_add.get("government_area")
        MapList_Mar = MapList_add.get("market")
        MapList_CC = MapList_add.get("country_code")
        MapList_Coord = x["address"]["location"]["coordinates"]
        MapList_review = x["review_scores"]
        MapList_rating = MapList_review.get("review_scores_rating")
        Map_coord_x = MapList_Coord[0]
        Map_coord_y = MapList_Coord[1]
        MapList_img = x["images"]
        MapList_url = MapList_img.get("picture_url")
        MapList_acco = x["accommodates"]
        MapList_amen = x["amenities"]
    
        if ("beds" in x) and (x["beds"] in l_doc):
            st.write("beds exist")
            if x["beds"] is not None:
                MapList_beds = x["beds"]
            else:
                MapList_beds = 0
        else:
            MapList_beds = "No Info"

        if "bathrooms" in x:
            MapList_bath = x["bathrooms"]
        else:
            MapList_bath = 0
    
        Mapdf_clms["List_id"].append(MapList_id)
        Mapdf_clms["List_name"].append(MapList_name)
        Mapdf_clms["List_price"].append(MapList_price)
        Mapdf_clms["List_sum"].append(MapList_sum)
        Mapdf_clms["List_st"].append(MapList_st)
        Mapdf_clms["List_sub"].append(MapList_sub)
        Mapdf_clms["List_Gov_Area"].append(MapList_Gov_Area)
        Mapdf_clms["List_Mar"].append(MapList_Mar)
        Mapdf_clms["List_CC"].append(MapList_CC)
        Mapdf_clms["List_Coord_X"].append(Map_coord_x)
        Mapdf_clms["List_Coord_Y"].append(Map_coord_y)
        Mapdf_clms["List_img_url"].append(MapList_url)
        Mapdf_clms["List_acco"].append(MapList_acco)
        Mapdf_clms["List_amen"].append(MapList_amen)
        Mapdf_clms["List_beds"].append(MapList_beds)
        Mapdf_clms["List_bath"].append(MapList_bath)
        Mapdf_clms["List_rating"].append(MapList_rating)
                
    Map_df = pd.DataFrame(Mapdf_clms)
    
    csv_name = "Airbnb_Listings_dtls.csv"
    csv_file = Map_df.to_csv(csv_name, index=False, mode="w+")

#-----------------------------------------------------------------------------------------------------#
##  Function to get selected Listing details
#-----------------------------------------------------------------------------------------------------#    
def Listing_Details(Selected_Area):
    st.header(
        f"Top Listings for {Selected_Area}",
        divider="blue",
    )
    csv_name = "Airbnb_Listings_dtls.csv"
    Listing_df = pd.read_csv(csv_name)
    filtered_data = Listing_df[df['List_Gov_Area'].isin(Selected_Area) ]
    for index, x in filtered_data.iterrows():
        MapList_url = x["List_img_url"]
        MapList_name = x["List_name"]
        MapList_sum = x["List_sum"]
        MapList_price = x["List_price"]
        MapList_beds = x["List_beds"]
        MapList_bath = x["List_bath"]
        MapList_amen = x["List_amen"]
        with st.container(height=300, border=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                st.image(MapList_url, width=300)
                st.write(MapList_name)
            with c2:
                st.write(MapList_sum)
                st.write("Price : ", MapList_price, " / Night")
                st.write("No of Beds : ", MapList_beds)
                st.write("No of Bathrooms : ", MapList_bath)
            with c3:
                st.write("Amenities : ", MapList_amen)

#-----------------------------------------------------------------------------------------------------#
## Code for st.sidebar in Streamlit page      
#-----------------------------------------------------------------------------------------------------#

with st.sidebar:
     st.sidebar.image("airbnb.jpg", use_column_width=False)
     # Display DataFrame in Streamlit
     st.write("Data from MongoDB Collection:")
     Dest = st.selectbox(
                "Select Destination : ",
                ("AUSTRALIA", "BRAZIL", "CANADA", "CHINA", "HONKONG", "PORTUGAL", "SPAIN", "TURKEY", "USA"),
            )
     CC1 = Dest[0:2]
     if Dest == "USA":
        CC = Dest[0:2]
        Geo_scope = "usa"
     elif Dest == "BRAZIL":
        CC = Dest[0:2]
        Geo_scope = "south america"
     elif Dest == "CANADA":
        CC = Dest[0:2]
        Geo_scope = "north america"
     elif Dest == "CHINA":
        CC = Dest[0:2]
        Geo_scope = "asia"
     elif Dest == "HONKONG":
        CC = "HK"
        Geo_scope = "asia"
     elif Dest == "PORTUGAL":
        CC = "PT"
        Geo_scope = "europe"
     elif Dest == "SPAIN":
        CC = "ES"
        Geo_scope = "europe"
     elif Dest == "TURKEY":
        CC = "TR"
        Geo_scope = "europe"
     else:
        CC = Dest[0:2]
        Geo_scope = "world"
     Map_Details(CC, Geo_scope)
     csv_name = "Airbnb_Listings_dtls.csv"
     df = pd.read_csv(csv_name)
     # Extract the 'area' column and remove duplicates
     Mar_list = df['List_Mar'].drop_duplicates().tolist()
     # Display the dropdown
     selected_Mar = st.selectbox("Select a City", Mar_list)
     
     filtered_data = df[df['List_Mar'] == selected_Mar]
     # Select a value within the filtered data
     if not filtered_data.empty:
      value_column = "List_Gov_Area"  # Replace with the column name containing the values
      area_list = filtered_data[value_column].drop_duplicates().tolist()
      selected_area = st.multiselect("Select a Area", area_list)
      
#-----------------------------------------------------------------------------------------------------#
## Code Columns in Streamlit page      
#-----------------------------------------------------------------------------------------------------#
      
col1, col2, col3 = st.columns(3)
with col1:
    #Call charts for Visualization
    if "List_Gov_Area" in df.columns and "List_price" in df.columns:
        # Group by country and calculate average price
        avg_price_df = df.groupby("List_Gov_Area")["List_price"].mean().reset_index()
        avg_price_df.columns = ["Area", "Average Price"]

        # Create a bar chart using Plotly
        fig = px.bar(
            avg_price_df,
            x="Average Price",
            y="Area",
            orientation="h",
            title="Average Price of Hotels by Area",
            labels={"Average Price": "Price (USD)", "Area": "Area"},
            color="Average Price",
            color_continuous_scale="Viridis"
        )
        # Show the chart in Streamlit
        st.plotly_chart(fig)
with col2:
    #Call charts for Visualization
    if "List_Gov_Area" in df.columns and "List_rating" in df.columns:
        filtered_df = df[df["List_rating"] > 85]

        # Group by area and count the number of hotels
        area_rating_df = filtered_df.groupby("List_Gov_Area")["List_rating"].count().reset_index()
        area_rating_df.columns = ["Area", "Hotel Rating"]
   
        # Create a bar chart using Plotly
        fig = px.bar(
            area_rating_df,
            y="Area",
            x="Hotel Rating",
            orientation="h",
            title="Hotels with Rating Above 85 by Area",
            labels={"Hotel Rating": "Number of Hotels", "Area": "Area"},
            color="Hotel Rating",
            color_continuous_scale="Blues"
        )
        # Show the chart in Streamlit
        st.plotly_chart(fig)
with col3:
    
#-----------------------------------------------------------------------------------------------------#
## Calling Function to get Map Plotted for selected country 
#-----------------------------------------------------------------------------------------------------#
    Map_Plot(csv_name, CC, Geo_scope)
    
#-----------------------------------------------------------------------------------------------------#
## Code for search in Streamlit page      
#-----------------------------------------------------------------------------------------------------#
          
if st.button("Search"):
 #col1, col2, col3 = st.columns(3)
 #with col1:
 
#-----------------------------------------------------------------------------------------------------#
## Calling Function to get selected Listing details      
#-----------------------------------------------------------------------------------------------------#

   Listing_Details(selected_area)
with st.spinner("Wait for it..."):
    time.sleep(1)
st.success("Done!", icon="✅")

#-----------------------------------------------------------------------------------------------------#
# End of Code
#-----------------------------------------------------------------------------------------------------#
