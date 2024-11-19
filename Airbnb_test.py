import streamlit as st 
from pymongo import MongoClient
import pandas as pd
import os
import time
import plotly.express as px
import plotly.graph_objects as go
from tenacity import retry, stop_after_attempt, wait_fixed

myclient = MongoClient ( 'mongodb+srv://dhodho20:Mongo2024@cluster0.xabkc5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

st.set_page_config(layout="wide")
st.header('Air BnB Details', divider='orange', anchor='Airbnb_SK', ) 

with st.sidebar:
    st.sidebar.image('airbnb.jpg', use_column_width=False)

df_clms={'List_id':[], 'List_URL':[], 'List_name':[], 'List_sum':[], 'List_space':[], 'List_des':[], 'List_neig':[], 'List_notes':[], 'List_trans':[], 'List_acc':[], 'List_int':[],
'List_hsrules':[], 'List_proptype':[], 'List_rmtype':[], 'List_bedtype':[], 'List_min':[], 'List_max':[], 'List_cancel':[],
'List_ls':[], 'List_calls':[], #'List_frev':[], 'List_lrev':[], 
'List_acco':[], #'List_bedrooms':[], 'List_beds':[], 
'List_noofrev':[], #'List_bath':[], 
'List_amen':[], 'List_price':[], #'List_secdep':[], 'List_cleanfee':[], 
'List_extrappl':[], 'List_guesticlu':[], 
'List_img':[], 'List_host':[], 'List_add':[], 'List_avail':[], 'List_revscores':[], 'List_reviews':[]} 

Mapdf_clms={'List_id':[], 'List_name':[], 'List_price':[],  'List_sum':[], #'List_add':[], 
            'List_CC':[], #'List_Coord':[], 
            'List_Coord_X' :[], 'List_Coord_Y' :[], #"List_img" :[], 
            "List_img_url":[],"List_acco":[], "List_amen":[], "List_beds":[] , "List_bath":[]  } 

mydb = myclient["sample_airbnb"]
mycollection = mydb["listingsAndReviews"]
#myquery = { "address": { "$regex": "^S" } }
myquery = { "_id": {"$regex":"^1"} }
#myquery = { "_id": "10051164" }
#mydoc = mycol.find(myquery)
mydoc = mycollection.find(myquery)
#mydoc = mycollection.find()
#df = pd.DataFrame(mydoc,columns= ['Items','Values'])
# for x in mydoc:
#       print(x)

# for x in mydoc:
#       List_id=x['_id']
#       #print (List_id)
#       List_URL=x['listing_url']
#       #print (URL_id)
#       List_name=x['name']
#       #print (List_name)
#       List_sum=x['summary']
#       List_space=x['space']
#       List_des=x['description']
#       List_neig=x['neighborhood_overview']
#       List_notes=x['notes']
#       List_trans=x['transit']
#       List_acc=x['access']
#       List_int=x['interaction']
#       List_hsrules=x['house_rules']
#       List_proptype=x['property_type']
#       List_rmtype=x['room_type']
#       List_bedtype=x['bed_type']
#       List_min=x['minimum_nights']
#       List_max=x['maximum_nights']
#       List_cancel=x['cancellation_policy']
#       List_ls=x['last_scraped']
#       List_calls=x['calendar_last_scraped']
#       # if x['first_review'] is not None:
#       #       List_frev=x['first_review']
#       # else:
#       #   List_frev=None
#       #List_frev=x['first_review']
      
#       # if x['last_review'] is not None:
#       #       List_lrev=x['last_review']
#       # else:
#       #   List_lrev=None
#       #List_lrev=x['last_review']
      
#       List_acco=x['accommodates']
#       # if x['bedrooms'] is not None:
#       #       List_bedrooms=x['bedrooms']
#       # else:
#       #   List_bedrooms=None
#       #List_bedrooms=x['bedrooms']
      
#       # if x['beds'] is not None:
#       #       List_beds=x['beds']
#       # else:
#       #   List_beds=None
#       #List_beds=x['beds']
      
#       List_noofrev=x['number_of_reviews']
#       # if x['bathrooms'] is not None:
#       #       List_bath=x['bathrooms']
#       # else:
#       #   List_bath=None
#       #List_bath=x['bathrooms']
      
#       List_amen=x['amenities']
#       List_price=x['price']
#       # if x['security_deposit'] is not None:
#       #       List_secdep=x['security_deposit']
#       # else:
#       #   List_secdep=None 
#       #List_secdep=x['security_deposit']
      
#       # if x['cleaning_fee'] is not None:
#       #       List_cleanfee=x['cleaning_fee']
#       # else:
#       #   List_cleanfee=None 
#       #List_cleanfee=x['cleaning_fee']
      
#       List_extrappl=x['extra_people']
#       List_guesticlu=x['guests_included']
#       List_img=x['images']
#       List_host=x['host']
#       List_add=x['address']
#       List_avail=x['availability']
#       List_revscores=x['review_scores']
#       List_reviews=x['reviews']
      
      
#       df_clms['List_id'].append(List_id)
#       df_clms['List_URL'].append(List_URL)
#       df_clms['List_name'].append(List_name)
#       df_clms['List_sum'].append(List_sum)
#       df_clms['List_space'].append(List_space)
#       df_clms['List_des'].append(List_des)
#       df_clms['List_neig'].append(List_neig)
#       df_clms['List_notes'].append(List_notes)
#       df_clms['List_trans'].append(List_trans)
#       df_clms['List_acc'].append(List_acc)
#       df_clms['List_int'].append(List_int)
#       df_clms['List_hsrules'].append(List_hsrules)
#       df_clms['List_proptype'].append(List_proptype)
#       df_clms['List_rmtype'].append(List_rmtype)
#       df_clms['List_bedtype'].append(List_bedtype)
#       df_clms['List_min'].append(List_min)
#       df_clms['List_max'].append(List_max)
#       df_clms['List_cancel'].append(List_cancel)
#       df_clms['List_ls'].append(List_ls)
#       df_clms['List_calls'].append(List_calls)
#       #df_clms['List_frev'].append(List_frev)
#       #df_clms['List_lrev'].append(List_lrev)
#       df_clms['List_acco'].append(List_acco)
#       #df_clms['List_bedrooms'].append(List_bedrooms)
#       #df_clms['List_beds'].append(List_beds)
#       df_clms['List_noofrev'].append(List_noofrev)
#       #df_clms['List_bath'].append(List_bath)
#       df_clms['List_amen'].append(List_amen)
#       df_clms['List_price'].append(List_price)
#       #df_clms['List_secdep'].append(List_secdep)
#       #df_clms['List_cleanfee'].append(List_cleanfee)
#       df_clms['List_extrappl'].append(List_extrappl)
#       df_clms['List_guesticlu'].append(List_guesticlu)
#       df_clms['List_img'].append(List_img)
#       df_clms['List_host'].append(List_host)
#       df_clms['List_add'].append(List_add)
#       df_clms['List_avail'].append(List_avail)
#       df_clms['List_revscores'].append(List_revscores)
#       df_clms['List_reviews'].append(List_reviews)
# List_df=pd.DataFrame(df_clms)
# List_df_head = List_df.head()
# print (List_df_head)
#st.write(List_df)
# Reset the index and drop the index column
#List_df.reset_index(drop=True, inplace=True)
#List_df.set_index('column', inplace=True)
#st.dataframe(List_df.style.hide(axis="index"))
#st.dataframe(List_df.)
#st.table(List_df_head)

def Map_Plot(csv_name,MapList_CC,MapGeo_scope):
    CC=MapList_CC
    csv = pd.read_csv(csv_name)
    #df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
    #csv['text'] = csv['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

    fig = go.Figure(data=go.Scattergeo(
            lon = csv['List_Coord_X'],
            lat = csv['List_Coord_Y'],
            text = csv['List_name'],
            mode = 'markers',
            marker_color = 'red',
            ))

    fig.update_layout(width=800, height=800, margin={"r": 0, "t": 0, "l": 0, "b": 0},
            title = 'Airbnb Hotels',
            geo_scope=MapGeo_scope,
        )
    fig.update_traces(marker_size=15, line=dict(color='teal'))  # Adjust marker size as needed
    #fig.update_geos(projection_type="orthographic")
    fig.show()



def Map_Details(Country_code, Geo_scope):     
    #st.write('Received CC as ')
    #st.write(Country_code)
    MapGeo_scope=Geo_scope
    mapquery = { "_id": {"$regex":"^1"} }
    #mapquery = { "country_code": Country_code }
    #mapquery = { "address.country_code": Country_code } 
    #mapquery = { "address.country_code" :{"$in": Country_code}}
    #mydoc = mycol.find(myquery)
    mydoc = mycollection.find(mapquery) 
    print(mapquery)
    print (mydoc)
    Selected_CC=Country_code
    #st.write(Country_code)
    for x in mydoc:
        print (x)
        MapList_id=x['_id']
        MapList_name=x['name']
        MapList_price=x['price']
        MapList_sum=x['summary']
        MapList_add=x['address']
        MapList_CC=MapList_add.get('country_code')
        #MapList_Coord=MapList_add.get('location')
        MapList_Coord=x['address']['location']['coordinates']
        Map_coord_x=MapList_Coord[0]
        Map_coord_y=MapList_Coord[1]
        MapList_img=x['images']
        MapList_url=MapList_img.get('picture_url')
        MapList_acco=x['accommodates']
        MapList_amen=x['amenities']
        # global App_amen
        # for i in MApList_amen:
        #     App_amen = App_amen + ', ' + i
        
        if x['beds'] in mydoc:
          st.write("beds exist")            
          if x['beds'] is not None:
            MapList_beds=x['beds']
            # st.write("beds not None")
          else:
              MapList_beds= 0
        else:
            MapList_beds= 'No Info'
      
        # if x['bathrooms'] in mydoc:
        if x['bathrooms'] is not None:
            MapList_bath=x['bathrooms']
        else:
            MapList_bath=0
        # else:
        #     MapList_bath= 'No Info' 
        
        Mapdf_clms['List_id'].append(MapList_id)
        Mapdf_clms['List_name'].append(MapList_name)
        Mapdf_clms['List_price'].append(MapList_price)
        Mapdf_clms['List_sum'].append(MapList_sum)
        #Mapdf_clms['List_add'].append(MapList_add)
        Mapdf_clms['List_CC'].append(MapList_CC)
        #Mapdf_clms['List_Coord'].append(MapList_Coord)
        Mapdf_clms['List_Coord_X'].append(Map_coord_x)
        Mapdf_clms['List_Coord_Y'].append(Map_coord_y)
        #Mapdf_clms['List_img'].append(MapList_img)
        Mapdf_clms['List_img_url'].append(MapList_url)
        Mapdf_clms['List_acco'].append(MapList_acco)
        Mapdf_clms['List_amen'].append(MapList_amen)
        Mapdf_clms['List_beds'].append(MapList_beds)
        Mapdf_clms['List_bath'].append(MapList_bath)

    Map_df=pd.DataFrame(Mapdf_clms)
    #print (Map_df)
    Map_df_head = Map_df.head()
    #print (Map_df_head)
    #st.write(Map_df_head)
    #return MapList_url, MapList_name, MapList_price
    
    csv_name = "Airbnb_Listings_dtls.csv"
    csv_file=Map_df.to_csv(csv_name,index=False,mode='w')
    #st.write("Top 5 Listings from your search")
    st.header('Top 5 Listings from your search', divider='blue', )
    for index, x in Map_df.iterrows(): 
    #for index, x in Map_df_head.iterrows():
        MapList_url=x['List_img_url']
        MapList_name=x['List_name']
        MapList_sum=x['List_sum']
        MapList_price=x['List_price']
        MapList_beds=x['List_beds']
        MapList_bath=x['List_bath']
        MapList_amen=x['List_amen']
        with st.container(height=300, border=True):
            c1,c2,c3 = st.columns(3)    
            with c1:    
                st.image(MapList_url, use_column_width=False, width=300)
                st.write(MapList_name)
                #st.write("Price : ", MapList_price, " / Night")
            with c2:
                st.write(MapList_sum)
                st.write("Price : ", MapList_price, " / Night")
                st.write("Max Occupancy : ", MapList_acco)
                st.write("No of Beds : ", MapList_beds)
                st.write("No of Bathrooms : ", MapList_bath)
                
            with c3:    
                st.write("Amenities : ", MapList_amen)
                
    #with st.container(height=700, border=True):            
        # c1 = st.columns([1])
        # with c1:
    Map_Plot(csv_name,MapList_CC,MapGeo_scope) 
        # with c2:
        #     st.write("Data")
# Display DataFrame in Streamlit
st.write("Data from MongoDB Collection:")
col1,col2,col3 = st.columns(3)
with col1:
    Dest = st.selectbox(
        "Select Destination : ", ('AUSTRALIA','BRAZIL', 'CANADA', 'CHINA', 'HONKONG', 
                                  'PORTUGAL', 'SPAIN','TURKEY', 'USA')
    )
    st.write("Selected : ", Dest) 
    CC1=(Dest[0:2])
    #st.write(Dest)
    #st.write(CC1)
    if Dest == 'USA':
        CC = (Dest[0:2])
        Geo_scope ='usa'
    elif Dest == 'BRAZIL':
        CC = (Dest[0:2])
        Geo_scope ='south america'
    elif Dest == 'CANADA':
        CC = (Dest[0:2])
        Geo_scope ='north america'
    elif Dest == 'CHINA':
        CC = (Dest[0:2])
        Geo_scope ='asia'
    elif Dest == 'HONKONG':
        CC = 'HK'
        Geo_scope ='asia'
    elif Dest == 'PORTUGAL':
        CC = 'PT'
        Geo_scope ='europe'
    elif Dest == 'SPAIN':
        CC = 'ES'
        Geo_scope ='europe'
    elif Dest =='TURKEY':
        CC = 'TR'
        Geo_scope ='europe'
    else:
         CC = (Dest[0:2])
         Geo_scope ='world'
    #st.write(CC)
with col2: 
    Chk_in = st.date_input("Check-In Date", value=None, format='DD/MM/YYYY')
    st.write("Your Check-In Date : ", Chk_in)
    
with col3:
    Chk_out = st.date_input("Check-Out Date", value=None, format='DD/MM/YYYY')
    st.write("Your Check-Out Date : ", Chk_out)
    
#with col4:
st.write("Click here to") 
if st.button('Search'):
    Map_Details(CC,Geo_scope)
    
    #st.progress() 
        # progress_text = "Operation in progress. Please wait."
        # my_bar = st.progress(0, text=progress_text)
        # for percent_complete in range(100):
        #     time.sleep(0.01)
        #     my_bar.progress(percent_complete + 1, text=progress_text)
        #     time.sleep(0.05)
        #     my_bar.empty()
    with st.spinner('Wait for it...'):
        time.sleep(1)
    st.success('Done!',icon="✅")

            #row1 = st.columns(2) 
            # row2 = st.columns(3) 

            #for col in row1 + row2: 
                #tile = col.container(height=200, border=True)
                #tile.title(":balloon:")
                #tile.image(['airbnb.jpg','airbnb.jpg','airbnb.jpg','airbnb.jpg'])
                #tile.button('Next')
                #st.image('airbnb.jpg', caption='airbnb')

        # # Function to get the list of image files
        # def get_image_files(image_dir):
        #     image_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
        #     return [os.path.join(image_dir, f) for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_extensions]

        # # Directory containing the images
        # image_dir = 'C:/Users/Viney Acsa Sam/OneDrive/Pictures'  # Change this to your image directory
        # image_files = get_image_files(image_dir)

        # # Initialize session state
        # if 'current_image_index' not in st.session_state:
        #     st.session_state.current_image_index = 0

        #     # Function to go to the next image
        # def next_image():
        #     st.session_state.current_image_index = (st.session_state.current_image_index + 1) % len(image_files)

        # # Display the current image
        # current_image = image_files[st.session_state.current_image_index]


        # with st.container(height=230, border=True):
        #     #st.image(current_image, use_column_width=False, width=200)
        #     #x=Map_df_head["List_id"]
        #     #pic=Map_df_head["List_img"]
        #     # Extract the 'picture_url' from the 'list_img' column
        #     #pic = MapList_img.get('picture_url')
        #     st.image(MapList_url, use_column_width=False, width=300)
        #     st.write(MapList_name)
        #     #st.write(Map_sum)

        # with st.container(height=230, border=True):
        #     #st.image(current_image, use_column_width=False, width=200)
        #     # x=List_df_head["List_id"]
        #     # pic=List_df_head["List_img"]
        #     # # Extract the 'picture_url' from the 'list_img' column
        #     # pic = List_img.get('picture_url')
        #     st.image(MapList_url, use_column_width=False, width=300)
        #     st.write(MapList_name)
        #     #st.write(MapList_sum)

# st.write(Map_df)

#df = pd.DataFrame(dtls, columns= ['States', 'Total Transaction Amount', 'Total Transacion Count'])
# csv_name = "Listings_data.csv"
# csv_file=List_df_head.to_csv(csv_name,index=False,mode='w')
# csv = pd.read_csv(csv_name)
# #print(csv.values)

# fig = px.choropleth(
#     csv,
#     #dtls,
#     geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
#     featureidkey='properties.ST_NM',
#     locations='States',
#     #color='Total Transaction Amount',
#     color= 'States',
#     #color_continuous_scale=px.colors.sequential.Plasma,
#     hover_name='States',
#     hover_data=['Total Transacion Count', 'States'],
#     color_continuous_scale="mint",
#     scope='asia'
# )

# fig.update_geos(fitbounds='locations', visible=False)
# fig.update_layout(title_text=f'Phone Pe Transaction Details - India', geo=dict(
# showframe=False,showcoastlines=False,),width=1500, height=500, margin={"r":0,"t":0,"l":0,"b":0}, hovermode='x unified')

  
# Keys = List_df_head.keys() 
# #st.table(Keys)
# items = List_df_head.items()
# #st.table(items) 
