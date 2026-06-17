public class Library {

	Book[] books = new Book[100];
	Member[] members = new Member[100];
	Loan[] loans = new Loan[100];

	public void addBook(Book newBook) {
		int i = 0;
		while (i < 100) {
			if (books[i] == null) {
				books[i] = newBook;
				return;
			}
			i++;
		}
		System.out.println("space used up!!");
	}

	/*
	 * public void addBook(String isbn, String title, String author) {
	 * Book newBook = new Book(isbn, title, author);
	 * 
	 * int i = 0;
	 * while (i < 100) {
	 * if (books[i] == null) {
	 * books[i] = newBook;
	 * return;
	 * }
	 * i++;
	 * }
	 * }
	 */

	public void registerMember(Member newMember) {
		int i = 0;
		while (i < 100) {
			if (members[i] == null) {
				members[i] = newMember;
				break;
			}
			i++;
		}
		return;
	}

	public Book findBook(String title) {
		if (books == null) {
			System.out.println("Library is empty");
			return null;
		}

		int i = 0;
		while (i < 100) {
			if (books[i].getTitle().equals(title)) {
				return books[i];
			} else
				i++;
		}
		return null;
	}

	public void lendBook(Member borrower, Book book, String bDate, String dDate) {
		// if book exists in system
		if (findBook(book.getTitle()) == null) {
			System.out.println("book is not known in system");
			return;
		}

		// if book is taken already
		if (book.getStatus() == false) {
			System.out.println("Book is already taken");
			return;
		}

		Loan newLoan = new Loan(borrower, book, bDate, dDate);

		int i = 0;
		while (i < 100) {
			if (loans[i] == null) {
				loans[i] = newLoan;
				borrower.addLoan(newLoan);
				break;
			}
			i++;
		}
		book.setStatus(false);
		return;
	}

	public void returnBook(Book book) {
		// find if book exists
		// find book loan
		// delete loan
		// set book status to available
		if (findBook(book.getTitle()) == null) {
			System.out.println("book is not known in system");
			return;
		}

		int i = 0;
		while (i < 100) {
			if (loans[i].book == book) {
				book.setStatus(true);
				loans[i] = null;
				break;
			}
			i++;
		}
		return;
	}

	public void printState() {
		int bookCount = 0;
		int memberCount = 0;
		int loanCount = 0;
		for (int i = 0; i < 100; i++) {
			if (books[i] != null)
				bookCount++;
		}

		for (int i = 0; i < 100; i++) {
			if (members[i] != null)
				memberCount++;
		}

		for (int i = 0; i < 100; i++) {
			if (loans[i] != null)
				loanCount++;
		}

		System.out.println("The Library currently has " + memberCount + " members. It has " + bookCount
				+ " books and " + loanCount + " loans.");
	}

}
