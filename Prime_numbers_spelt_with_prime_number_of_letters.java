import java.util.Scanner;

public class primeNoSplet {

	/* C++ program to print a given number in words.
	   The program handles till 9 digits numbers and
	   can be easily extended to 20 digit number */
	
	// Strings at index 0 is not used, it is to make array
	// indexing simple
	static String one[] = { "", "one ", "two ", "three ", "four ",
            "five ", "six ", "seven ", "eight ",
            "nine ", "ten ", "eleven ", "twelve ",
            "thirteen ", "fourteen ", "fifteen ",
            "sixteen ", "seventeen ", "eighteen ",
            "nineteen "
          };

	// Strings at index 0 and 1 are not used, they is to
	// make array indexing simple
	static String ten[] = { "", "", "twenty ", "thirty ", "forty ",
            "fifty ", "sixty ", "seventy ", "eighty ",
            "ninety "
          };
	// n is 1- or 2-digit number
	static String numToWords(long n, String s)
	{
	    String str = "";
	    // if n is more than 19, divide it
	    if (n > 19)
	        str += ten[(int) (n / 10)] + one[(int) (n % 10)];
	    else
	        str += one[(int) n];
	 
	    // if n is non-zero
	    if (n!=0)
	        str += s;
	 
	    return str;
	}
	// Function to print a given number in words
	static String convertToWords(long n)
	{
	    // stores word representation of given number n
	    String out = "";
	 
	    // handles digits at ten millions and hundred
	    // millions places (if any)
	    out += numToWords((n / 10000000), "crore ");
	 
	    // handles digits at hundred thousands and one
	    // millions places (if any)
	    out += numToWords(((n / 100000) % 100), "lakh ");
	 
	    // handles digits at thousands and tens thousands
	    // places (if any)
	    out += numToWords(((n / 1000) % 100), "thousand ");
	 
	    // handles digit at hundreds places (if any)
	    out += numToWords(((n / 100) % 10), "hundred ");
	 
	    if (n > 100)
	    	if(n % 100 !=0)
	    		out += "and ";
	 
	    // handles digits at ones and tens places (if any)
	    out += numToWords((n % 100), "");
	 
	    return out;
	}
	static boolean isPrime(long n) {
		if(n>1) {
			for (int i=2;i<n;i++)
				if(n%i==0)
					return false;
			return true;
		}
		return false;
	}
	static String findPrime(long a,long b) {
		String n="";
		for(long i = a;i<b;i++) {
			if(isPrime(i)) {
				n+=i+",";
			}
		}
		return n;
	}
	static int spaceCount(String s) {
		int n=0;
		for(char c : s.toCharArray()) {
			if(c == ' ')
				n++;
		}
		return n;
	}
	// Driver code
	public static void main(String[] args) {
	// long handles upto 9 digit no
    // change to unsigned long long int to
    // handle more digit number
    Scanner scan = new Scanner(System.in);
    int upper_bound = scan.nextInt();
    int lower_bound = scan.nextInt();
    String s =findPrime(lower_bound, upper_bound);
    
	int count =0;
	for (String l : s.split(",")) {
		String word = convertToWords(Long.parseLong(l));
		boolean c = isPrime(word.length()-spaceCount(word));
	    // convert given number in words
		//System.out.println(l +"="+word+"="+(word.length()-spaceCount(word))+"=" + c);
	    if(c)
	    	count++;
		}
	System.out.println(count);
	}
}
