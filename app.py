
import os
import streamlit as st
from databas import add_book, get_all_books, delete_book, search_book, get_statistics

st.markdown("""<style>
 .stApp {background-color: #f5f5f5;}           
             <style/>
            """ ,unsafe_allow_html=True)
# 🎉 Title
st.title("📚 Personal Library Manager")

# 🔥 Sidebar Menu
menu = st.sidebar.selectbox(
    "Select an Option", 
    [ "Home","Add a Book", "Display All Books", "Remove a Book", "Search a Book", "Display Statistics"]
)
if menu == "Home":
   st.subheader("🏠 Welcome to Personal Library Manager!")
   st.image("home.png", use_container_width=True)
   st.write("Select an option from the sidebar to get started.")
# ✅ 1. Add a Book
if menu == "Add a Book":
    st.subheader("➕ Add a New Book")

    book_Name = st.text_input("Enter the name of the book:")
    book_Author = st.text_input("Enter the author of the book:")
    published_year = st.text_input("Enter the published year:")
    genre = st.text_input("Enter the genre of the book:")
    read = st.radio("Enter the read status:", ["Yes", "No"])

    if st.button("Add Book"):
        book = {
            "title": book_Name,
            "author": book_Author,
            "published_year": published_year,
            "genre": genre,
            "status": "yes" if read == "Yes" else "no"
        }
        add_book(book)
        st.success("✅ Book added successfully!")

# ✅ 2. Display All Books
elif menu == "Display All Books":
    st.subheader("📖 Library Collection")
    books = get_all_books()
    
    if not books:
        st.warning("No books in the library.")
    else:
        for book in books:
            st.write(f"**{book['title']}** by *{book['author']}*")
            st.text(f"Published in {book['published_year']} | Genre: {book['genre']} | Read: {book['status']}")
            st.markdown("---")

# ✅ 3. Remove a Book
elif menu == "Remove a Book":
    st.subheader("❌ Remove a Book")
    book_Name = st.text_input("Enter the name of the book to remove:")

    if st.button("Remove Book"):
        result = delete_book(book_Name)
        if result.deleted_count > 0:
            st.success("✅ Book removed successfully!")
        else:
            st.error("⚠️ Book not found in the library.")

# ✅ 4. Search for a Book
elif menu == "Search a Book":
    st.subheader("🔍 Search for a Book")
    book_Name = st.text_input("Enter the name of the book to search:")

    if st.button("Search"):
        book = search_book(book_Name)
        if book:
            st.success(f"**Found:** {book['title']} by {book['author']}")
            st.text(f"Genre: {book['genre']} | Published: {book['published_year']} | Read: {book['status']}")
        else:
            st.error("⚠️ Book not found.")

# ✅ 5. Display Statistics
elif menu == "Display Statistics":
    st.subheader("📊 Library Statistics")
    total_books, read_books, read_percentage = get_statistics()

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books} ({read_percentage:.2f}%)")
