'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process Package")

package_string = st.text_input("Enter package data: ")
if package_string:
    pack_list = parse_packaging(package_string)
    total_size = calc_total_units(pack_list)
    unit = get_unit(pack_list)

    st.text(pack_list)

    for dict in pack_list:
        for key, value in dict.items():
            st.info(f"{key} -> {value}")
    st.success(f"Total Package Size: {total_size}")
