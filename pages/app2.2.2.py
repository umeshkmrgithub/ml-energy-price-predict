import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import numpy as np
#--------------------------------------------------------------------------------------------------------------------------------------

# page configuration
st.set_page_config(page_title="ML-MODEL",
                   page_icon='random',
                   layout="wide", )
st.write("""
<div style='text-align:center'>
    <h1 style='color:#009999;'>ML-MODEL FOR ENERGY CONSUMPTION YEAR 2016</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)


#--------------------------------------------------------------------------------------------------------------------------------------

# model = joblib.load('/home/umesh/Desktop/scratch_python/MD108 Project Files-20240713T050728Z-001/MD108 Project Files/ML_ENERGY_CONSUMPTION_FINAL_v2.2.2/ml_energy_consumption_final_v2.2.2/energy_consumption_model_ML2.2.joblib')
# model=joblib.load('/home/umesh/Desktop/energy_consumption_model_ML2.2.joblib')
model=('/home/umesh/Desktop/ML_FINAL_ENERGY_PRICE_PREDICT_v2.2/energy_consumption_model_ML2.2.joblib')
#--------------------------------------------------------------------------------------------------------------------------------------
st.title ("ML MODEL FOR ENERGY CONSUMPTION METER READING PREDICTION")

#--------------------------------------------------------------------------------------------------------------------------------------
selected = option_menu(None, [ "PREDICTION","ANALYSIS NOTES"],
                       icons=["house", 'cash-coin', 'trophy', "check-circle"], orientation='horizontal',
                       default_index=0)

if selected == 'PREDICTION':

            if 'PREDICTION':
                cc1, cc2 = st.columns([2, 2])
                with cc1:
                    primary_use = st.text_input("PRIMARY USE: (Edu: 1, Office: 2, Entertainment: 3, Resident: 4, Retail: 5, Parking: 6, Other: 7)")            
                    square_feet = st.text_input ("SQUARE FEET: (MIN: 7.863698387992262 , MAX: 13.09691017563933)")
                    air_temperature = st.text_input ("AIR_TEMPERATURE: (MIN: 2.85783267765904, MAX: 3.6136169696133895)")
                    dew_temperature = st.text_input ("DEW TEMPERATURE: (MIN: 2.4990256141907308, MAX: 3.280911215787653)")
                    precip_depth_1_hr = st.text_input ("PRECIP_DEPTH: (0)")
                    sea_level_pressure = st.text_input ("SEA LEVEL PRESSURE: (MIN: 6.917938771637118, MAX: 6.935210633605454)")
                    
                with cc2:
                    wind_direction = st.text_input ("WIND DIRECTION: (MIN: 0.3846444691323314, MAX: 5.8888779583328805)")
                    wind_speed = st.text_input ("WIND SPEED: (MIN: 0.3846444691323314, MAX: 2.3759981820890492)")
                    month = st.number_input("MONTH: ")
                    day = st.number_input("DAY")
                    hour = st.number_input ("HOUR")
                    log_meter_reading = st.text_input ("LOG METER READING: (MIN: 2.6838455124053926, MAX: 8.416488487294606)")

                    # button = st.button('prediction')
                    # prediction = model.predict([[primary_use,square_feet,air_temperature,dew_temperature,precip_depth_1_hr,sea_level_pressure,wind_direction,wind_speed,month,day,hour,log_meter_reading]])
                    # st.success(prediction[0])

                    # Input validation and conversion
                    try:
                        primary_use = float(primary_use) if primary_use else 0.0
                        square_feet = float(square_feet) if square_feet else 0.0
                        air_temperature = float(air_temperature) if air_temperature else 0.0
                        dew_temperature = float(dew_temperature) if dew_temperature else 0.0
                        precip_depth_1_hr = float(precip_depth_1_hr) if precip_depth_1_hr else 0.0
                        sea_level_pressure = float(sea_level_pressure) if sea_level_pressure else 0.0
                        wind_direction = float(wind_direction) if wind_direction else 0.0
                        wind_speed = float(wind_speed) if wind_speed else 0.0
                        month = int(month) if month else 1
                        day = int(day) if day else 1
                        hour = int(hour) if hour else 0
                        log_meter_reading = float(log_meter_reading) if log_meter_reading else 0.0

                        # Prepare the input data
                        input_data = np.array([[primary_use, square_feet, air_temperature, dew_temperature,
                                                precip_depth_1_hr, sea_level_pressure, wind_direction,
                                                wind_speed, month, day, hour, log_meter_reading]])
                        
                        # Make prediction
                        button = st.button('Predict Meter Reading')
                        prediction = model.predict(input_data)
                        st.success(f'Predicted Meter Reading (kWh): {prediction[0]}')

                    except ValueError as e:
                        st.error(f"Input error: {e}")
                        
if selected == 'ANALYSIS NOTES':
    st.markdown("# Analysis Summary ")
    st.write("The results of this study demonstrates how machine learning can be used to predict energy consumption. This explains the impact on external factors such air/ dew temperature, wind speed, sea level pressure and building floor space on the energy consumption.")
