public class Loan {

	Member borrower;
	Book book;
	String borrowDate;
	String dueDate;

	public Loan(Member borrower, Book book, String bDate, String dDate) {
		this.borrower = borrower;
		this.book = book;
		borrowDate = bDate;
		dueDate = dDate;
	}
}
