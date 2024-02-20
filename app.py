import streamlit as st
import base64
from streamlit_card import card
import streamlit.components.v1 as components








def get_image_data(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/png;base64," + encoded.decode("utf-8")
    return data


def showcase():
    st.markdown("--- ")
    st.header("🎥 Videos created using VideoGPT")
    st.write("Welcome to VideoGPT")


    vid_col_1, vid_col_2, vid_col_3 = st.columns(3)
    vid_col_1.video("static/videos/Resemble.ai.mp4")
    vid_col_1.text("🤖 Revolutionizing Voiceovers: How Resemble.ai's Cloning Tech Created Our AI Video ")

    vid_col_2.video("static/videos/Historic.mp4")
    vid_col_2.text("🤖  Historic Shorts for Reels ")

    vid_col_3.video("static/videos/Hackathon.mp4")
    vid_col_3.text("🤖  Hackathon Passion ")






st.set_page_config(page_title="VideoGPT", page_icon="📷", layout="centered")


def main():
    # show logo image in center

    _, img_col, _ = st.columns([1, 3, 1])
    img_col.image("./static/images/VideoGPTlogo.png")

    st.info(
        """
        **Welcome to VideoGPT!** 🚀

        The project aims to simplify AI-based content creation while ensuring accessibility and user-friendliness
        .Create AI Videos with your own Voice using VideoGPT and Resemble.ai
        """
    )

    with st.sidebar:
        _, img_col, _ = st.columns([1, 3, 1])
        img_col.image("./static/images/VideoGPTlogo.png")
    st.markdown("--- ")
    st.header("🛠️ Tools")
    col1, col2 = st.columns(2)

    video_image_1 = get_image_data("./static/images/video1.png")

    with col1:
        hasClicked = card(
            title="🎬 Create Video",
            text="",
            image=video_image_1,
            url="/topic_to_video",
            key="image_card",
            styles={
                "card": {
                    "width": "100%",
                },
                "filter": {
                    "background-color": "rgba(0, 0, 0, 0.65)"  # <- make the image not dimmed anymore
                },
            },
        )
    with col2:
        pass

    showcase()









if __name__ == "__main__":

    main()

