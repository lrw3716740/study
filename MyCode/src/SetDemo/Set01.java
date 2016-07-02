package SetDemo;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class Set01 {

	public static void main(String[] args) {

		
		Set s=new HashSet();
		s.add("111");
		s.add("112");
		s.add(111);
		s.add("111");
		s.remove("111");
		Boolean b=s.isEmpty();
		System.out.println("s:"+s);
		Iterator it =s.iterator();
		while(true){
			if (it.hasNext()){
				System.out.println(it.next());
			}
			else
				break;
		}
		System.out.println("s:"+s);

}}