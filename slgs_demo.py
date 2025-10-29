import slgs_ops

# Add books with SLGS theme
print(slgs_ops.add_book("SLGS001", "Grammar School Math", "Teacher Kamara", "Non-Fiction", 4))
print(slgs_ops.add_book("SLGS002", "Sierra Leone Folktales for Grammar School", "Author Bangura", "Fiction", 3))
print(slgs_ops.add_book("SLGS003", "Sci-Fi Adventures for Students", "Writer Jalloh", "Sci-Fi", 2))
print(slgs_ops.add_book("SLGS001", "Duplicate", "Author", "Fiction", 1))  # Fail: Duplicate

# Add members
print(slgs_ops.add_member(1, "Abu Sesay", "abu@slgs.sl"))
print(slgs_ops.add_member(2, "Mariama Conteh", "mariama@slgs.sl"))
print(slgs_ops.add_member(1, "Duplicate", "email@slgs.sl"))  # Fail: Duplicate ID
print(slgs_ops.add_member(3, "", "invalid"))  # Fail: Empty name

# Borrow books (success and errors)
print(slgs_ops.borrow_book("SLGS001", 1))  # Success
print(slgs_ops.borrow_book("SLGS002", 1))  # Success
print(slgs_ops.borrow_book("SLGS003", 1))  # Success
print(slgs_ops.borrow_book("SLGS003", 1))  # Fail: Limit
print(slgs_ops.borrow_book("SLGS004", 1))  # Fail: ISBN not found
print(slgs_ops.borrow_book("SLGS001", 4))  # Fail: Member not found
slgs_ops.update_book("SLGS003", total_copies=0)
print(slgs_ops.borrow_book("SLGS003", 2))  # Fail: No copies

# Search books
print(slgs_ops.search_book("Grammar"))
print(slgs_ops.search_book(""))  # Fail: Empty keyword

# Update book
print(slgs_ops.update_book("SLGS001", title="Advanced Grammar School Math", total_copies=5))
print(slgs_ops.update_book("SLGS001", genre="Invalid"))  # Fail: Invalid genre
print(slgs_ops.update_book("SLGS004", title="Missing"))  # Fail: Not found

# Return book
print(slgs_ops.return_book("SLGS001", 1))  # Success
print(slgs_ops.return_book("SLGS004", 1))  # Fail: Not borrowed
print(slgs_ops.return_book("SLGS001", 4))  # Fail: Member not found

# Delete book
print(slgs_ops.delete_book("SLGS001"))  # Success after return
print(slgs_ops.delete_book("SLGS002"))  # Fail: Borrowed
print(slgs_ops.delete_book("SLGS004"))  # Fail: Not found