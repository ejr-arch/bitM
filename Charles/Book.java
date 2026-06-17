public class Book {

	private String isbn;
	private String title;
	private String author;
	private boolean available;

	// Book book1 = new Book(56354423, guardian);
	public Book(String isbn, String title) {
		this.isbn = isbn;
		this.title = title;
		available = true;
	}

	// Book book2 = new Book(56t63727, guardian, titus);
	public Book(String isbn, String title, String author) {
		this.isbn = isbn;
		this.title = title;
		this.author = author;
	}

	public String getIsbn() {
		return isbn;
	}

	public String getTitle() {
		return title;
	}

	public String getAuthor() {
		return author;
	}

	public boolean getStatus() {
		return available;
	}

	public void setStatus(boolean available) {
		this.available = available;
	}

	@Override
	public String toString() {
		// to be implemented
		return null;
	}
}
