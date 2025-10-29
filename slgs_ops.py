# SLGS Grammar School Library Management System - Operations
# Engineered with dictionary for books (O(1) lookups via ISBN), list for members (dynamic addition/removal), tuple for genres (immutable for validation)
# All functions include detailed validation to prevent errors, aligning with brief's CRUD + borrow/return requirements

slgs_books = {}
slgs_members = []
slgs_genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

def add_book(isbn: str, title: str, author: str, genre: str, total_copies: int) -> str:
    """Add a book after validating all inputs: unique ISBN, valid genre, positive copies, non-empty strings."""
    # Step 1: Validate inputs to avoid invalid data entry
    if not all([isbn, title, author, genre]) or total_copies < 1:
        return "All fields must be filled, and total copies must be at least 1!"
    # Step 2: Check for duplicate ISBN
    if isbn in slgs_books:
        return "ISBN already in grammar school catalog!"
    # Step 3: Validate genre against tuple
    if genre not in slgs_genres:
        return f"Genre must be one of: {', '.join(slgs_genres)}!"
    # Step 4: Add the book if all checks pass
    slgs_books[isbn] = {'title': title, 'author': author, 'genre': genre, 'total_copies': total_copies}
    return "Book added to SLGS grammar school library!"

def add_member(member_id: int, name: str, email: str) -> str:
    """Add a member after validating ID uniqueness and non-empty name/email."""
    # Step 1: Validate inputs
    if not name or not email or '@' not in email:  # Basic email check
        return "Name and valid email must be provided!"
    # Step 2: Check for duplicate ID by iterating list
    for member in slgs_members:
        if member['member_id'] == member_id:
            return "Member ID already registered in SLGS!"
    # Step 3: Append new member dict
    slgs_members.append({'member_id': member_id, 'name': name, 'email': email, 'borrowed_books': []})
    return "Member added to SLGS grammar school records!"

def search_book(keyword: str) -> list or str:
    """Search for books by title or author (case-insensitive), returning detailed matches or error."""
    # Step 1: Validate keyword
    if not keyword:
        return "Search keyword cannot be empty!"
    # Step 2: Iterate and collect matches
    results = []
    for isbn, details in slgs_books.items():
        if keyword.lower() in details['title'].lower() or keyword.lower() in details['author'].lower():
            results.append({
                'isbn': isbn,
                'title': details['title'],
                'author': details['author'],
                'genre': details['genre'],
                'total_copies': details['total_copies']
            })
    # Step 3: Return results or message
    return results if results else "No books found in SLGS catalog!"

def update_book(isbn: str, **kwargs) -> str:
    """Update book details with validation for genre and copies."""
    # Step 1: Check if ISBN exists
    if isbn not in slgs_books:
        return "ISBN not found in SLGS catalog!"
    # Step 2: Validate updates
    if 'genre' in kwargs and kwargs['genre'] not in slgs_genres:
        return "Updated genre must be valid for SLGS!"
    if 'total_copies' in kwargs and kwargs['total_copies'] < 0:
        return "Total copies cannot be negative!"
    # Step 3: Apply updates
    slgs_books[isbn].update(kwargs)
    return "Book updated in SLGS grammar school library!"

def delete_book(isbn: str) -> str:
    """Delete book only if not borrowed, after full check."""
    # Step 1: Check existence
    if isbn not in slgs_books:
        return "ISBN not found in SLGS!"
    # Step 2: Scan all members for borrowed status
    for member in slgs_members:
        if isbn in member['borrowed_books']:
            return "Cannot delete: Book is borrowed by a SLGS member!"
    # Step 3: Delete if clear
    del slgs_books[isbn]
    return "Book deleted from SLGS grammar school catalog!"

def borrow_book(isbn: str, member_id: int) -> str:
    """Borrow book after checking availability, member existence, and borrow limit."""
    # Step 1: Validate book existence and copies
    if isbn not in slgs_books:
        return "ISBN not found in SLGS!"
    if slgs_books[isbn]['total_copies'] < 1:
        return "No copies available in grammar school library!"
    # Step 2: Find member and check limit
    member = next((m for m in slgs_members if m['member_id'] == member_id), None)
    if not member:
        return "Member ID not found in SLGS records!"
    if len(member['borrowed_books']) >= 3:
        return "Member has reached the 3-book limit at SLGS!"
    # Step 3: Perform borrow
    member['borrowed_books'].append(isbn)
    slgs_books[isbn]['total_copies'] -= 1
    return "Book borrowed from SLGS grammar school library!"

def return_book(isbn: str, member_id: int) -> str:
    """Return book after verifying it's borrowed by the member."""
    # Step 1: Validate book and member
    if isbn not in slgs_books:
        return "ISBN not found in SLGS!"
    member = next((m for m in slgs_members if m['member_id'] == member_id), None)
    if not member:
        return "Member ID not found in SLGS records!"
    # Step 2: Check if borrowed
    if isbn not in member['borrowed_books']:
        return "This book was not borrowed by the member!"
    # Step 3: Perform return
    member['borrowed_books'].remove(isbn)
    slgs_books[isbn]['total_copies'] += 1
    return "Book returned to SLGS grammar school library!"