package ArrayListDemo;

import java.util.ArrayList;

public class day1 {

	public static void main(String[] args) {
		
		
		ArrayList array=new ArrayList ();
		array.add(123);
		array.add("lirenwei");
		System.out.println(array.get(0));
		System.out.println("array:"+array);
		array.remove(0);
		System.out.println("array:"+array);
		System.out.println("bihao");
	}

}
