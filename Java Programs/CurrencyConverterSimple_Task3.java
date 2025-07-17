import java.util.*;
public class CurrencyConverterSimple_Task3
{
    public static void main(String[] args) 
    {
        // Currency rates relative to USD
            // Currency rates relative to USD
        HashMap<String, Double> rates = new HashMap<>();
        rates.put("USD", 1.0);
        rates.put("INR", 83.5);
        rates.put("EUR", 0.92);
        rates.put("GBP", 0.78);
        rates.put("JPY", 158.2);
        rates.put("AUD", 1.49);
            
        System.out.println("=== Currency Converter ===");
        System.out.println("Supported: USD, INR, EUR, GBP, JPY, AUD");
            
        System.out.print("Enter base currency: ");
        String base = new Scanner(System.in).next().toUpperCase();
            
        System.out.print("Enter target currency: ");
        String target = new Scanner(System.in).next().toUpperCase();
            
        System.out.print("Enter amount: ");
        double amount = new Scanner(System.in).nextDouble();
            
        if (!rates.containsKey(base) || !rates.containsKey(target)) 
        {
            System.out.println("Error: Unsupported currency.");
        } 
        else 
        {
            double baseRate = rates.get(base);
            double targetRate = rates.get(target);
            double converted = (amount / baseRate) * targetRate;
            System.out.printf("%.2f %s = %.2f %s\n", amount, base, converted, target);
        }
    }
}    
