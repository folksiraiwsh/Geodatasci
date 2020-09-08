{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2020-09-08 10:27:26.895 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.896 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.896 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.897 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.897 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.898 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.899 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.900 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.901 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.902 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.904 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.906 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.908 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.913 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.915 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n",
      "2020-09-08 10:27:26.916 WARNING fiona._env: Recode from CP437 to UTF-8 failed with the error: \"Invalid argument\".\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<streamlit.delta_generator.DeltaGenerator at 0x107ad0ca0>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import folium as fo\n",
    "from streamlit_folium import folium_static\n",
    "import geopandas as gp\n",
    "\n",
    "st.title('Streamlit with Folium')\n",
    "\n",
    "\"\"\"\n",
    "## An easy way to create a website using Python\n",
    "\"\"\"\n",
    "\n",
    "df = pd.read_csv('https://raw.githubusercontent.com/Maplub/MonthlyAirQuality/master/sensorlist.csv')\n",
    "\n",
    "tambol = st.text_input(label='ตำบล')\n",
    "\n",
    "st.write(df[df['tambol'] == tambol])\n",
    "\n",
    "\n",
    "crs = \"EPSG:4326\"\n",
    "geometry = gp.points_from_xy(df.lon,df.lat)\n",
    "geo_df  = gp.GeoDataFrame(df,crs=crs,geometry=geometry)\n",
    "\n",
    "nan_boundary  = gp.read_file('https://github.com/Maplub/AirQualityData/blob/master/nan_shp_wgs84.zip?raw=true')\n",
    "nanall = nan_boundary.unary_union\n",
    "\n",
    "nan_sta = geo_df.loc[geo_df.geometry.within(nanall)]\n",
    "\n",
    "\n",
    "longitude = 100.819200\n",
    "latitude = 19.331900\n",
    "\n",
    "station_map = fo.Map(\n",
    "\tlocation = [latitude, longitude], \n",
    "\tzoom_start = 10)\n",
    "\n",
    "latitudes = list(nan_sta.lat)\n",
    "longitudes = list(nan_sta.lon)\n",
    "labels = list(nan_sta.name)\n",
    "\n",
    "for lat, lng, label in zip(latitudes, longitudes, labels):\n",
    "\tfo.Marker(\n",
    "\t\tlocation = [lat, lng], \n",
    "\t\tpopup = label,\n",
    "\t\ticon = fo.Icon(color='red', icon='heart')\n",
    "\t).add_to(station_map)\n",
    "\n",
    "folium_static(station_map)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
