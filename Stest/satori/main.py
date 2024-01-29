import streamlit as st
from backend import get_julia


col1,col2 = st.columns(2,gap='medium')
with col1:
    min_x, max_x = st.slider(label='実数部 x の範囲を変更',value=(-2.0,2.0),step=0.01,key='x')
    st.write('x_max  =  ',max_x,'   x_min  =  ',min_x) 
st.markdown('***')
with col2:
    min_y, max_y = st.slider(label='虚数部 y の範囲を変更',value=(-2.0,2.0),step=0.01,key='y')
    st.write('y_max  =  ',max_y,'   y_min  =  ',min_y)


col1,col2 = st.columns(2,gap='medium')
with col1:
    Ca = st.slider(label='複素定数 C の実数部を変更',value=-0.47,min_value=-2.0,max_value=2.0,step=0.01,key='a')
with col2:
    Cb = st.slider(label='複素定数 C の虚数部を変更',value=-0.45,min_value=-2.0,max_value=2.0,step=0.01,key='b')

st.write('comp_const = ',Ca,'  + ',Cb,'j') 
comp_const = complex(Ca,Cb)





if st.button('描画します'):
    st.session_state.chart_data = get_julia(min_x,max_x,min_y,max_y,comp_const)
    if (len(st.session_state.chart_data['x_axis'])) >= 500:
        st.session_state.Flag = True
    else:
        st.error('入力値が適正ではありません。変更してください')
        st.session_state.Flag = False
        



if 'Flag' in st.session_state:
    if st.session_state.Flag:
        st.scatter_chart(st.session_state.chart_data,x='x_axis',y='y_axis',color='color',size=12)




