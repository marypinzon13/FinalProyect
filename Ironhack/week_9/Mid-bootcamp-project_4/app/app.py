import streamlit as st
import pandas as pd

st.header("CREATE YOUR OWN CAKE!")
## Recoger datos del pastel

# widget cake
cakes = st.selectbox(
    'Please, select your cake:',
    ('Victoria_Cake', 'Chocolat_Cake', 'Coco_Cake','Limon_Cake','Red_Velvet_Cake','Nuts_banana_caramel_Cake','Carrot_Cake','Oreo_Cake','Orange_poppy_seeds_Cake'))

st.write('You selected:', cakes)

# widget filling
fill = st.selectbox(
    'Plesea, select your favorite fill:',
    ('Batter_Cream', 'Batter_Cream_Oreo', 'Dark_Chocolate','Chocolat_Milk','White_chocolat','Limon_Curd','Strawberry_jam','cranberries_jam','mango_jam','orange_carrot_jam'))

st.write('You selected:', fill)

# widget fondant
fondant = st.selectbox(
    'Would you like fondant on your cake?:',
    ('Yes', 'No'))

st.write('You selected:', fondant)

# widget piece
piece = st.selectbox(
    'How many people do you want your cake for?:',
    ('6 - 8', '12 - 15', '18 - 20'))

st.write('You selected:', piece)

#Design
title = st.text_input('Please, indicate the type of design you want on your cake', 'TikTok cake')
st.write('Your design is', title)


# Montar el dataframe
testing = pd.DataFrame({"location_A":[1], "location_B":[0], "location_C":[0], "Carrot_Cake":[0],
       "Chocolat_Cake":[0], "Coco_Cake":[0], "Limon_Cake":[0], "Nuts_banana_caramel_Cake":[0],
       "Orange_poppy_seeds_Cake":[0], "Oreo_Cake":[1], "Red_Velvet_Cake":[0],
       "product_name_Red Velvet":[0], "Victoria_Cake":[0], "fill_Batter_Cream":[0],
       "fill_Batter_Cream_Oreo":[1], "fill_Caramel":[0], "fill_White_Chocolat":[0],
       "fill_Dark_Chocolat":[0], "fill_Milk_Chocolat":[0], "fill_Limon_Curd":[0],
       "fill_Strawberry_jam":[0], "fill_cranberries_jam":[0], "fill_mango_jam":[0],
       "fill_orange_carrot_jam":[0], "no_fondant":[0], "Fondant_L":[0], "Fondant_M":[0],
       "Fondant_S":[1], "High_design":[1], "Basic_design":[0], "Median_design":[0],
       "Excelent_design":[0], "No_design":[0], "diameter":[0], "piece":[0],})
#st.dataframe(testing)

# Cargar el scaler

# Cargar el modelo

# Usar el modelo para hacer la prediccion

# Mostrar resultado por pantalla
# Button
if st.button('Accept'):
    st.write('The price of your cake is: 25.16')
    st.write(testing)
    st.write('Thanks you!')
else:
    st.write('Thanks you!')














df = pd.read_csv('/Users/maryramirez/Ironhack/week_9/Mid-bootcamp-project_4/notebook/cakes_bbdd.csv')
st.dataframe(df)


