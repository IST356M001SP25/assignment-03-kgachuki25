'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
from io import StringIO
import json
from packaging import parse_packaging, calc_total_units, get_unit

if "filecount" not in st.session_state:
    st.session_state.filecount = 0
if "linecount" not in st.session_state:
    st.session_state.linecount = 0
if "packagehist" not in st.session_state:
    st.session_state.packagehist = []

st.title("Process Package Files")

packFile = st.file_uploader("Upload package file:", type = "txt")

if packFile:
    packBin = packFile.getvalue()
    packText = StringIO(packBin.decode("utf-8")).read()
    all_packages = [] # to store each line parsed for json output
    for line in packText.split("\n"):
        pack_list = parse_packaging(line)
        all_packages.append(pack_list)
        st.session_state.linecount += 1
    st.session_state.filecount += 1
    fname = packFile.name
    jsonFile = fname.replace(".txt", ".json")
    with open(jsonFile, "w") as j:
        json.dump(all_packages, j, indent = 4)
    st.session_state.packagehist.append(f"{len(all_packages)} packages written to {jsonFile}")

for h in st.session_state.packagehist:
    st.info(h)
st.success(f"{st.session_state.filecount} files processed, {st.session_state.linecount} total lines processed")
