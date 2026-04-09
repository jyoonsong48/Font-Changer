from pyfiglet import Figlet
import random
import streamlit as st

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)
f = ["5lineoblique", "alligator", "alligator2", "bigchief", "binary", "block", "calgphy2", "caligraphy", "catwalk", "cosmic", "cosmike", "hollywood", "isometric1", "larry3d",  "smkeyboard", "speed", "ticksslant"]

st.title("Font Changer")
text_input = st.sidebar.text_input("*✧.*. •.°✵ :ᴡʀɪᴛᴇ ꜱᴏᴍᴇᴛʜɪɴɢ ʜᴇʀᴇ･ﾟ✧･ﾟ✵ *･ﾟ")

if text_input == "":
    st.write("Write Something...")
else:
    for i in f:
        st.subheader(f"{i}")
        figlet.setFont(font=i)
        text = figlet.renderText(text_input)
        st.code(text, language=None)
    st.subheader(f"ʀᴀɴᴅᴏᴍ ꜰᴏɴᴛ ꜰᴏʀ ʏᴏᴜ ⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾*+:•*∴")
    fig = Figlet(font = random_font)
    text = fig.renderText(text_input)
    st.code(text, language=None)
