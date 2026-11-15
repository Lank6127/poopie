import streamlit

streamlit.set_page_config(page_title="sneak aex website")

streamlit.header("this is sneak aex website")
streamlit.subheader("go to this website to learn more sneak aex")
streamlit.write("[click](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
streamlit.caption("go to this for the genre of sneak aex")
streamlit.write("[totally innocent](http://rule34.world/)")
button = streamlit.checkbox("button for kitten")
if button:
    streamlit.image("https://i.pinimg.com/736x/e4/e0/bb/e4e0bb2d87cd56405a16e86e6b33dc4a.jpg")

if streamlit.checkbox("sneak aex"):
    streamlit.write("how dare you try to see sneak aex")
    streamlit.image("https://i.pinimg.com/736x/9e/99/60/9e9960b22b2c6182dc3ead866899081b.jpg")