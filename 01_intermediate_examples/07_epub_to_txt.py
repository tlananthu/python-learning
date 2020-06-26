import ebooklib
from ebooklib import epub

book=epub.read_epub('resources/07/poyman_karadu.epub')

bookTitle=book.get_metadata('DC', 'title')

allItems=book.get_items()
for item in allItems:
    print(item)
    print(item.get_body_contents())