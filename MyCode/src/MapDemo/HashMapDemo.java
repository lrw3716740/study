package MapDemo;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Map m=new HashMap();
		m.put("1", "lirenwei");
		m.put("2", "lirenwei");
		Set se=m.keySet();
		String s=(String) m.get("1");
//		m.remove("1");
		
		System.out.println(m);
		System.out.println(s);
		System.out.println(se);
		System.out.println(m.size());
	}

}
