public class Member {
	int memberID;
	String name;
	Loan[] loans;

	public Member(int memberID, String name) {
		this.memberID = memberID;
		this.name = name;
		loans = new Loan[10];
	}

	public void addLoan(Loan loan) {
		int i = 0;
		while (true) {
			if (loans[i] == null) {
				loans[i] = loan;
				return;
			}
			i++;
		}
	}
}
