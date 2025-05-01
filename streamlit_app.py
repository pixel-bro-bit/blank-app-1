import streamlit as st

# Configure the page settings
st.set_page_config(page_title="My Awesome Website", layout="wide")

def render_home():
    st.title("Welcome to My Awesome Website")
    st.write("This is the Home page. Enjoy exploring the content!")
    # Display a sample image from Picsum (you can replace this with your own image URL)
    st.image("https://picsum.photos/800/300", caption="A Beautiful Scenery")
    st.write("Here you'll find updates, news, and more.")

def render_about():
    st.title("About Us")
    st.write(
        """
        This website is built with **Streamlit**, a fast and easy way to create interactive web apps with Python.
        
        **Technologies used:**
        - Python
        - Streamlit
        
        Streamlit allows you to focus on coding and data logic while it handles the web interface.
        """
    )
    # You can also add more components like charts, user inputs, etc.
    st.markdown("Learn more about how Streamlit works by visiting their [official documentation](https://docs.streamlit.io/).")

def render_contact():
    st.title("Contact")
    st.write("Have questions or suggestions? Get in touch!")
    st.write("Email: [example@example.com](mailto:example@example.com)")
    # Optionally, add a contact form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thanks for reaching out!")

def main():
    # Create a sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", ["Home", "About", "Contact"])

    # Render content based on the selected page
    if page == "Home":
        render_home()
    elif page == "About":
        render_about()
    elif page == "Contact":
        render_contact()

if __name__ == "__main__":
    main()
