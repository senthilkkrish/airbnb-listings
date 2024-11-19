import streamlit as st 
from pymongo import MongoClient
import pandas as pd
import os
import time
import plotly.express as px
import plotly.graph_objects as go
from tenacity import retry, stop_after_attempt, wait_fixed

myclient = MongoClient ( 'mongodb+srv://dhodho20:Mongo2024@cluster0.xabkc5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


df_clms={'List_id':[], 'List_URL':[], 'List_name':[], 'List_sum':[], 'List_space':[], 'List_des':[], 'List_neig':[], 'List_notes':[], 'List_trans':[], 'List_acc':[], 'List_int':[],
'List_hsrules':[], 'List_proptype':[], 'List_rmtype':[], 'List_bedtype':[], 'List_min':[], 'List_max':[], 'List_cancel':[],
'List_ls':[], 'List_calls':[], #'List_frev':[], 'List_lrev':[], 
'List_acco':[], #'List_bedrooms':[], 'List_beds':[], 
'List_noofrev':[], #'List_bath':[], 
'List_amen':[], 'List_price':[], #'List_secdep':[], 'List_cleanfee':[], 
'List_extrappl':[], 'List_guesticlu':[], 
'List_img':[], 'List_host':[], 'List_add':[], 'List_avail':[], 'List_revscores':[], 'List_reviews':[]} 


mydb = myclient["sample_airbnb"]
mycollection = mydb["listingsAndReviews"]

mydoc = mycollection.find()

for x in mydoc:
      List_id=x['_id']
      #print (List_id)
      List_URL=x['listing_url']
      #print (URL_id)
      List_name=x['name']
      #print (List_name)
      List_sum=x['summary']
      List_space=x['space']
      List_des=x['description']
      List_neig=x['neighborhood_overview']
      List_notes=x['notes']
      List_trans=x['transit']
      List_acc=x['access']
      List_int=x['interaction']
      List_hsrules=x['house_rules']
      List_proptype=x['property_type']
      List_rmtype=x['room_type']
      List_bedtype=x['bed_type']
      List_min=x['minimum_nights']
      List_max=x['maximum_nights']
      List_cancel=x['cancellation_policy']
      List_ls=x['last_scraped']
      List_calls=x['calendar_last_scraped']
      # if x['first_review'] is not None:
      #       List_frev=x['first_review']
      # else:
      #   List_frev=None
      #List_frev=x['first_review']
      
      # if x['last_review'] is not None:
      #       List_lrev=x['last_review']
      # else:
      #   List_lrev=None
      #List_lrev=x['last_review']
      
      List_acco=x['accommodates']
      # if x['bedrooms'] is not None:
      #       List_bedrooms=x['bedrooms']
      # else:
      #   List_bedrooms=None
      #List_bedrooms=x['bedrooms']
      
      # if x['beds'] is not None:
      #       List_beds=x['beds']
      # else:
      #   List_beds=None
      #List_beds=x['beds']
      
      List_noofrev=x['number_of_reviews']
      # if x['bathrooms'] is not None:
      #       List_bath=x['bathrooms']
      # else:
      #   List_bath=None
      #List_bath=x['bathrooms']
      
      List_amen=x['amenities']
      List_price=x['price']
      # if x['security_deposit'] is not None:
      #       List_secdep=x['security_deposit']
      # else:
      #   List_secdep=None 
      #List_secdep=x['security_deposit']
      
      # if x['cleaning_fee'] is not None:
      #       List_cleanfee=x['cleaning_fee']
      # else:
      #   List_cleanfee=None 
      #List_cleanfee=x['cleaning_fee']
      
      List_extrappl=x['extra_people']
      List_guesticlu=x['guests_included']
      List_img=x['images']
      List_host=x['host']
      List_add=x['address']
      List_avail=x['availability']
      List_revscores=x['review_scores']
      List_reviews=x['reviews']
      
      
      df_clms['List_id'].append(List_id)
      df_clms['List_URL'].append(List_URL)
      df_clms['List_name'].append(List_name)
      df_clms['List_sum'].append(List_sum)
      df_clms['List_space'].append(List_space)
      df_clms['List_des'].append(List_des)
      df_clms['List_neig'].append(List_neig)
      df_clms['List_notes'].append(List_notes)
      df_clms['List_trans'].append(List_trans)
      df_clms['List_acc'].append(List_acc)
      df_clms['List_int'].append(List_int)
      df_clms['List_hsrules'].append(List_hsrules)
      df_clms['List_proptype'].append(List_proptype)
      df_clms['List_rmtype'].append(List_rmtype)
      df_clms['List_bedtype'].append(List_bedtype)
      df_clms['List_min'].append(List_min)
      df_clms['List_max'].append(List_max)
      df_clms['List_cancel'].append(List_cancel)
      df_clms['List_ls'].append(List_ls)
      df_clms['List_calls'].append(List_calls)
      #df_clms['List_frev'].append(List_frev)
      #df_clms['List_lrev'].append(List_lrev)
      df_clms['List_acco'].append(List_acco)
      #df_clms['List_bedrooms'].append(List_bedrooms)
      #df_clms['List_beds'].append(List_beds)
      df_clms['List_noofrev'].append(List_noofrev)
      #df_clms['List_bath'].append(List_bath)
      df_clms['List_amen'].append(List_amen)
      df_clms['List_price'].append(List_price)
      #df_clms['List_secdep'].append(List_secdep)
      #df_clms['List_cleanfee'].append(List_cleanfee)
      df_clms['List_extrappl'].append(List_extrappl)
      df_clms['List_guesticlu'].append(List_guesticlu)
      df_clms['List_img'].append(List_img)
      df_clms['List_host'].append(List_host)
      df_clms['List_add'].append(List_add)
      df_clms['List_avail'].append(List_avail)
      df_clms['List_revscores'].append(List_revscores)
      df_clms['List_reviews'].append(List_reviews)
List_df=pd.DataFrame(df_clms)
List_df_head = List_df.head()
print (List_df_head)
st.write(List_df)
#Reset the index and drop the index column
List_df.reset_index(drop=True, inplace=True)
List_df.set_index('column', inplace=True)
st.dataframe(List_df.style.hide(axis="index"))
st.dataframe(List_df.)
st.table(List_df_head)


def Map_Details(Country_code, Geo_scope):     
    #st.write('Received CC as ')
    #st.write(Country_code)
    MapGeo_scope=Geo_scope
    #mapquery = { "_id": {"$regex":"^1"} }
    #mapquery = { "country_code": Country_code }
    mapquery = { "address.country_code": Country_code } 
    #mapquery = { "address.country_code" :{"$in": Country_code}}
    #mydoc = mycol.find(myquery)
    mydoc = mycollection.find(mapquery)
    Selected_CC=Country_code
    #st.write(Country_code)
    for x in mydoc:
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
        
        # if x['beds'] in mydoc:
        #     st.write("beds exist")
        if x['beds'] is not None:
            MapList_beds=x['beds']
            # st.write("beds not None")
        else:
            MapList_beds= 0
        # else:
        #     MapList_beds= 'No Info'
      
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
    Map_df_head = Map_df.head()
    #print (Map_df_head)
    #st.write(Map_df_head)
    #return MapList_url, MapList_name, MapList_price
    
    csv_name = "Airbnb_data_PowerBI.csv"
    csv_file=Map_df.to_csv(csv_name,index=False,mode='w')
    #st.write("Top 5 Listings from your search")
    