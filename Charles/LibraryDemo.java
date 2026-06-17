public class LibraryDemo {

	public static void main(String[] args) {

		Library newLibrary = new Library();
		newLibrary.printState();

		Book book1 = new Book("18892", "Guardians");
		newLibrary.addBook(book1);

		Book book2 = new Book("64245", "Twilight", "James Arthur");
		newLibrary.addBook(book2);

		Book book3 = new Book("6763", "StarLink", "Elon Musk");
		newLibrary.addBook(book3);

		Member member1 = new Member(1, "Charles");
		newLibrary.registerMember(member1);

		Member member2 = new Member(2, "Elvis");
		newLibrary.registerMember(member2);

		newLibrary.lendBook(member2, book1, "2/5/2026", "4/5/2026");
		newLibrary.printState();

		newLibrary.lendBook(member1, book1, "3/5/2026", "4/5/2026");
		newLibrary.returnBook(book1);

		newLibrary.lendBook(member1, book1, "10/5/2026", "11/5/2026");
	}
}
