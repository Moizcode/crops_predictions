import streamlit as st
import pickle
import sklearn as sk


model = pickle.load(open('model.pkl', 'rb'))


season = pickle.load(open('season.pkl', 'rb'))
crop = pickle.load(open('crop.pkl', 'rb'))
state = pickle.load(open('state.pkl', 'rb'))

st.markdown('''
<style>

.css-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    background-color: sienna;
    border-radius: 18px;
    text-align: center;
}

</style>
''', unsafe_allow_html=True,
            )

st.title('Crop Production Prediction')


with st.expander('Inputs'):
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        selected_state = st.selectbox(
            'Select state',
            (state))
    with a2:
        selected_season = st.selectbox(
            'Select season',
            (season))
    with a3:
        selected_crop = st.selectbox(
            'Select Crop',
            (crop))
    with a4:
        area = st.number_input('Insert Area of field(Acre)')

if st.button('Predict'):
    data = pickle.load(open('datafram.pkl', 'rb'))
    data['Area'] = area
    selected_state = "State_Name_"+selected_state
    selected_season = "Season_"+selected_season
    selected_crop = "Crop_"+selected_crop
    data[selected_crop] = 1
    data[selected_season] = 1
    data[selected_state] = 1
    result = model.predict(data)[0]
    result_text = "Yield Prediction {price:.2f} Tonnes"
    st.subheader(result_text.format(price=result))
