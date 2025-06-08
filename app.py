import streamlit as st
from openai_utils import generate_linkedin_post, humanize_post, openai_detect_ai
# from zerogpt_utils import is_ai_written  # No longer needed

st.set_page_config(page_title="Linkedin Human Post Writer", page_icon="📝")
st.title("📝 Linkedin Human Post Writer")
st.write("Generate LinkedIn posts that sound human, not AI!")

user_prompt = st.text_area("What do you want your LinkedIn post to be about?", height=100)

if st.button("Generate Post"):
    if not user_prompt.strip():
        st.warning("Please enter a topic or achievement.")
    else:
        with st.spinner("Generating your LinkedIn post..."):
            post = generate_linkedin_post(user_prompt)
        if not post:
            st.error("Failed to generate post. Please try again.")
        else:
            max_attempts = 3
            attempt = 0
            history = []
            while attempt < max_attempts:
                with st.spinner(f"Checking if the post sounds AI-written (using OpenAI, Attempt {attempt+1})..."):
                    ai_result = openai_detect_ai(post)
                history.append((post, ai_result))
                if ai_result is None:
                    st.error("Error checking with OpenAI. Please try again later.")
                    break
                st.info(f"Detection result: {ai_result}")
                if ai_result.strip().lower().startswith('ai') is False:
                    st.success("Your LinkedIn post is ready and sounds human!")
                    st.text_area("Final LinkedIn Post", value=post, height=200)
                    break
                st.warning("OpenAI detected AI writing. Humanizing the post...")
                with st.spinner("Humanizing the post..."):
                    post = humanize_post(post)
                if not post:
                    st.error("Failed to humanize post. Please try again.")
                    break
                attempt += 1
            else:
                st.info("Max attempts reached. Here is the best version of your post:")
                st.text_area("Final LinkedIn Post", value=post, height=200)
            # Show history of attempts
            with st.expander("See all attempts and AI detection results"):
                for i, (p, flag) in enumerate(history, 1):
                    st.markdown(f"**Attempt {i}:** {flag}")
                    st.code(p) 