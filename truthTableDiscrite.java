import java.util.Arrays;

public class truthTableDiscrite {
    private static Object result2;

    public static void main(String[] args) {
        boolean[] pValues = {true ,true, false,false};
        boolean[] qValues = {true, false, true, false};

        System.out.println("Negation (NOT)");
        printHeader("p", "NOT p");
        for (boolean k : pValues) {
            boolean result = !k;
            int p = k?1:0;
            int result2 =result?1:0;
            printRow(p, result2);
        }
        System.out.p?1:println();

        System.out.println("Conjunction (AND)");
        printHeader("p", "q", "p AND q");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean result = k && j;
            int p = k;
            int q = j?1:0;
            int result2 =result?1:0;
             printRow(p , q , result2);
        }
        System.out.println();

        System.out.println("Disjunction (OR)");
        printHeader("p", "q", "p OR q");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean result = k  j;
            int p = k?1:0;
            int q = j?1:0;
            int result2 =result?1:0;
             printRow(p , q , result2);
        }
        System.out.println();

        System.out.println("Exclusive OR (XOR)");
        printHeader("p", "q", "p XOR q");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean result = k ^ j;
            int p = k?1:0;
            int q = j?1:0;
            int result2 =result?1:0;
             printRow(p , q , result2);
        }
        System.out.println();

        System.out.println("Implication (p implies q)");
        printHeader("p", "q", "p -> q");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean result = !k j;
            int p = k?1:0;
            int q = j?1:0;
            int result2 =result?1:0;
             printRow(p , q , result2);
        
        }
        System.out.println();

        System.out.println("Biconditional (p if and only if q)");
        printHeader("p", "q", "p <-> q");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean result = k == j;
            int p = k?1:0;
            int q = j?1:0;
            int result2 =result?1:0;
             printRow(p , q , result2);
            
        
        }
        System.out.println();

        System.out.println("Minterms (SOP) and Maxterms (POS)");
        printHeader("p", "q", "Minterm", "Maxterm");
        for (int i = 0; i < pValues.length; i++) {
            boolean k = pValues[i];
            boolean j = qValues[i];
            boolean min = k && j;
            boolean max = k || j;
            int p = k?1:0;
            int q = j?1:0;
            int minterm =min?1:0;
            int maxterm = max?1:0;
          printRow(p, q, minterm, maxterm);
        }
    }

    private static void printHeader(String... columns) {
        for (String column : columns) {
            System.out.printf("%-7s", column);
        }
        System.out.println();
    }

    private static void printRow(Object... values) {
        for (Object value : values) {
            System.out.printf("%-7s", value);
        }
        System.out.println();
    }

}