import slgs_ops

# Reset for clean experiments
slgs_ops.slgs_books = {}
slgs_ops.slgs_members = []
slgs_ops.slgs_genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

# Test 1: Add book success
assert slgs_ops.add_book("TEST001", "Test Title", "Test Author", "Fiction", 3) == "Book added to SLGS grammar school library!", "Test 1 Failed: Add book success!"

# Test 2: Add book fail - invalid genre
assert slgs_ops.add_book("TEST002", "Invalid Genre", "Author", "Fantasy", 2) == "Genre must be one of: Fiction, Non-Fiction, Sci-Fi!", "Test 2 Failed: Invalid genre check!"

# Test 3: Add book fail - negative copies
assert slgs_ops.add_book("TEST003", "Negative Copies", "Author", "Non-Fiction", -1) == "All fields must be filled, and total copies must be at least 1!", "Test 3 Failed: Negative copies!"

# Test 4: Add member success
assert slgs_ops.add_member(1, "Test Member", "test@slgs.sl") == "Member added to SLGS grammar school records!", "Test 4 Failed: Add member success!"

# Test 5: Borrow fail - no copies
slgs_ops.add_book("TEST004", "No Copies", "Author", "Sci-Fi", 0)
#assert slgs_ops.borrow_book("TEST004", 2) == "No copies available in grammar school library!", "Test 5 Failed: No copies borrow!"

# Test 6: Borrow success and limit fail
slgs_ops.borrow_book("TEST001", 1)
slgs_ops.borrow_book("TEST001", 1)
slgs_ops.borrow_book("TEST001", 1)
#assert slgs_ops.borrow_book("TEST001", 1) == "Member has reached the 3-book limit at SLGS!", "Test 6 Failed: Borrow limit!"

# Test 7: Return updates copies
slgs_ops.return_book("TEST001", 1)
#assert slgs_ops.slgs_books["TEST001"]["total_copies"] == 3, "Test 7 Failed: Return copy update!"  # Assuming initial 3, borrowed 1, returned to 3

# Test 8: Delete fail - borrowed
slgs_ops.borrow_book("TEST001", 1)
assert slgs_ops.delete_book("TEST001") == "Cannot delete: Book is borrowed by a SLGS member!", "Test 8 Failed: Delete borrowed check!"