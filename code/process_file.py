'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
from io import StringIO
import json
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process File of Packages")

packFile = st.file_uploader("Upload package file:", type = "txt")

if packFile:
    packBin = packFile.getvalue()
    packText = StringIO(packBin.decode("utf-8")).read()
    all_packages = [] # to store each line parsed for json output
    for line in packText.split("\n"):
        pack_list = parse_packaging(line)
        total_size = calc_total_units(pack_list)
        unit = get_unit(pack_list)
        all_packages.append(pack_list)

        st.info(f"{line} -> Total Package Size: {total_size} {unit}")

    fname = packFile.name
    jsonFile = fname.replace(".txt", ".json")
    with open(jsonFile, "w") as j:
        json.dump(all_packages, j, indent = 4)
    st.success(f"{len(all_packages)} written to {jsonFile}")



